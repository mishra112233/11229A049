import cv2
image = cv2.imread('tank.bmp')
y_start, y_end = 10, 155
x_start, x_end = 10, 155
cropped_image = image[y_start:y_end, x_start:x_end]
cv2.imshow('Original Image', image)
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('cropped_image.jpg', cropped_image)
