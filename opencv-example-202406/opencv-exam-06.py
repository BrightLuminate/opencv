# 원그리기 타원 그리기
import cv2
import numpy as np

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255


# 원 그리기 센터 shape (512,512,3)  위에 shape 숫자 바꿔보기 
cy =img.shape[0]//2 # 높이에서 중간
cx = img.shape[1]//2 # 너비에서 중간 

# 200 하고 0 => 100 하나씩 그린거 
for r in range(200, 0, -100):
    cv2.circle(img, (cx,cy), r, color=(255,0,0))
cv2.circle(img, (cx,cy), radius=50, color=(0,0,255), thickness=-1)


# 타원 그리기 
ptCenter = cx, cy
size = 200, 100

# 큰 타원 
# 인수 순서 : 대상이미지, 타원중점, (긴거 200 , 짧은거 100), 각도 0 , 시각각도 0 , 끝각도 360(타원 0부터 360도 끝는다), 파란색
cv2.ellipse(img, ptCenter, size, 0, 0, 360, (255,0,0))
# 인수 순서 : 대상이미지, 타원중점, (긴거 200 , 짧은거 100), 각도 45 , 시각각도 0 , 끝각도 360(타원 0부터 360도 끝는다), 빨간색 
cv2.ellipse(img, ptCenter, size, 45, 0, 360, (0, 0, 255))

# 작은 타원 
# 중점 , 크기 , 각도를 튜플로 묶어서 한번에 전달하면 작원 타원  (큰타원 200 100 작은타원 으로 바꾼다. 그안에 사각형을 포함되는 작은 타원 )
box = (ptCenter, size, 0)
cv2.ellipse(img, box, (255, 0, 0), 5)

box = (ptCenter, size, 45)
cv2.ellipse(img, box, (0, 0, 255), 5)






cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()