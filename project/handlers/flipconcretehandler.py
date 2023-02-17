"""
Flip handler class.
"""

from project.handlers.abstracthandler import AbstractHandler
from project.handlers.Constants import const
import cv2


class FlipConcreteHandler(AbstractHandler):
    flip = const.VERTICAL

    def process_request(self, request):
        if const.FLIP == request.get("name"):
            self.flip = request.get("flip")

            if const.VERTICAL == self.flip:
                flip_image = cv2.flip(self.img, 0)
            else:
                flip_image = cv2.flip(self.img, 1)
            print("This is {} handling request '{}'".format(self.__class__.__name__, "request"))

            AbstractHandler.img = flip_image

            return True
