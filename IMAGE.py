from PIL import Image
import numpy as np 
image = Image.open('kartinka.jpg')

imarray = np.asarray(image)
length = 1278
heigth = 1920

for i in range(length-1):
    for j in range(heigth-1, 0, -1):
        imarray[i, j] = 0

#print(imarray[1277, 1919])
im = Image.fromarray(imarray)
im.show()