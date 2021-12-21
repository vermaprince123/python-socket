import socket
client = socket.socket()
client.connect(('localhost', 9000))
done = False
while not done:
    client.send(input("[ message by You ] :- ").encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        done = True
    else:
        print("[ message from server side ] :- " + msg)
client.close()
