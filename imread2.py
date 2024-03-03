import cv2
image=cv2.imread(r'C:\Users\maanv\Desktop\opencv\fcritlogo.png')
cv2.imwrite(r'fcritttLogo.png',image) 
cv2.imshow('2ndtry Try',image)
cv2.waitKey(10000)

cv2.destroyAllWindows()