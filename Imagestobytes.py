from PIL import Image

img=Image.open('eight.png')
data=list(img.getdata())
#print(data)
for i in range(len(data)):
    data[i]=255-data[i]
print(data)