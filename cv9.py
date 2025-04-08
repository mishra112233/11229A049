import cv2
def read_and_display_images():
    image_paths = [
        'image.jpg',
        'tank.bmp',
        'sniper.png',
        'bullet.tiff'
    ]
    for image_path in image_paths:
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Image '{image_path}' not found!")
            continue
        format_name = image_path.split('.')[-1].upper()
        cv2.imshow(f"Image as {format_name}", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
read_and_display_images()
