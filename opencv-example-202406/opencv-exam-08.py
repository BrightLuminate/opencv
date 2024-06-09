import cv2
import numpy as np

img = cv2.imread("./cv-images/lena.jpg") # cv2.IMREAD_COLOR

print('img.ndim=', img.ndim)
print('img.shape=', img.shape)
print('img.dtype=', img.dtype)

## np.bool, np.uint16, np.uint32, np.float32, np.float64, np.complex64
img = img.astype(np.int32)
print('img.dtype=',img.dtype)

img= np.uint8(img)
print('img.dtype=',img.dtype)

print('img.shape=', img.shape)

img = img.flatten()
print('img.shape=', img.shape)

img = img.reshape(-1, 512, 512) 
print('img.shape=', img.shape)

cv2.imshow('img', img[0])
cv2.waitKey()
cv2.destroyAllWindows()