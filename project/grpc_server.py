import os.path
from concurrent import futures
from project.image_transform_agent import ImageTransformAgent
import grpc
import cv2
import json
from project.handlers.Constants import const
from proto import image_processor_pb2
from proto import image_processor_pb2_grpc

class ImageProcessorService(image_processor_pb2_grpc.ImageProcessorServicer):

    def GetServerResponse(self, request, context):
        operations = json.loads(request.operations)
        print(operations)

        # Save original image to temporary location.
        temp_image_filepath = os.path.join(const.TEMP_IMAGE_FOLDER, request.image.filename)
        with open(temp_image_filepath, "wb+") as temp_file:
            temp_file.write(request.image.imagedata)

        # Read original image from temporary location.
        img = cv2.imread(temp_image_filepath)
        image_transformer = ImageTransformAgent()

        print(type(img))

        list_of_operations = list()
        list_of_operations.append({"name": const.ORIGINAL, "img": img})
        list_of_operations.extend(operations)
        # print(list_of_operations)

        """Send the requests one by one, to handlers as per the sequence of handlers defined in the Client class"""
        output_img = image_transformer.agent(list_of_operations)

        # Write transformed image to temporary location
        cv2.imwrite(temp_image_filepath, output_img)

        with open(temp_image_filepath, "rb") as temp_file:
            image = image_processor_pb2.Image(
                filename=os.path.basename(f"Converted_{request.image.filename}"),
                imagedata=temp_file.read()
            )

        return image


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_processor_pb2_grpc.add_ImageProcessorServicer_to_server(ImageProcessorService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()