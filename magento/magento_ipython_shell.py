#!/usr/bin/env python

import sys
import argparse
from magento import MagentoAPI

try:
    from IPython import embed
except:
    print "You must have IPython installed to use this shell. Try"
    print "'pip install ipython', 'easy_install ipython' , or head"
    print "over to ipython.org."
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description=\
            "Launch an IPython shell with a MagentoAPI instance, 'magento' " + \
            "connected to a given endpoint.")
    parser.add_argument("host", help="The Magento server host.")
    parser.add_argument("port", type=int, help="The Magento server port.")
    parser.add_argument("api_user", help="The API user to log in as.")
    parser.add_argument("api_key", help="The API key to log in with.")
    parser.add_argument("-p", "--path", help="The URL path to your instance's XML-RPC API.")
    parser.add_argument("-v", "--verbose", action="store_true", 
                        help="Set the XML-RPC client to verbose.")
        
    args = parser.parse_args()

    endpoint = {
        "host": args.host,
        "port": args.port,
        "api_user": args.api_user,
        "api_key": args.api_key,
        "path": args.path,
        "verbose": args.verbose
    }

    path = args.path if args.path else MagentoAPI.PATH
    url = "http://%s:%d" % (args.host, args.port) + path

    print
    print
    print "-- magento-ipython-shell -----------------"
    print "Connecting to '%s'" % url
    print "Using API user/key %s/%s" % (args.api_user, args.api_key)
    magento = MagentoAPI(**endpoint)
    print "Connected! The 'magento' variable is bound to a usable MagentoAPI instance."
    print "-- magento-ipython-shell -----------------"
    print
    print
    embed() # Shell time!

if __name__ == "__main__":
    main()
