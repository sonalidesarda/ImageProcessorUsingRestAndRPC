"""
Default handler class.
"""

from project.handlers.abstracthandler import AbstractHandler
from project.handlers.Constants import const


class DefaultHandler(AbstractHandler):

    def process_request(self, request):
        if const.ORIGINAL == request.get("name"):
            AbstractHandler.img = request.get("img")
            print("This is {} handling request '{}'".format(self.__class__.__name__, "request"))
        else:
            print("This is {} telling you that request '{}' has no handler right now.".format(self.__class__.__name__,
                                                                                          "request"))

        return True
