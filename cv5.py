import cv2
from PIL import Image

image = cv2.imread('image.jpg')


print("Image Height:", image.shape[0])
print("Image Width:", image.shape[1])
print("Number of Channels:", image.shape[2])
print("Image Size (in Pixels):", image.size)
print("Image Data Type:", image.dtype)
image = Image.open('C:\\Users\\CSE\\Desktop\\image.jpg')

print("Image Format:", image.format)
