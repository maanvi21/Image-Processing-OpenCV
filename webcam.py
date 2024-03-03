import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame.")
        break
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break
cap.release()
cv2.destroyAllWindows()


    # Wait for a key event for 1 millisecond
    #key = cv2.waitKey(1)

    # Check if the 'ESC' key is pressed (ASCII code 27)
    #if key == 27:
       # break
