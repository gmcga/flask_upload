from picamera import PiCamera
from time import sleep
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

camera = PiCamera()
camera.rotation = 180

MEDIA_FOLDER_PATH = os.getenv("MEDIA_FOLDER_PATH") # path to the folder where media files are stored accessed from .env file

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") # YYYY-MM-DD-HH-MM-SS-milsec
    # guarantees each image file has a unique name in case I want to save and display multiple images later on
def picture():
    file_name = f"image_{get_current_time()}.jpg"
    camera.start_preview() 
    sleep(2) # gives camera time to adjust to lighting and focus before taking picture
    
    camera.capture(f"{MEDIA_FOLDER_PATH}{file_name}")
    camera.stop_preview()
    
    return file_name
    

