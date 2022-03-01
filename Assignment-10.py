from sre_constants import SUCCESS
import cv2
from cv2 import imshow
from pyzbar.pyzbar import decode

cap=cv2.VideoCapture(0)
cap.set(3,640) 
cap.set(4,480)
camera=True
while camera==True:
    success, frame = cap.read()

    for code in decode(frame):
        print(code.type)
        print(code.data.decode)('utf-8')
    
    cv2.imshow('QR Camera', frame)
    if cv2.waitKey(1)==ord('x'):
        cap.release()
        cv2.destroyAllWindows()



