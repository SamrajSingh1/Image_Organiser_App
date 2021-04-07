import base64

from flask import Flask,jsonify ,request,json
import os
import cv2
import numpy as np
import pytesseract
from werkzeug.datastructures import ImmutableMultiDict
import time
app = Flask(__name__)
@app.route("/")
def dummy_apii():
    return "Hey Folks"
@app.route("/sp",methods=["GET","POST"])
def dummy_api():
        if request.method=="POST":
                data = dict(request.form)
                image = data["image"]
                ext=data["ext"]
                img1 = base64.b64decode(image)
                with open("tempImage"+ext, "wb") as fh:
                     fh.write(img1)
                img = cv2.imread("./" +"tempImage"+ext )
                os.remove("./" + "tempImage"+ext)
                detector = cv2.CascadeClassifier("haarcascade_frontalface_alt (1).xml")
                faces = detector.detectMultiScale(img)
                pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

                text = pytesseract.image_to_string(img, config='')
                if ((len(faces) < 1) & (len(text)>3))| len(text)>25:
                    return "1"+data['fname']
                elif (len(faces) > 0):
                    return "0"+data['fname']
                else:
                    return "2"+data['fname']

if __name__=="__main__":
    app.run(host='192.168.220.120',port=5111)
