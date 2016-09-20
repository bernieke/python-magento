#!/usr/bin/env python


from __future__ import print_function

import sys
import argparse

from magento.magento_api import MagentoAPI, DEFAULT_XMLRPC_PATH

try:
    from IPython import embed
except:
    print('You must have IPython installed to use this shell.\n'
          'Try "pip install ipython", "easy_install ipython", or head '
          'over to ipython.org')
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description='Launch an IPython shell '
                                     'with a MagentoAPI instance, "magento", '
                                     'connected to a given endpoint.')
    parser.add_argument('host', help='The Magento server host.')
    parser.add_argument('port', type=int, default=80,
                        help='The Magento server port.')
    parser.add_argument('api_user', help='The API user to log in as.')
    parser.add_argument('api_key', help='The API key to log in with.')
    parser.add_argument('-p', '--path', default=DEFAULT_XMLRPC_PATH,
                        help='The URL path to the XML-RPC API.')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Set the XML-RPC client to verbose.')
    parser.add_argument ('--proto', default='http', help='Choose between http or https')
    args = parser.parse_args()

    url = 'http://{}:{}/{}'.format(args.host, args.port, args.path.strip('/'))

    print('\n\n-- magento-ipython-shell -----------------')
    print('Connecting to "{}"'.format(url))
    print('Using API user/key {}/{}'.format(args.api_user, args.api_key))

    magento = MagentoAPI(args.host, args.port, args.api_user, args.api_key,
                         path=args.path, verbose=args.verbose, proto=args.proto)
    assert magento

    print('Connected! The "magento" variable is bound to a usable MagentoAPI '
          'instance.\n'
          '-- magento-ipython-shell -----------------\n\n')
    embed()  # Shell time!

if __name__ == '__main__':
    main()
