import hug
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import sys
import pybase64
from io import StringIO
import base64
from PIL import Image
import json

@hug.get('/happy_birthday')
def happy_birthday(name, age:hug.types.number=1):
    return f"Happy {age} Birthday {name}!"

@hug.post('/image1')
def image1(name):
    return f"Success {name}"

@hug.post('/barcode')
def decode(data):
    img = base64.b64decode(data)
    jpg_as_np = np.frombuffer(img, dtype=np.uint8)
    image_buffer = cv2.imdecode(jpg_as_np, flags=1)
    decodedObjects = pyzbar.decode(image_buffer)
    print ("test")
    if len(decodedObjects) >0:
        for obj in decodedObjects:
            ttype = obj.type
            data = obj.data
        return f"ttype = {ttype} and data = {data}"
    else:
        return f"Sorry was unable to process the last request try again"
