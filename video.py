#!/usr/bin/python

import select
import socket
import re

bport = 4000
vport = 4003

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
s.connect((host, vport))

try:
  cmdline = ['vlc', '--demux', 'h264', '-']
  player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
  while True:
    data = connection.read(bsize)
    if not data:
      break
    player.stdin.write(data)
finally:
  connection.close()
  s.close()
  player.terminate()