This is a simple chat application written in python. We have two files. One containing the code for the server and the other for the client. 
If you have some notion of network, you can easily understand that for a chat application to work, we need a server that will accept connection from clients and has as second function 
the dispatching of the messages send by each client.
So in the server file "server.py" we have a function which has a role, accepting different connections from clients.
A second function which listen to messages from clients and later dispatches it.
The client file "chatApplication_client.py" has a listen-to-message function which listen to new messages from the server. Then after that we wrote some line of code that
helps the client initiate a connection with the server on specific port and ip addresse (in our case: local addresse).

You can change the port number and IP addresse of the server to correspond to your own needs.
Thank you
#lovelearnhelp
