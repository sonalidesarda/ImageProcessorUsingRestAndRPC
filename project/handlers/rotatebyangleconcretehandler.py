"""
Rotate by angle handler class.
"""

from project.handlers.abstracthandler import AbstractHandler
from project.handlers.Constants import const
import imutils


class RotateByAngleConcreteHandler(AbstractHandler):
    degree = 90

    def process_request(self, request):
        if const.ROTATE_BY_ANGLE == request.get("name"):
            self.degree = request.get("degree")

            rotate_image = imutils.rotate(self.img, self.degree)
            print("This is {} handling request '{}'".format(self.__class__.__name__, "request"))
            AbstractHandler.img = rotate_image
            print("Current value of degree :: ",self.degree)

            return True
