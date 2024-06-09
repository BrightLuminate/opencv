# 색깔 변경 
import cv2
import matplotlib.pyplot as plt



# 칼라이미지의 경우 색상 채널 순서는 BGR 거꿀로 읽어야된다.  255,0 128 B G R 로 R G B 바뀐다.
# 정지영상 읽기
imageFile = "./cv-images/lena.jpg"
imgBGR = cv2.imread(imageFile) # 기본값
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB) # 색상 변환 시그널을 주면 cv2.COLOR_BGR2RGB 
imgGRAY = cv2.imread(imageFile, 0)

fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(9,6))
ax1.axis("off")
ax2.axis("off")

# 색상 변환 시그널  R G B 거꾸로 
ax1.imshow(imgRGB)
# 기본값
# ax1.imshow(imgBGR)
ax2.imshow(imgGRAY, cmap='gray', interpolation='bicubic')

plt.show()