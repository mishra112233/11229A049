import cv2


def main():
    image = cv2.imread("download.jpg")
    if image is None:
        print("error:could not read the image")
        return
    res_image = cv2.resize(image, (500, 500))
    cv2.imwrite("resized_image.jpg", res_image)
    print("resized image saved")
    cv2.imshow("original image", image)
    cv2.imshow("resized image", res_image)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

