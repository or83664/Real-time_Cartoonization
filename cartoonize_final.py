import cv2

cap = cv2.VideoCapture(0)
while(True):
  ret, frame = cap.read()

  num_bilateral = 10   #定义双边滤波的数目
  #用高斯金字塔降低取样
  img_color = frame
  
  #重复使用小的双边滤波代替一个大的滤波
  for _ in range(num_bilateral):
      img_color = cv2.bilateralFilter(img_color,d=11,sigmaColor=8,sigmaSpace=9)

  #转换为灰度并且使其产生中等的模糊
  img_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
  img_blur = cv2.medianBlur(img_gray, 11)

  #检测到边缘
  imgCanny = cv2.Canny(frame, 100, 200)
  th1 = cv2.bitwise_not(imgCanny)
  
  #转换回彩色图像
  img_edge = cv2.cvtColor(th1, cv2.COLOR_GRAY2RGB)
  img_cartoon = cv2.bitwise_and(img_color, img_edge)

  cv2.imshow('edge', img_edge)
  cv2.imshow('cartoon', img_cartoon)

  k = cv2.waitKey(30) & 0xff
  if k == 27: break

cap.release()
cv2.destroyAllWindows()

