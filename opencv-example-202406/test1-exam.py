import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the images
img1 = cv2.imread("./cv-images/puppy-1207816_640.jpg")
img2 = cv2.imread("./cv-images/dog-6680642_640.jpg")

# Define the ROI parameters in the first image
x1 = 250
y1 = 50
width = 200
height = 200

# Extract the ROI from the first image
cropped_image = img1[y1:y1+height, x1:x1+width]

# Define the top-left corner where the cropped image will be placed in the second image
x2 = 100
y2 = 100

# Get the dimensions of the second image
img2_height, img2_width, _ = img2.shape

# Ensure the ROI fits within the second image
if x2 + width > img2_width or y2 + height > img2_height:
    raise ValueError("The cropped image does not fit within the target image at the specified location.")

# Create a copy of the second image to avoid modifying the original
composite_image = img2.copy()

# Place the cropped image at the specified location in the second image
composite_image[y2:y2+height, x2:x2+width] = cropped_image

# Display the composite image using OpenCV
cv2.imshow('Composite Image', composite_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Alternatively, display the composite image using matplotlib
composite_image_rgb = cv2.cvtColor(composite_image, cv2.COLOR_BGR2RGB)
plt.imshow(composite_image_rgb)
plt.axis('off')  # Hide the axes
plt.show()
