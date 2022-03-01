from sre_constants import SUCCESS
import cv2
from pyzbar.pyzbar import decode
from pyzbar import pyzbar
from datetime import *


#Video Camera capture cuntion
def camera():
    #Capture settings 
    cap= cv2.VideoCapture(1)
    cap.set(3, 640)
    cap.set(4,480)
    #To stop repetition of decode result (it will only display a code once)
    usedCodes=[]
    camera=True
    #while loop for continuous video capture
    while camera ==True:
        success, frame =cap.read()
        
        #for loop for printing the code once
        for code in decode (frame):
            if code.data.decode('utf-8') not in usedCodes:
                print("Decoded!\n")
                print(code.type)
                print(code.data.decode('utf-8'))
                usedCodes.append(code.data.decode("utf-8"))
                #calling the function for decoding the QR scanned
                frame=QR_readnw(frame)
                break
       #to show camera on desktop
        cv2.imshow('Qr Scan Cam', frame)
        #press X to close Videocapture
        if cv2.waitKey(1) == ord('x'):
                break
    cap.release()            
    cv2.destroyAllWindows

def QR_readnw (frame):
    dQR = pyzbar.decode(frame) 
    accessTime = datetime.now()
    accessD = accessTime.strftime("%d %B, %Y") 
    accessH = accessTime.strftime("%I:%M %p") 
    for qrData in dQR:
        decodedQR = qrData.data.decode('utf-8')
        with open ("QR Text.txt", "w") as textfile: 
            textfile.write(f"Digital Signature: Accessed: {accessD} at {accessH}\n")
            textfile.write("\n"+decodedQR) 
            #message for letting u know decoding and encoding has been successful
            print("\nQR code has now been encoded in .txt file\nPress X to close window")
    return frame
    
camera()