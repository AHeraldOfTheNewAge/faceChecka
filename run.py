#https://www.digitalocean.com/community/tutorials/how-to-detect-and-extra
#just watch that sheet above, learn some
#https://towardsdatascience.com/object-detection-with-tensorflow-model-and-opencv-d839f3e42849

import cv2
import sys

imagePath = sys.argv[1]#run the script with arguments..

print(imagePath+"imagine")

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#blue,green,red to gray?

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
)

print("Found {0} Faces!".format(len(faces)))


for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    roi_color = image[y:y + h, x:x + w]
    print("[INFO] Object found. Saving locally.")
    cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color)
    
status = cv2.imwrite('faces_detected.jpg', image)


print ("Image faces_detected.jpg written to filesystem: ",status)
