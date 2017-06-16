# coding=utf-8

import socket
import time


def handle_client(sock):
    while True:
        data = raw_input('>')

        if not data:
            sock.send('BYE')
            print 'BYE'
            break
        else:
            sock.sendall(data)
            time.sleep(0.3)

        while True:
            try:
                res_data = sock.recv(1024)
                print 'Response:' + res_data
            except:
                break

    sock.close()


def init_client(server_addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_addr)
    sock.setblocking(0)

    return sock


if __name__ == '__main__':
    port = raw_input('port:')
    client = init_client(('127.0.0.1', int(port)))
    handle_client(client)
