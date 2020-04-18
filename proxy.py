import socket
import sys
import threading

def __init__(self, config):

    signal.signal(sognal.SIGNIT, slef.shutdown)

    self.serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    self.serverSocket.stsockopt(socket.SOL_SOCKET, socket.REUSEADDR,1)

    self.serverSocket.bind((conid['HOST_NAME'], config['BIND_PORT']))

    self.serverSocket.listen(10)

    self.__clients={}

#Accept client 

    while True:
    
        (clientSocket, client_address) = self.serverSocket.accept()

        d = threading.Thread(name=slf._getClientName(client_address),
             target=self.proxy_thread, args=(clientSocket,client_addresss),
             daemon=True) 
        d.start()
    #get the request from the browser

request = conn.recv(config['MAX_REQUEST_LEN'])
    
    #parsing the first line
first_line = request.split('\n')[0]

    #getting url
url = first_line.split(' ')[1]

http_pos = url.find("://")

if(http_pos == -1):
    temp=url
else:
    temp=url[(http_pos+3):]

port_pos = temp.find(":")

    # find end
webserver_pos = temp.find("/")

if webserver_pos == -1:
    webserver_pos=len(url)
    
webserver=""
port=-1
if(port_pos==-1 or webserver_pos<port_pos):
    port=80
    webserver = temp[:webserver_pos]
else:
    port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
    webserver = temp[:port_pos]

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(config['CONNECTION_TIMEOUT'])
s.connect((webserver,port))
s.sendall(request)

while 1:
    # receive data from web server
    data = s.recv(config['MAX_REQUEST_LEN'])

    if (len(data) > 0):
        conn.send(data) # send to browser/client
    else:
        break
























