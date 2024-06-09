''''
막간 테스트 ! 

1. 512  * 512 하얀 도화지 이미지를 만든다.
2. 100, 100 좌상단에 400, 400 우하단 빨간 네모를 그린다.
3. 120, 50 부터 300, 500 까지 이어지는 파란 직선을 그린다. 

'''

import cv2
import numpy as np

# 하얀 화면 만들기 3가지 똑같다.
img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255

# x 가로 y 세로 

x1, x2 = 100, 400
y1, y2 = 100, 400

cv2.rectangle(img, (x1,y1), (x2,y2), (0, 0, 255 ))

pt1 = 120, 50
pt2 = 300, 500

cv2.line(img, pt1, pt2, (255,0,0),2)

# 사각형과 직선 교차점 표시하기 :clipLine 사각형의 내 꼭지점 (x1, y1, x2-x1, y2-y1)
imgRect =  (x1, y1, x2-x1, y2-y1) # 시작점과 각 거리 

# retval : 교차점 여부
# rpt1, rpt2 : 각 교차점들 circle 원으로 표시한다. radius=5, 
retval, rpt1, rpt2 = cv2.clipLine(imgRect, pt1, pt2)
if retval:
    # 두께 -1 은 원 채우기 이다. 
    cv2.circle(img, rpt1, radius=5,
               color=(0, 255, 0), thickness=-1)
    cv2.circle(img, rpt2, radius=5,
               color=(0,255,0), thickness=-1)


cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
