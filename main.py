import os
import math
import time
import socket
from dotenv import load_dotenv


choices = [
    "Choose one of the following choice", 
    "1. Do some process without network",
    "2. Connect with AWS server and have a chat 😃",
]

def do_some_process_without_network():
    HUGE_NUMBER = 99999
    WAIT_SECONDS = 0.7
    squares = []
    for i in range(1, HUGE_NUMBER):
        squares.append( i**2 )
        time.sleep(WAIT_SECONDS)
    
    print(f"Calculated Squre roots from 1 to {HUGE_NUMBER}")

    return squares


def connect_with_aws_server():
    # PATH = os.path.join(os.getcwd(), ".env")
    # path = os.environ[PATH]
    load_dotenv()

    HOST = os.getenv('HOST')
    PORT = 65432


    client_socket = socket.socket()  # instantiate
    client_socket.connect((HOST, PORT))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection



for choice in choices:
    print(choice)

user_input = int(input("\nPlease choose from above choices: "))

if user_input == 1:
    do_some_process_without_network()
else:
    connect_with_aws_server()
