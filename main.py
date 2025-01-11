# -*- coding: utf-8 -*-
import subprocess
import os
import time

# Main entry point for launching server and clients
def run_python_server_file_in_new_cmd(file_to_run):
    # Get the absolute path of the file to run
    abs_file_path = os.path.abspath(file_to_run)
    
    # Construct the command to open a new cmd window and run the Python file
    command = f'start cmd /k "python {abs_file_path}"'
    
    # Execute the command
    subprocess.run(command, shell=True)

def run_python_client_file_in_new_cmd(file_to_run, client_name):
    # Get the absolute path of the file to run
    abs_file_path = os.path.abspath(file_to_run)
    
    # Construct the command to open a new cmd window and run the Python file with the client name
    command = f'start cmd /k "python {abs_file_path} --name {client_name}"'
    
    # Execute the command
    subprocess.run(command, shell=True)


if __name__ == "__main__":
    # Ask for the number of clients
    nbclients = int(input("Enter the number of users: "))

    # Collect client names
    allclients = []
    for i in range(nbclients):
        client_name = input(f'\n> User {i+1} - Name: ')
        allclients.append(client_name)
        
    # Start the server
    run_python_server_file_in_new_cmd('server.py')
    time.sleep(1)  # Wait for the server to initialize
    
    # Start clients
    for client_name in allclients:
        run_python_client_file_in_new_cmd('client.py', client_name)
        time.sleep(2)  # Wait a moment before starting the next client
        
    # Close all cmd windows after execution
    os.system('taskkill /F /IM cmd.exe')
