# This script uses the OpenCV Haar Cascades to detect faces. Input is taken from a connected webcam and dected faces are overlayed.
# Due to the preloaded classifier being used, only frontal face recognition is currently functional.
#
# http://docs.opencv.org/trunk/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html
#
# The location of faces is output to an Arduino, which uses servos to adjust webcam position in order to center the face in
# the window.

import sys #for webcam access
import cv2 #openCV library
import serial #allows Arduino interfacing
import numpy
import time #for delays

def adjust_camera(x, y, w, h):
    """
    Takes as parameters the xy and height width position of the detected face, finds where the middle of the window is and sends
    characters to the Arduino which direct it to:
    u: move up
    d: move down
    l: move left
    r: move right

    A delay is used so that the servos don't overshoot the midpoint and go into an overcompensation loop. This is also the reason
    why the midpoint is allowed to be within +- 125 pixels.
    """
    nothing = 0
    mid_y = int(y + (h / 2.0))
    mid_x = int(x + (w / 2.0))
    
    if mid_y == half_height:
        nothing = 1
    elif mid_y < (half_height) - 125: #if the current location of the face is more than 125 pixels away from the center
        ser.write('u')
        print 'u'
    elif mid_y > (half_height) + 125: #if the current location of the face is more than 125 pixels away from the center
        ser.write('d')
        print 'd'
    
    time.sleep(0.005)
    
    if mid_x == half_width:
        nothing = 1
    elif mid_x < (half_width) - 125: #if the current location of the face is more than 125 pixels away from the center
        ser.write('l')
        print 'l'
    elif mid_x > (half_width) + 125: #if the current location of the face is more than 125 pixels away from the center
        ser.write('r')
        print 'r'
    
    print "Current Face height is:", mid_y
    print "Current Face width is:", mid_x
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
half_height = int(sizeh / 2.0) #determine window midpoint
half_width = int(sizew / 2.0) #determine window midpoint, used for the adjust_camera method

#continously take new frames and convert to grayscale, then
while True:
    #img = cv2.imread('image.jpeg') #image path, for static face detection
    ret, frame = video_stream.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert image to grayscale, simiplifies detection
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #detect face, scale adjustment allows detection of different size faces
    for (x, y, w, h) in faces: #draw rectangle around faces
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        print "Current Face XY location is:", x, y #display xy coordinates of the center of the face
        adjust_camera(x, y, w, h) #adjust webcam location based on current face position
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #time.sleep(0.005)

video_capture.release()
cv2.destroyAllWindows()