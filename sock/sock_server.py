# coding=utf-8

import socket
from os import popen


def exe_cmd(cmd):
    try:
        output = popen(cmd)
        exe_result = output.read()
    except:
        exe_result = 'Executing cmd failed.'

    return exe_result


def handle_server_cmd(sock):
    while True:
        try:
            data = ''
            data_ = sock.recv(1024)
            if not data_:
                break
            data += data_

            print data

            if data.startswith('/msg'):
                sock.sendall('msg mode.')
                handle_server(sock)
            else:
                exe_result = exe_cmd(data)
                print exe_result
                sock.sendall(exe_result)
        except Exception, e:
            print e
            break


def handle_server(sock):
    while True:
        try:
            data = ''
            data_ = sock.recv(1024)
            if not data_:
                break
            data += data_

            print data

            if data.startswith('/cmd'):
                sock.sendall('cmd mode.')
                handle_server_cmd(sock)
                break
            else:
                sock.sendall('msg recevied.')

        except Exception, e:
            print e
            break


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
