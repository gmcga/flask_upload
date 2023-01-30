# flask_upload

Locally-hosted webpage made using Flask, ran on Raspberry Pi. The user can press a button on the webpage that causes the PiCamera attached to the Pi to take a picture which is then uploaded to the webpage.

### How to install and set up a virtual environment for flask_upload on your Raspberry Pi
*Note: flask_upload code was written for Python version 3.7.3; it is advised to have this version (ideally, or a newer version) installed to prevent any issues from occuring.*
- download all the flask_upload files to your Raspberry Pi from GitHub
- open a command line on the Raspberry Pi or [ssh into it](https://itsfoss.com/ssh-into-raspberry/) using the command prompt or your favourite IDE 
- within the IDE, navigate to the flask_upload directory using `cd` [helpful article if you aren't familiar with cd](https://www.onmsft.com/how-to/change-directories-command-prompt-windows-10-11)
- ensure you have the latest version of pip with the following command:

`python3 -m pip install --user --upgrade pip`

- install virtualenv:

`python3 -m pip install --user virtualenv`

- make sure you are in the directory where all your flask_upload files are stored, then create a virtual environment:

`python3 -m venv env`

- activate the virtual environment:

`source env/bin/activate`

- to confirm you are in the virtual environment, you can use the command `which python` which should output a directory ending in /env/bin/python
- now, install the required packages:

`python3 -m pip install -r requirements.txt`

- you should see an output similar to this:

*Successfully installed Flask-2.2.2 Jinja2-3.1.2 MarkupSafe-2.1.1 Werkzeug-2.2.2 click-8.1.3 importlib-metadata-5.2.0 itsdangerous-2.1.2 picamera-1.13 python-dotenv-0.21.0 typing-extensions-4.4.0 zipp-3.11.0*

- next, create a .env file to contain the path to the folder that contains media (e.g. images)
- on your Raspberry Pi or otherwise, navigate to the directory that contains the other program files e.g. app.py, requirements.txt, etc. 
- create a new file called ".env", then edit the file
- type in the environment variable required: MEDIA_FOLDER_PATH, which will contain the path to the media folder in this format:

`MEDIA_FOLDER_PATH="[path-to-media_folder]"` (replace [path-to-media_folder] with the path you need)
- for example, your .env file might look like this: 

`MEDIA_FOLDER_PATH="/home/pi/Desktop/flask_upload/static/media_folder/"` and the string will always end with `/static/media_folder/"`
- if you are using your Pi or an IDE that supports it such as VSCode, you can right click on media_folder and copy the folder path, then paste it in between quotes to make this process a bit easier

## You're done! 
The flask_upload web app should now be ready to run! To do this: just enter the following:

`python3 app.py` 

You should receive an output informing you of the address you can connect to to view and interact with the web app. This is typically something like http://127.0.0.1:8000. Copy this into your web browser of choice to connect to the site! 
