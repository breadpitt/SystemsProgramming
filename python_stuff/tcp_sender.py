#!/usr/local/bin/python3

import sys

from socket import socket, AF_INET, SOCK_STREAM

ip = sys.argv[1]
port = sys.argv[2]
data = sys.argv[3]

tcp_sock = socket(AF_INET, SOCK_STREAM)

tcp_sock.connect((ip,port))

ret = tcp_sock.send(bytes(data, 'utf-8'))

print("sent")
