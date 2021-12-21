import socket
server = socket.socket()
server.bind(("localhost", 9000))
server.listen()
client, addres = server.accept()
done = False
while not done:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        done = True
    else:
        print("[ message from prince verma side ] :- " + msg)
    client.send(input("[ message by You ] :- ").encode('utf-8'))
client.close()
server.close()
