import cv2
image=cv2.imread(r'C:\Users\maanv\Desktop\opencv\fcritlogo.png')
rect=(400,400,400,250)
color=(0,0,0)
thickness=2
cv2.rectangle(image,(rect[0],rect[1],rect[2],rect[3]),color,thickness)
cv2.imwrite(r'C:\Users\maanv\Desktop\opencv\fcritlogo.png',image)
cv2.imshow('1st Try',image)
cv2.waitKey()
cv2.destroyAllWindows()