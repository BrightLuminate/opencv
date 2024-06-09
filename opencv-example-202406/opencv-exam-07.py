# 문자열 출력 
import numpy as np
import cv2


img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
text = 'OpenCV NO-Jam'
org = (50, 100) # 텍스트 시작점 
font = cv2.FONT_HERSHEY_SIMPLEX # 제공되는 글꼴
# 대상이미지 , 내용, 위치, 글꼴, 폰트크기, 색상, 두께
cv2.putText(img,text, org, font, 1, (255,0,0), 2)

# 내용과 글꼴 폰트크기와 두께를 줘서 텍스트 크기 새로 계산 baseLine 글자를 밑줄 길이
size, baseLine = cv2.getTextSize(text, font, 1, 2)
# 사이즈 org, (org[0]+size[0], org[1]-size[1]) 글리겠다 네모칸 치고 
cv2.rectangle(img, org, (org[0]+size[0], org[1]-size[1]), (0, 0, 255))
cv2.circle(img, org, 3, (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
