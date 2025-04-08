import cv2


def main():
    image = cv2.imread('cat.jpg')
    if image is None:
        print("ERROR: could not find image")
        return
    res_image = cv2.resize(image, (500, 500))
    cv2.imwrite("resized_image.jpg", res_image)
    print("Resized image is saved")
    cv2.imshow("Original image", image)
    cv2.imshow("Resized image", res_image)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
