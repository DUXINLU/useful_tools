import sys
import getopt
from sock_client import *
from sock_server import *

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'csi:p:')

    opts_dict = dict(opts)

    if '-i' in opts_dict:
        ip = opts_dict['-i']
    if '-p' in opts_dict:
        port = int(opts_dict['-p'])
    if '-c' in opts_dict:
        client = init_client((ip, port))
        handle_client(client)
    elif '-s' in opts_dict:
        init_server((ip, port))
