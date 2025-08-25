import cv2
import numpy as np
import matplotlib.pyplot as plt


# قراءة صورة من الجهاز
path="3wd.jpg"
# read image
img=cv2.imread(path)
print(img.shape)
ss=img.shape
size1=ss[0]//2
size2=ss[1]//2
# print(type())


print(size1,size2)

# show image
# cv2.imshow("Lena Soderberg", img)


# resize=cv2.resize(img,(size1,size2))
# cv2.imshow("resize picture",resize)
# cv2.waitKey(0)


# # video
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture("vwda.mp4")#ينشى كائن لقراءة الفيديو من الملف
while True:
 success, vid = cap.read()#ينشى كائن الفيديو
 img = cv2.resize(vid, (frameWidth,frameHeight))#يغير حجم الاطار 
 cv2.imshow("Result", img)
 if cv2.waitKey(1) & 0xFF == ord('q'):
     break
cap.release()#يحرر كائن الفيديو
cv2.destroyAllWindows()#opncvيغلق جميع النوافذ المفتوحة من 


img = cv2.imread("3wd.jpg")  # قراءة الصورة
kernel = np.ones((4,4),np.uint8)  # Kernel مصفوفة صغيرة من القيم 1
imgG = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #  رمادي
imgBlur = cv2.GaussianBlur(imgG, (7,7), 0)  # ضبابية
imgCanny = cv2.Canny(img, 100, 200)  # حواف Canny
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)  # توسيع الحواف
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)  # تآكل الحواف

cv2.imshow("Original", img)#الاصلية
cv2.imshow("Gray", imgG)#رمادية
cv2.imshow("Blur", imgBlur)#زرقاء
cv2.imshow("Canny", imgCanny)#حواف
cv2.imshow("Dialation", imgDialation)#توسيع حواف
cv2.imshow("Eroded", imgEroded)#تاكل حواف
cv2.waitKey(0)#انتظار الضغط على زر