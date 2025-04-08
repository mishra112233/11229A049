import cv2

                     
def main():
    image = cv2.imread('cat.jpg')
    if image is None:
        print("ERROR: could not find image")
        return
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("Original image", image)
    cv2.imshow("Gray image", gray_image)
    cv2.imshow("HSV image", hsv_image)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
