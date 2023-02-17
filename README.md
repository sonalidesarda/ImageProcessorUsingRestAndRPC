Prerequisites:
1. Python 3.5 or higher
2. pip version 9.0.1 or higher


Steps to run the applications:
1. Upnzip the image_processpor.zip file
2. Go the unzipped directory location in terminal/command promt
3. Go inside ImageProcessorApplication directory
4. Run following command to upgrade the pip:
	$ python -m pip install --upgrade pip
5. Run following commands to create virtual environment:
	$ python -m pip install virtualenv
	$ virtualenv venv
	$ source venv/bin/activate
	$ python -m pip install --upgrade pip
6. Install required packages:
	$ pip install -r requirements.txt
7. Set application root directory as PYTHONPATH:
	$ export PYTHONPATH="$PWD"
8. Go to /project directory
	$ cd project
9. Run following command to start flask server:
	$ python flask_server.py
10. Possible operations json string:
	[{"name": "ROTATE", "direction": "RIGHT"}, {"name": "ROTATE", "direction": "LEFT"}, {"name": "ROTATE_BY_ANGLE", "degree": 190}, {"name": "RESIZE", "height": 400, "width": 250}, {"name": "GRAYSCALE"}, {"name": "FLIP"}, {"name": "THUMBNAIL"}]
11. Rest client can be accessed using swagger webpage. Visit http://127.0.0.1:5000/apidocs/.
12. Run following command to start grpc server:
	$ python grpc_server.py
13. Open new terminal and git to ImageProcessorApplication folder. Run following command:
	$source venv/bin/activate	
14. grpc client can be accessed using terminal. Go to root ImageProcessorApplication directory. Run following command:
	$ python grpc_client.py <input_filepath> <operations> <output_filepath>

	Example:
	$ python grpc_client.py /Users/sonalidesarda/Documents/Images/jpeg/output.jpeg '[{"name": "ROTATE", "direction": "RIGHT"}]' /Users/sonalidesarda/Documents/Images/jpeg/output_final.jpeg



