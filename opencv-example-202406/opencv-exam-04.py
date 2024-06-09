# 직선 (line) 및 사각형(rectangle) 그리기 
import cv2
import numpy as np

# 하얀 화면 만들기 3가지 똑같다.  zeros 0으로 채워진 배열  나머지 + 255 전체 픽셀 하양게 되서   
img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255 
# 1배열 더한다. 
# img = np.ones((512,512,3), np.uint8) * 255
# 풀 더한다 .
# img = np.full((512,512,3), (255, 255, 255), dtype= np.uint8)


pt1 = 100, 100
pt2 = 400, 400

# 인수 순서 : 대상이미지, 좌상단, 우하단, 색상, 두께
cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)

# 인수 순서 : 대상이미지 , 시작점, 끝점 , 색상 , 두께

# x축 y축 파란색 두께는 5
cv2.line(img, (0,0), (500, 0 ), (255, 0, 0), 5)

# x축 y축 빨간색 두께는 5
cv2.line(img, (0,0), (0, 500), (0,0,244), 5)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyWindow()