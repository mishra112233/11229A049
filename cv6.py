import cv2

image = cv2.imread('cat.jpg')
text = "cat"
position = (50, 50)  # (x, y) coordinates
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 0, 255)  # red in BGR
cv2.putText(image, text, position, font, font_scale, font_color)
cv2.imshow('Image with Text', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
