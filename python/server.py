# -*- coding: utf-8 -*-

import socket

HOST = ''
PORT = 9966

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print 'Serving HTTP on port %s ...' % PORT

while True:
    client_connention, client_address = listen_socket.accept()
    request = client_connention.recv(1024)
    print request

    http_response = '''\
HTTP/1.1 200 OK

Hello, World!
'''
    
    client_connention.sendall(http_response)
    client_connention.close()
