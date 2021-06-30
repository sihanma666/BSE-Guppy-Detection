import cv2
import numpy as np
import requests
import time

cap = cv2.VideoCapture(0)
url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/46b66638-6bdf-49ba-b600-9e83a8dfe9b7/LabelFile/'
i=1
while True:
    i=i+1
    _temp,frame = cap.read()
    
    framename = 'guppy' + str(i) + '.jpg'
    cv2.imwrite(framename, frame)
    
    data = {'file': open(framename, 'rb')}
    
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('VuQnpnWewkvGPzKMmv0EM_CgE6zElUmc', ''), files=data)
    print(response.text)
    
    score = xmax = xmin = ymax = ymin = 0
    for x in d['result'][0]['prediction']:
        if x['score'] > score:
            score = x['score']
            xmax = x['xmax']
            xmin = x['xmin']
            ymax = x['ymax']
            ymin = x['ymin']
    
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord(*'g'):
        break
    time.sleep(10)
    
cap.release()
cv2.destroyAllWindows()