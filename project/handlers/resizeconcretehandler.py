"""
Resize handler class.
"""

from project.handlers.abstracthandler import AbstractHandler
from project.handlers.Constants import const
import cv2


class ResizeConcreteHandler(AbstractHandler):
    height = 90
    width = 90

    def process_request(self, request):
        if const.RESIZE == request.get("name"):
            self.height = request.get("height")
            self.width = request.get("width")
            points = (self.width, self.height)

            resized_img = cv2.resize(self.img, points, interpolation=cv2.INTER_LINEAR)
            AbstractHandler.img = resized_img
            print("This is {} handling request '{}'".format(self.__class__.__name__, "request"))

            return True
