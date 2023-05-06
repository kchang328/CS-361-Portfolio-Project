# CS-361-Portfolio-Project

Communication Contract

# Requesting data via microservice
To make a request to the string reversal microservice, the client side must connect to the microservice via a socket and then send an existing text file from the project directory. Here is an example call: client.send("input.txt".encode('utf-8')

# Receiving data via microservice
To receive data from the microservice, the client side must be connected to the microservice and then wait to receive data from the microservice. The microservice will write to the the same file that it received and send a status code. "R0" means that string reversal was completed successfully. "0" means that the file was empty. "N0" means that the file name that was sent does not exist. Here is an example of how to receive data on the client side: client.recv(1024).decode('utf-8')
