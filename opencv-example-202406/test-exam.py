import cv2


dog1File = "./cv-images/puppy-1207816_640.jpg"
dog2File = "./cv-images/dog-6680642_640.jpg"


# ROI 검출하기 
cat  = cv2.imread(dog1File) 
dog  = cv2.imread(dog2File) 

y_term = 100
x_term = 100
y_cat_org = 50
x_cat_org = 240
y_dog_org = 600
x_dog_org = 1000

compose  = dog.copy()
compose[y_dog_org:y_dog_org+y_term, x_dog_org:x_dog_org+x_term] = \
cat[y_cat_org:y_cat_org+y_term, x_cat_org:x_cat_org+x_term]

cv2.imshow('compose',compose)

cv2.waitKey()
cv2.destroyAllWindows()