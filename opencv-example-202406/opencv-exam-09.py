# 관심잇는 부분 을 잘라낸다 .
import cv2

img = cv2.imread("./cv-images/lena.jpg", cv2.IMREAD_GRAYSCALE)
img[100, 200] = 0  # 특정 픽셀의 값을 0으로 지정 즉 검게 만듬 


print(img[100:110, 200:210]) 

# 특정 여역을 골라 전부 검게 만듬 
img[100:400, 200:300] = 0  # ROI 접근 region of interest 흥미의 영역 (ROI) 이 영상에서 이부분이 중요하다 또는 관심이 있다 라고 하는 부분 

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

img = cv2.imread("./cv-images/lena.jpg") # cv2.IMREAD_COLOR 
img[100, 200] = [255, 0, 0]  # 컬러(BGR) 변경
print(img[100, 200:210]) # ROI 접근

img[100:400, 200:300] = [255, 0, 0]  # ROI 접근 새 채널이다. 
    
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()