import os
import sys
import socket
import select


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 8082))
sock.listen(10)
binding_fd = sock.fileno()

fd_list = [binding_fd]
sock_list = []

while True:
    read_list = select.select(fd_list, [], [])[0]
    for fd in read_list:
        if fd == binding_fd:
            s = sock.accept()[0]
            sock_list.append(s)
            fd_list.append(s.fileno())
        else:
            d = os.read(fd, 10240)
            if len(d) == 0:
                print 'close %s' % fd
                fd_list.remove(fd)
            else:
                os.write(1, d)

