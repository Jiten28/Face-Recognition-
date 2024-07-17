import cv2

cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)

imgBackground = cv2.imread('Resources\background.png')

while True:
    success, img = cap.read()
    
    cv2.imshow("Face Detection", img)
    cv2.waitKey(1)