#!/usr/bin/python3
import os
import cv2

directory = 'C:/Users/sihan/Documents/GitHub/BSE-Guppy-Detection/Dataset Output'
newdirectory = 'C:/Users/sihan/Documents/GitHub/BSE-Guppy-Detection/Dataset rotate90'
for file in os.listdir(directory):
    img = cv2.imread(directory + file)
    rotat90_img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

    #saving now
    os.chdir(newdirectory)
    cv2.imwrite(file + '_rotate90' + '.jpg', rotat90_img)
    os.chdir(directory)