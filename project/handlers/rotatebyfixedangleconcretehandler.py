"""
Rotate by fixed angle handler class.
"""

from project.handlers.abstracthandler import AbstractHandler
from project.handlers.Constants import const
import cv2


class RotateByFixedAngleConcreteHandler(AbstractHandler):
    direction = const.LEFT

    def process_request(self, request):
        if const.ROTATE == request.get("name"):
            self.direction = request.get("direction")

            if self.direction == const.LEFT:
                rotated_image = cv2.rotate(self.img, cv2.cv2.ROTATE_90_CLOCKWISE)
            else:
                rotated_image = cv2.rotate(self.img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
            print("This is {} handling request '{}'".format(self.__class__.__name__, "request"))
            AbstractHandler.img = rotated_image
            print("Current value of direction :: ",self.direction)

            return True
