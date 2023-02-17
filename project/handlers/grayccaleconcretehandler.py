"""
Gray scale handler class.
"""

from project.handlers.abstracthandler import AbstractHandler
from project.handlers.Constants import const
import cv2


class GrayScaleConcreteHandler(AbstractHandler):

    def process_request(self, request):
        if const.GRAYSCALE == request.get("name"):
            print("This is {} handling request '{}'".format(self.__class__.__name__, "request"))

            gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            AbstractHandler.img = gray

            return True
