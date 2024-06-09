import cv2
from matplotlib import pyplot as plt

# 이미지 파일 경로
imageFile = './data/lena.jpg'

# 이미지 파일을 BGR 형식으로 읽기 (OpenCV는 기본적으로 BGR 형식을 사용)
imgBGR = cv2.imread(imageFile)

# Matplotlib의 축을 숨기기
plt.axis('off')

# BGR 형식을 RGB 형식으로 변환
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

# Matplotlib를 사용하여 이미지를 표시
plt.imshow(imgRGB)
plt.show()
