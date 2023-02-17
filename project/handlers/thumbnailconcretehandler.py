"""
Thumbnail handler class.
"""

from project.handlers.abstracthandler import AbstractHandler
from project.handlers.Constants import const
import cv2


class ThumbnailConcreteHandler(AbstractHandler):

    def process_request(self, request):
        if const.THUMBNAIL == request.get("name"):
            scale_percent = 10
            # calculate the 50 percent of original dimensions
            print("This is {} handling request '{}'".format(self.__class__.__name__, "request"))
            width = int(self.img.shape[1] * scale_percent / 100)
            height = int(self.img.shape[0] * scale_percent / 100)
            # dsize
            dsize = (width, height)

            # resize image
            thumbnail = cv2.resize(self.img, dsize)
            AbstractHandler.thumbnail = thumbnail

            return True
