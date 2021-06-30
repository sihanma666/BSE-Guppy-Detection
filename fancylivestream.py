import os
import cv2
import numpy as np
import requests
import time
import json
from datetime import datetime
from PIL import Image
import PIL

cap = cv2.VideoCapture(0)
url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/46b66638-6bdf-49ba-b600-9e83a8dfe9b7/LabelFile/'
i=1
while True:
    i=i+1
    _temp,frame = cap.read()
    
    
    """now = datetime.now()
    y = now.strftime("%Y")
    m = now.strftime("%m")
    d = now.strftime("%d")
    t = now.strftime("%H:%M:%S")
    date_time = now.strftime("%m%d%Y%H%M%S")"""
    framename = 'guppy' + str(i) + '.jpg'
    
    cv2.imwrite(framename, frame)
    
    data = {'file': open(framename, 'rb')}
    
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('VuQnpnWewkvGPzKMmv0EM_CgE6zElUmc', ''), files=data)
    print('API called')
    
    d = json.loads(response.text)
    #print(d)
    
    score = xmax = xmin = ymax = ymin = 0
    for x in d['result'][0]['prediction']:
        if x['score'] > score:
            score = x['score']
            xmax = x['xmax']
            xmin = x['xmin']
            ymax = x['ymax']
            ymin = x['ymin']
            
    """score = d['result'][0]['prediction'][0]['score']
    xmax = d['result'][0]['prediction'][0]['xmax']
    xmin = d['result'][0]['prediction'][0]['xmin']
    ymax = d['result'][0]['prediction'][0]['ymax']
    ymin = d['result'][0]['prediction'][0]['ymin']"""
    
    #if score<0.8:
        
    cv2.imshow("Frame", frame)
    
    

    if cv2.waitKey(1) & 0xFF == ord(*'g'):
        break
    time.sleep(10)
    
cap.release()
cv2.destroyAllWindows()
