import cv2
import numpy as np

# Path to the image file
imageFile = './data/lena.jpg'

# Read the image in color mode
img = cv2.imread(imageFile, cv2.IMREAD_COLOR)

# Read the same image in grayscale mode
img2 = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)

# Read the image file as a byte array using numpy
encode_img = np.fromfile(imageFile, np.uint8)

# Decode the byte array to get the image
img = cv2.imdecode(encode_img, cv2.IMREAD_UNCHANGED)

# Display the color image
cv2.imshow('Lena color', img)

# Display the grayscale image
cv2.imshow('Lena grayscale', img2)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Destroy all OpenCV windows
cv2.destroyAllWindows()
