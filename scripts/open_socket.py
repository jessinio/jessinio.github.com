import os
import sys
import socket
import select

stdout_fd = sys.stdout.fileno()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 9900))
sock.listen(5)
while True:
  s, addr_info = sock.accept()
  fd = s.fileno()
  while True:
    select.select([fd], [], [])
    input_string = s.recv(1024)
    if len(input_string) == 0:
      s.close()
      print "\nClose"
      break
    else:
        os.write(stdout_fd, input_string)
