import socket
from threading import Thread
from tokenize import String


#server's IP address

SERVER_HOST = "0.0.0.0" #local machine adresse
SERVER_PORT = 4040 #port to use in our communication
separator_token = "<SEP>" #the seperator we will use to separate the  client name and its message

vr = True

#we create a list to contain the client's name connected to the socket  and initialize them

clientList_sockets = set()

#create a TCP socket
soc = socket.socket()

#make the port to be a reusable port

soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

#bind the socket to the adress we specified
soc.bind((SERVER_HOST,SERVER_PORT))

#listen for upcoming connections
soc.listen(5) #5 specifies the number of unaccepted connections that the system will allow before refusing new connections

print(f"[*] listening as {SERVER_HOST}:{SERVER_PORT}")

#possible messages to stop the server
#serverEnd = ["exit","end","stop", "stop server"]

#we will write a function below that will accept data reaching the server

def listen_to_clients(client_socket):
    """
    this function keep listening for a message from "client_socket"
    and broadcast the message to all other connected clients.
    """
    while True:
        try:
            #keep listening to messages from client_socket socket
            message = client_socket.recv(1024).decode() #The bufsize argument of 1024 used here is the maximum amount of data to be received at once. It doesn’t mean that .recv() will return 1024 bytes
        except Exception as e:
            #client no longer connected , remove it from the set(list of connected clients)
            print(f"[!] Error: {e}")
            clientList_sockets.remove(client_socket)
            client_socket.close()
            
        else:
            #if we receive a message, replace the <SEP> token with ":" for good printing
            message = message.replace(separator_token,": ")
          
            #iterate over all connected sockets


            for client in clientList_sockets:
                # if msg and val== True:
                #     msg = msg + " " + re.findall("\](.*?)\:",message)[0]
                #     client.send(msg.encode())
                    #val =False
                
            # propagate the message
                client.send(message.encode())



while True:
    try:
        # we need to keep listening to connections all the time
        clientSocket, client_address = soc.accept()

        #vr = True
        #msg = "a user is connected with name : "

        print(f"[+] {client_address} connected")
        
        #add the new connected client to the list of connected sockets
        clientList_sockets.add(clientSocket)
        
        #start a new thread that listens for each client's messages

        t = Thread(target=listen_to_clients, args=(clientSocket,))
        #vr = False

        #make the thread daemon so it ends whenever the main thread ends

        t.daemon = True

        #start the thread
        t.start()
    except:
        
        #close client sockets
        for cs in clientList_sockets:
            cs.close()
        #close server socket too
        soc.close()


