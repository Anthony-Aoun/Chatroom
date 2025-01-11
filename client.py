import socket
import threading
import time
import argparse

# Function to print messages with a slight delay for better visualization
def print_modified(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Move to the next line after printing the entire string

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            # Receive the message from the server
            message = client_socket.recv(1024).decode('utf-8')
            
            if not message:
                break
            
            # Print the received message
            print_modified(message)

        except ConnectionResetError:
            break

# Client setup and main loop
def start_client(client_name, host='127.0.0.1', port=5000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    # Send the client name to the server
    client_socket.send(client_name.encode('utf-8'))

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        if message.lower() == 'exit':
            break

        # Send the message to the server
        client_socket.send(message.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Process some client name.')
    parser.add_argument('--name', type=str, required=True, help='Name of the client')
    args = parser.parse_args()
    client_name = args.name
    
    print(f"Client Interface: {client_name}\n")
    
    start_client(client_name)
