from flask import Flask, render_template, request, redirect, url_for
import os
from get_image import picture

MEDIA_FOLDER = os.path.join("static", "media_folder") # where images are stored

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = MEDIA_FOLDER

image_filename = os.path.join(app.config["UPLOAD_FOLDER"], "initial_image.jpg") # website first loads with the initial image being displayed

@app.route("/", methods=["GET", "POST"])
def index():
    global image_filename # try to figure out a way to not use global variable for this
    if request.method == "POST": # button pressed
        if request.form.get("action1") == "Press to get picture":
            image_filename = os.path.join(app.config["UPLOAD_FOLDER"], picture()) # takes picture
        
        return redirect(url_for("index")) # if button is not pressed, just get index
    elif request.method == "GET": # get the webpage
        return render_template("index.html", user_image = image_filename)
    
    return render_template("index.html", user_image = image_filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False) # run with debug mode off to prevent picamera out of memory error

    
    