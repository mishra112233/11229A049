import cv2
from PIL import Image
import matplotlib.pyplot as plt

# List of image file paths (you can change these to your image paths)
image_paths = [
    'C:\\Users\\CSE\\Desktop\\image.jpg',  # JPG image
    'C:\\Users\\CSE\\Desktop\\image.png',  # PNG image
    'C:\\Users\\CSE\\Desktop\\image.bmp',  # BMP image
    'C:\\Users\\CSE\\Desktop\\image.tiff'  # TIFF image
]


# Function to display an image using OpenCV
def display_with_opencv(image_path):
    image = cv2.imread(image_path)
    cv2.imshow(f'Image: {image_path}', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Function to display an image using PIL and matplotlib
def display_with_pil(image_path):
    image = Image.open(image_path)
    plt.imshow(image)
    plt.title(f"Image: {image_path}")
    plt.axis('off')  # Turn off axis
    plt.show()


# Loop through the image paths and display them using OpenCV and PIL
for image_path in image_paths:
    print(f"Displaying image using OpenCV: {image_path}")
    display_with_opencv(image_path)

    print(f"Displaying image using PIL: {image_path}")
    display_with_pil(image_path)
