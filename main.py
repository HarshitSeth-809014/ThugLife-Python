import cv2
import numpy as np
from PIL import Image

mask_path = 'mask.png'
face_cascade_path = 'haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)
mask = Image.open(mask_path)

def thug_mask(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.5)
    background = Image.fromarray(image)

    for (x,y,w,h) in faces:
        resized_mask = mask.resize((w+40,h+40),Image.ANTIALIAS)
        offset = (x-25,y)
        background.paste(resized_mask,offset,mask = resized_mask)
    return np.asarray(background)

# 0 or 1 in function
cap = cv2.VideoCapture(0) 

while True:
    _,frame = cap.read()
    cv2.imshow("Thug Life Filter",thug_mask(frame))
    if cv2.waitKey(25) == ord('q'):
        break
        # press 'q' to exit the program

cap.release()
cv2.destroyAllWindows()