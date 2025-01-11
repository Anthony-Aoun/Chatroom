import socket
import threading

# Function to handle each client
def handle_client(client_socket, client_address, clients, client_names):
    # Receive the client's name
    client_name = client_socket.recv(1024).decode('utf-8')
    client_names[client_socket] = client_name

    # Broadcast that the client has joined
    welcome_message = f"{client_name} has joined the chat!"
    print(welcome_message)
    broadcast_message(welcome_message, client_socket, clients)

    while True:
        try:
            # Receive the message from the client
            message = client_socket.recv(1024).decode('utf-8')
            
            if not message:
                break

            # Format the message to show the client's name
            formatted_message = f"{client_name}: {message}"
            print(f"Received from {client_address}: {formatted_message}")

            # Broadcast the message to other clients
            broadcast_message(formatted_message, client_socket, clients)

        except ConnectionResetError:
            break

    # Client has left the chat
    print(f"Connection closed: {client_address}")
    client_socket.close()
    clients.remove(client_socket)
    leave_message = f"{client_name} has left the chat."
    print(leave_message)
    broadcast_message(leave_message, client_socket, clients)
    del client_names[client_socket]

# Function to broadcast message to all clients except the sender
def broadcast_message(message, sender_socket, clients):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                # Send the message to the client
                client_socket.send(message.encode('utf-8'))
            except BrokenPipeError:
                continue

# Server setup
def start_server(host='127.0.0.1', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server started on {host}:{port}")

    clients = []
    client_names = {}

    while True:
        # Accept new client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        clients.append(client_socket)
        
        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address, clients, client_names))
        client_thread.start()

if __name__ == "__main__":
    start_server()
