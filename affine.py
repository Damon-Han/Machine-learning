import cv2
import numpy as np


dog = cv2.imread('/Users/binh/Desktop/MYOPENCV/韩斌护照.jpeg')
print(dog.shape)
h,w,ch = dog.shape

##矩阵的平移
##首先确定平移变换矩阵
##M = np.float32([[1, 0, 100],[0, 1, 100]])

##获取变换矩阵
#getRotationMatrix2D(中心点,旋转角度,缩放大小)

##旋转角度为逆时针
#M = cv2.getRotationMatrix2D((w/2,h/2),15,0.3)
#print(M)

##M = cv2.getAffineTransform(src,dst),通过三点确定变换的位置.
src = np.float32([[400,300],[800,300],[400,600]])
dst = np.float32([[200,400],[600,500],[150,650]])
M = cv2.getAffineTransform(src,dst)
new = cv2.warpAffine(dog,M,(w,h))
print(new.shape)
cv2.imshow('new', new)
cv2.waitKey(0)


