#!/usr/bin/python

from __future__ import print_function
import sys, getopt
import os
import grpc
import json
from project.proto import image_processor_pb2_grpc
from project.proto import image_processor_pb2


def create_image_processor_request(image_path, operations):
    with open(image_path, "rb") as img_file:
        image = image_processor_pb2.Image(
            filename=os.path.basename(image_path),
            imagedata=img_file.read()
        )

        return image_processor_pb2.ImageProcessorRequest(
            image=image,
            operations=json.dumps(operations)
        )


def run():
    n = len(sys.argv)
    if n != 4:
        print("Syntax error!!")
        print("Try:")
        print("python grpc_client.py <input_filepath> <operations> <output_filepath>")
    else:
        inputfile = sys.argv[1]
        operations = json.loads(sys.argv[2])
        outputfile = sys.argv[3]

        # Establish connection with server.
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = image_processor_pb2_grpc.ImageProcessorStub(channel)

            # filepath = "/Users/sonalidesarda/Documents/Projects/Converted_a1f38f13-7a73-45d9-9794-b7f4144b3583.jpeg"
            # operations = [
            #     {"name": "ROTATE", "direction": "RIGHT"},
            #     {"name": "GRAYSCALE"},
            # ]

            request = create_image_processor_request(inputfile, operations)
            response = stub.GetServerResponse(request)
            img_file = open(outputfile, "wb")
            img_file.write(response.imagedata)
            print(f"Transformed image is stored at : {outputfile}")


if __name__ == '__main__':
    run()