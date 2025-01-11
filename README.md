# Chatroom - Server & Clients

A simple local Python chatroom application, demonstrating basic client-server communication using sockets. The project includes:

- A server (`server.py`) that manages client connections and broadcasts messages to all connected clients.
- A client (`client.py`) that sends messages to the server and receives broadcasted messages.
- A main script (`main.py`) that automates the launching of the server and multiple clients.

## Features

- Multiple clients can join a chatroom and send messages.
- The server broadcasts messages to all connected clients.
- Clients can see messages sent by other clients.
- Each client has a unique name.
- The main script allows for easy setup of the server and clients.

## Requirements

- Python 3.x
- No external dependencies (uses built-in `socket` and `threading` modules)

## Files

### `main.py`

- Launches the server and multiple clients.
- Prompts the user to input the number of clients and their names.
- Automatically opens new terminal windows to run both the server and clients.

### `server.py`

- Listens for incoming client connections.
- Handles each connected client in a separate thread.
- Broadcasts messages to all connected clients.
- Informs all clients when someone joins or leaves the chat.

### `client.py`

- Connects to the server using a specified name.
- Sends messages to the server.
- Receives and prints messages broadcasted by the server.
- Clients can type messages and send them to the chatroom.

## How to Run

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Anthony-Aoun/Chatroom.git
    cd Chatroom
    ```
   

2. **Run the `main.py` script:**

    To start the server and clients, run the `main.py` script. It will prompt you for the number of users and their names. The script will then open the required terminal windows to start the server and clients.

   ```bash
   python main.py
   ```


    - The server will start first.
    - The script will ask for the number of clients and their names.
    - Clients will be launched in separate cmd windows.

3. **Interact with the chatroom:**

    - Each client can type a message and send it to the server.
    - The server will broadcast messages to all clients.
    - Type `exit` to close a client connection.

## Example

    Server started on 127.0.0.1:5000
    Connection from ('127.0.0.1', 12345)
    User 1 - Name: Alice
    User 2 - Name: Bob

    > Alice has joined the chat!
    > Bob has joined the chat!
    > Alice: Hello, Bob!
    > Bob: Hello, Alice!
    > Alice has left the chat.

## Notes

- This project runs locally (on `localhost`), so all clients and the server are on the same machine.
- Each client is launched in a separate terminal window.
- The server can handle multiple clients at once using threads.

## License
This project is licensed under the MIT License.

## Author
© 2025 [Anthony Aoun](https://github.com/Anthony-Aoun). All rights reserved.

This project is open-source and free to use for educational purpouses only.