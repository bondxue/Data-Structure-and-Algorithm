from collections import defaultdict


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):

        self.root = RouteTrieNode(handler)

    def insert(self, path_parts, handler):
        node = self.root
        for part in path_parts:
            node.insert(part)
            node = node.children[part]
        node.handler = handler

    def find(self, path_parts):
        node = self.root
        for part in path_parts:
            if part in node.children:
                node = node.children[part]
            else:
                return None
        return node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:

    def __init__(self, handler=None):
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler

    def insert(self, path):
        self.children[path] = RouteTrieNode()


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler, not_found_handler):
        self.routeTrie = RouteTrie(handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        path_parts = self.split_path(path)
        self.routeTrie.insert(path_parts, handler)

    def lookup(self, path):
        path_parts = self.split_path(path)
        handler = self.routeTrie.find(path_parts)
        if handler is None:
            return self.not_found_handler
        else:
            return handler

    @staticmethod
    def split_path(path):
        path = path.strip("/")
        return path.split("/") if path else []


# Here are some test cases and expected outputs you can use to test your implementation
# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup(""))  # Empty Path, should print 'root handler'

