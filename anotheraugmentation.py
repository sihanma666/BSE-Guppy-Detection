import PIL
import glob
from PIL import Image
images = glob.glob("C:/User/sihan/Documents/GitHub/BSE-Guppy-Detection/Dataset Output/*.png")
image_no = 1
for image in images:
    image.show()
    #with open(image,"rb") as file:
     #   img = Image.open(file)
      #  imgResult = img.transpose(PIL.Image.FLIP_TOP_BOTTOM).convert('RGB')
       # name = 'C:/Users/sihan/Documents/GitHub/BSE-Guppy-Detection/Dataset Output/horizflip_' + str(image_no) + '.jpg'
        #imgResult.save(name, 'JPEG')
        #image_no += 1
print("All good")