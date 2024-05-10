from PIL import Image

ashi= int(input('enter the height of the required image to be resized: '))
ashi1= int(input('enter the width of the required image to be resized: '))

image = Image.open('D:\pythonpratice\download.jpg')

new_image = image.resize((ashi,ashi1))
new_image.show()


