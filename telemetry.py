#!/usr/bin/python

import select
import socket
import re

bport = 4000
tport = 4002

bsize = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', bport))

server = None
p = re.compile('ROV@(.+)')
m = None
while not server:
    result = select.select([s],[],[])
    server = result[0][0].recv(bsize)
    m = p.match(server)
    if m:
      break
print server
host = m.group(1)

s.close()

s = socket.socket()
s.connect((host, tport))

try:
  data = s.recv(bsize)
  while data:
    print data
    data = s.recv(bsize)
except KeyboardInterrupt:
  print ''
  exit