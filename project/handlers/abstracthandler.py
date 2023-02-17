"""
Abstract handler class.
"""


class AbstractHandler(object):
    """Parent class of all concrete handlers"""
    img = None
    thumbnail = None

    def __init__(self, nxt):
        """change or increase the local variable using nxt"""
        self._nxt = nxt

    def handle(self, request):
        """It calls the processRequest through given request"""
        print(self.__class__.__name__, request.get("name"))
        handled = self.process_request(request)

        """case when it is not handled"""
        if not handled:
            self._nxt.handle(request)

        return self.img

    def process_request(self, request):
        """throws a NotImplementedError"""
        raise NotImplementedError('First implement it !')
