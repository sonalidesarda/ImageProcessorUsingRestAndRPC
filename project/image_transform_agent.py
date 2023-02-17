"""
Image transform agent.
"""

from project.handlers.defaulthandler import DefaultHandler
from project.handlers.flipconcretehandler import FlipConcreteHandler
from project.handlers.grayccaleconcretehandler import GrayScaleConcreteHandler
from project.handlers.resizeconcretehandler import ResizeConcreteHandler
from project.handlers.rotatebyangleconcretehandler import RotateByAngleConcreteHandler
from project.handlers.rotatebyfixedangleconcretehandler import RotateByFixedAngleConcreteHandler
from project.handlers.thumbnailconcretehandler import ThumbnailConcreteHandler


class ImageTransformAgent:

    def __init__(self):
        """Provides the sequence of handles for the users"""
        initial = None
        self.handler = ResizeConcreteHandler(ThumbnailConcreteHandler(GrayScaleConcreteHandler(FlipConcreteHandler\
                       (RotateByAngleConcreteHandler(RotateByFixedAngleConcreteHandler(DefaultHandler(initial)))))))

    def agent(self, user_request):
        """Iterates over each request and sends them to specific handles"""
        output_image = None
        print("Length", len(user_request))
        for request in user_request:
            print("Testsssss")
            output_image = self.handler.handle(request)

        return output_image
