python-magento
==============

This is a simple Python interface to Magento's XML-RPC API. The API
discovers and makes all of Magento's API methods available to you.

Usage
-----

.. code:: python

    from magento import MagentoAPI

    magento = MagentoAPI("magentohost.com", 80, "test_api_user", "test_api_key")

    magento.help() # Prints out all resources discovered and available.
    # cart: create, info, license, order, totals
    # cart_coupon: add, remove
    # ... (a bunch of other resources)
    # sales_order: addComment, cancel, hold, info, list, unhold

    magento.sales_order.help() # 'sales_order' is a resource.
    # sales_order: Order API
    #   - addComment: Add comment to order
    #   - cancel: Cancel order
    #   - hold: Hold order
    #   - info: Retrieve order information
    #   - list: Retrieve list of orders by filters
    #   - unhold: Unhold order

    # Let's list sales and add their subtotals!
    orders = magento.sales_order.list()
    subtotals = [order["subtotal"] for order in orders]
    revenue = sum(subtotals)

    # Additionally, you can get API metadata from these calls:
    json_description_of_resources = magento.resources()
    json_description_of_possible_global_exceptions = magento.global_faults()
    json_description_of_possible_resource_exceptions = magento.resource_faults("sales_order")

The API discovers and makes all of Magento's API methods available to
you. The best way to learn how to use the API is to play around with it
in a Python shell and refer back to the `Magento API
documentation <http://www.magentocommerce.com/api/soap/introduction.html>`__
for docs on the usage of specific methods.

Quick IPython Shell
-------------------

The Magento API is massive and takes effort to grok. If you need to use
it in some production capacity, you'll want to jump into a shell
frequently and muck around with inputs and stare at outputs.

``magento-ipython-shell`` will drop you into an IPython shell that has a
variable bound to a MagentoAPI object that is ready for use.

The shell requires IPython, which is the bee's knees. Install it and get
it working first. Alternately, spin up a Python shell and instantiate
the objects you need. This is just a slightly nicer way to get started
mucking around.

Here's how to launch it:

::

    > magento-ipython-shell localhost.com 8888 api_user api_key

    -- magento-ipython-shell -----------------
    Connecting to 'http://localhost.com:8888/magento/api/xmlrpc'
    Using API user/key api_user/api_key
    Connected! The 'magento' variable is bound to a usable MagentoAPI instance.
    -- magento-ipython-shell -----------------

    Python 2.7.2 (default, Jun 16 2012, 12:38:40) 
    Type "copyright", "credits" or "license" for more information.

    IPython 0.13.1 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]:

Now you can mess around with the ``magento`` instance.

::

    In [1] magento
    Out[1]: <magento.MagentoAPI at 0x107d3c310>

    In [2]: magento.help() # Lists all the resources available and their methods.
    Resources:

    cart: create, info, license, order, totals
    cart_coupon: add, remove
    ... (many more)

    In [3]: magento.cart.help() # Describes the methods available under a resource.
    cart: Shopping Cart
      - create: Create shopping cart
      - info: Retrieve information about shopping cart
      - license: Get terms and conditions
      - order: Create an order from shopping cart
      - totals: Get total prices for shopping cart

    In [4]: len(magento.sales_order.list()) # Play around with output.
    Out[4]: 2

Installation
------------

python-magento is on PyPi:

-  ``pip install python-magento``
-  ``easy_install python-magento``

... or grab this code and run ``setup.py install``
