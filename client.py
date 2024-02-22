import threading
from socket import *

userName = input('Enter a username:')


clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('196.42.109.230',13000)) #connect client to server
     

def recieveMsgs():
    while True:
        try:
            message = clientSocket.recv(1024).decode('utf-8') #while the client is recieving messages from the server

            if message == "UserName request": #if the server is requesting the client's name:
                clientSocket.send(userName.encode('utf-8')) #Send the username

            elif message == "Would you like to be visible to other members of the server?\n type 'Yes' or 'No'":
                clientSocket.send(input("")) #allows the client to reply to the servers message

            elif message == "Select an option:\n 1.View Online Clients":
                 clientSocket.send(input("")) #allows the client to reply to the servers message
            else: 
                print(message) #if its not a username request from the server then print the message

        except:
            print("Error")
            clientSocket.close()

def sendMsgs():
    while True:
            message = input("")
            clientSocket.send(message.encode('utf-8')) #Send encoded message to another client

recieveMsgs_Thread = threading.Thread(target= recieveMsgs)
recieveMsgs_Thread.start()

sendMsgs_Thread = threading.Thread(target= sendMsgs)
sendMsgs_Thread.start()

