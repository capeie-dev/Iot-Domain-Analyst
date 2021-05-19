#!/usr/bin/env python3
import numpy as np
import cv2
import pyocr
import pyocr.builders
from PIL import Image
import re
import datetime

# Lists serve as the file
nameList = []   
regNoList = []          
phoneNoList = []       

# Firebase path


#Regex for Registration Number
def extract_reg_number(string):
    pat3 = re.compile(r'[0-2][0-9][B|M][A-Z][A-Z][0-2][0-9][0-9][0-9]')
    re3 = pat3.findall(string)
    re3 = ''.join(re3)
    return re3

#Regex for Name
def extract_names(string):
    pattern = re.compile(r'[A-Z][a-z]+')
    names = pattern.findall(string)
    newname = ' '.join(names)
    return newname

#Regex for Phone Number
def extract_phoneNo(string):
    pat2 = re.compile(r'[6-9][0-9]{9}')
    number = pat2.findall(string)
    number = ''.join(number)
    return number

# Activate Tesseract
tools = pyocr.get_available_tools()
tool = tools[0]

# Open Camera
cap = cv2.VideoCapture(0)
while(True):
    #Image Preprocessing
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, threshd = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) 
    
    #OCR in Action
    txt = tool.image_to_string(Image.fromarray(gray), builder=pyocr.builders.TextBuilder())

    RegID = extract_reg_number(txt)
    Name = extract_names(txt)
    PhoneNumber = extract_phoneNo(txt)

    if(RegID != ""):
        regNoList.append(RegID)

    if(Name != ""):
        nameList.append(Name)
    
    if(PhoneNumber != ""):
        phoneNoList.append(PhoneNumber)


    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif RegID != "":
        print(RegID)
        break
cap.release()
cv2.destroyAllWindows()

    
 


