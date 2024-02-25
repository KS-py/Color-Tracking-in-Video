import numpy as np
import time
import cv2
import argparse 

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="Path to the (optional) video", required=True)
ap.add_argument("-c", "--color", help="Color for the threshold", required=True)
args = vars(ap.parse_args())

picked_color = args["color"]
FLAG = True

#create the thresholds for the color we want to identify
if picked_color == "blue":
    lower = np.array([100, 67, 0], dtype="uint8")
    upper = np.array([255, 128, 50], dtype="uint8")
elif picked_color == "yellow":
    lower = np.array([0, 128, 139], dtype="uint8")
    upper = np.array([0, 255, 255], dtype="uint8")    
elif picked_color == "red":
    lower = np.array([0, 0, 139], dtype="uint8")
    upper = np.array([43, 75, 238], dtype="uint8")
elif picked_color == "green":
    lower = np.array([32, 50, 1], dtype="uint8")
    upper = np.array([0, 255, 170], dtype="uint8")    
else:
    print("Please the threshold color is not available, please provide one of the following: red, yellow, blue, green")
    FLAG = False
    
camera = cv2.VideoCapture(args["video"])

while FLAG:
    (grabbed, frame) = camera.read()

    if not grabbed:
        break

    #We do a Gaussian Blur to emphasize the contours
    blur = cv2.inRange(frame, lower,upper)
    blur = cv2.GaussianBlur(blur, (3, 3), 0)

    
    (cnts, _) = cv2.findContours(blur.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts) > 0:
        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
        cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)

    cv2.imshow("Tracking", frame)
    cv2.imshow("Binary", blur)

    time.sleep(0.05)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        

camera.release()
cv2.destroyAllWindows()
