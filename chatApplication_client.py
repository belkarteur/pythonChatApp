from re import T
import socket
import random
from threading import Thread
from datetime import date, datetime
from tkinter.ttk import Separator
from playsound import playsound
from colorama import Fore, init, Back

#initialise colors
init()

#set the available colors
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW]

#chose a random color for the client
client_color = random.choice(colors)

#server's IP adresse, if the server is not on this machine put the private (network) I^
# addresse e.g 10.10.1.2

SERVER_HOST = "127.0.0.1" #we can still put 0.0.0.0 since in this case we are using the local addresse by default
SERVER_PORT = 4040 # server's port
separator_token = "<SEP>" #we will use it to seprate the client name and its message


#initialize TCP socket
soc = socket.socket()

print(f"[*] Connecting to {SERVER_HOST} : {SERVER_PORT}")

#connect to the server
soc.connect((SERVER_HOST, SERVER_PORT))
print("[+] connected. ")


#we now prompt the client to enter his name

name = input("Enter your name: ")


#now we ask each client to keep listening from messages from the host or server if you prefer and print it

def listen_to_messages():
    while True:
        message = soc.recv(1024).decode()
        playsound(r"hangout.mp3") #we notify the arrival of a new message by a sound.
        print("\n" + message)

# make a thread that listens for messages for this client and print

t = Thread(target=listen_to_messages) #we use thread so that the program can manage multiple connections and exchage of informatins


#make the thread daemon so it ends whenever the main thread ends
t.daemon = True
# start the thread
t.start()

# now we will listen from messages from the client and send it to the servvver

while True:
    #input message we want to send to the server
    message_to_send = input()
    
    #little precaution , we set a way to exit the program
    if message_to_send.lower() == "q" or message_to_send.lower()== "exit":
        soc.close()
        break #if the user enters just hte letter q the program will stop
    # we add the datetime , name and the color of the sender
    date_now = datetime.now().strftime('%d-%m-%Y %HH:%MM:%SS')
    message_to_send = f"{client_color}[{date_now}]{name}{separator_token}{message_to_send}{Fore.RESET}"

    #finally send the message
    soc.send(message_to_send.encode()) #encode the data so that it can be transmitted iver the network

# close the socket
soc.close()