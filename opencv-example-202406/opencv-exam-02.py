# 이미지 저장 
import cv2


# 칼라이미지의 경우 색상 채널 순서는 BGR 거꿀로 읽어야된다. 
# 정지영상 읽기 
imageFile = "./cv-images/lena.jpg"
img = cv2.imread(imageFile)


#배열을 실제 이미지 파일로 저장하기
cv2.imwrite("./cv-images/Lena.bmp", img)
cv2.imwrite("./cv-images/Lena.png", img)
cv2.imwrite("./cv-images/Lena2.png", img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite("./cv-images/Lena2.jpg", img,[cv2.IMWRITE_JPEG_QUALITY,90])
