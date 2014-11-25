import sys
import cv2

#cascadePath = sys.argv[0]
#the pre-trained classifier for facial detection (cannot detect profile view)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

video_stream = cv2.VideoCapture(0) #captures video from input 0, should be changed if external webcam is attached

#continously take new frames and convert to grayscale, then
while True:
    #img = cv2.imread('image.jpeg') #image path, for static face detection
    ret, frame = video_stream.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert image to grayscale, simiplifies detection
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #detect face, scale adjustment allows detection of different size faces
    for (x, y, w, h) in faces: #draw rectangle around faces
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        print x, y #display xy coordinates of the center of the face, will be output to arduino
    
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
