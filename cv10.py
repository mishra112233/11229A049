import cv2
image = cv2.imread('bullet.tiff')
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
rotated_image_1 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
rotated_image_2 = cv2.rotate(image, cv2.ROTATE_180)
cv2.imshow("Original Image", image)
cv2.imshow("90 Degree", rotated_image)
cv2.imshow("-90 Degree",rotated_image_1)
cv2.imshow("180 Degree",rotated_image_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
from PIL import Image
image_path = "csk.jpg"
img = Image.open(image_path)
angle = 45
rotated_img = img.rotate(angle, expand=True)
rotated_img.show()
rotated_img.save(f'rotated_{angle}_degrees.jpg')
