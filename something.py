import requests
import PIL
import glob


url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/46b66638-6bdf-49ba-b600-9e83a8dfe9b7/LabelFile/'

from PIL import Image
images = glob.glob("C:/User/sihan/Documents/GitHub/BSE-Guppy-Detection/Dataset Output/*.png")
image_no = 1
for image in images:

    data = {'file': open(image, 'rb')}

    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('VuQnpnWewkvGPzKMmv0EM_CgE6zElUmc', ''), files=data)



print(response3.text)
