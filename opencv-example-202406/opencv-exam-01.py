# 이미지 읽기 
import cv2

print(cv2.__version__)

# 칼라이미지의 경우 색상 채널 순서는 BGR 거꿀로 읽어야된다. 
# 정지영상 읽기
imageFile = "./cv-images/lena.jpg"
img = cv2.imread(imageFile, 1) # 플래그 1은 칼라! 
img_gray = cv2.imread(imageFile, 0) # 플래그 0은 흑백!  




# 흑백으로 보인다. 
# print(img_gray.shape)


# 이미지 크기 색상 정보 
# print(img.shape)

# 칼라이미지의 경우 색상 채널 순선느 BGR 거꿀로 읽어야된다. 원래는 RGB 색상 이다. 
# print(img[100, 100])


# 넘파이 배열을 이미지로 변환하여 출력하기 
cv2.imshow('Lena color', img)
cv2.imshow('Lena grayscale', img_gray)
 
cv2.waitKey()
cv2.destroyAllWindows() 