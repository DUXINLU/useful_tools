# coding=utf-8

import socket


def handle_server(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print 'receving:%s' % (data,)
        except Exception, e:
            print e
            break

        sock.sendall('msg recevied')


def init_server(addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(addr)
    print 'server running on %s' % (addr,)
    sock.listen(1)

    while True:
        print 'waiting for connection...'
        sock_client, addr = sock.accept()
        print 'connect from %s' % (addr,)

        handle_server(sock_client)


if __name__ == '__main__':
    port = raw_input('port:')
    sock_server = init_server(('127.0.0.1', int(port)))
