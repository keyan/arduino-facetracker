"""
This script uses the OpenCV Haar Cascades to detect faces. Input is taken from a connected webcam and dected faces are overlayed.
Due to the preloaded classifier being used, only frontal face recognition is currently functional.

http://docs.opencv.org/trunk/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html
"""
import sys #for webcam access
import cv2 #openCV library
import serial #allows Arduino interfacing
import numpy
import time

def adjust_camera(x, y, w, h):
    nothing = 0
    mid_y = int(y + (h / 2.0))
    mid_x = int(x + (w / 2.0))
    
    if mid_y == half_height:
        nothing = 1
        print "nothing y"
    elif mid_y < (half_height) - 100:
        ser.write('u')
        print 'u'
    elif mid_y > (half_height) + 100:
        ser.write('d')
        print 'd'
    
    time.sleep(0.005)
    
    if mid_x == half_width:
        nothing = 1
        print "nothing x"
    elif mid_x < (half_width) - 100:
        ser.write('l')
        print 'l'
    elif mid_x > (half_width) + 100:
        ser.write('r')
        print 'r'
    
    print mid_y
    print mid_x
    print half_height
    print half_width
    time.sleep(0.005)
        
#cascadePath = sys.argv[0]
#the pre-trained classifier for facial detection (cannot detect profile view)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
video_stream = cv2.VideoCapture(0) #captures video from input 0, should be changed if external webcam is attached
ser = serial.Serial('/dev/cu.usbmodem411', 9600) #set up serial port to interface with Arduino
# video_stream.set(3, 700) #propID for the alias CV_CAP_PROP_FRAME_WIDTH
# video_stream.set(4, 400) #propID for the alias CV_CAP_PROP_FRAME_HEIGHT
sizew = video_stream.get(3) #propID for the alias CV_CAP_PROP_FRAME_WIDTH
sizeh = video_stream.get(4) #propID for the alias CV_CAP_PROP_FRAME_HEIGHT
half_height = int(sizeh / 2.0)
half_width = int(sizew / 2.0)

#continously take new frames and convert to grayscale, then
while True:
    #img = cv2.imread('image.jpeg') #image path, for static face detection
    ret, frame = video_stream.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert image to grayscale, simiplifies detection
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #detect face, scale adjustment allows detection of different size faces
    for (x, y, w, h) in faces: #draw rectangle around faces
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        print x, y #display xy coordinates of the center of the face, will be output to arduino
        adjust_camera(x, y, w, h)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()