import xmlrpclib

class MagentoAPI(object):
    PATH = "/magento/api/xmlrpc"

    def __init__(self, host, port, api_user, api_key):
        uri = "http://%s:%s" % (host, str(port)) + MagentoAPI.PATH
        self._client = xmlrpclib.ServerProxy(uri)
        self._session_id = self._client.login(api_user, api_key)
        self._discover()

    def _discover(self):
        self._resources = {}
        resources = self._client.resources(self._session_id)
        for resource in resources:
            self._resources[resource["name"]] = MagentoResource(
                self._client, self._session_id, resource["name"], 
                resource["title"], resource["methods"])

    def __getattr__(self, name):
        if name in self._resources:
            return self._resources[name]
        else:
            raise AttributeError
        
    def get_client(self):
        return self._client

    def help(self, resource=None, method=None):
        if not resource:
            print "Resources:"
            print
            for name in sorted(self._resources.keys()):
                print "- %s" % (name)

        if resource:
            resource = self._resources.get(resource)
            if not resource:
                print "'%s' is not a valid resource." % resource
                return
            resource.help()


class MagentoResource(object):
    def __init__(self, client, session_id, name, title, methods):
        self._client = client
        self._session_id = session_id
        self._name = name
        self._title = title
        self._methods = {}
        
        for method in methods:
            self._methods[method["name"]] = method

    def __getattr__(self, name):
        if name in self._methods:
            return self._get_method_call(name)
        else:
            raise AttributeError
        
    def _get_method_call(self, method_name):
        path = ".".join([self._name, method_name])
        def call_method(*args, **kwargs):
            return self._client.call(self._session_id, path, *args)
        return call_method

    def help(self, method=None):
        print "%s: %s" % (self._name, self._title)
        for method in sorted(self._methods.keys()):
            print "  - %s: %s" % (method, self._methods[method]["title"])
    
