# This script uses the OpenCV Haar Cascades to detect faces. Input is taken
# from a connected webcam and dected faces are overlayed. Due to the preloaded
# classifier being used, only frontal face recognition is currently functional.
#
#
# The location of faces is output to an Arduino, which uses servos to adjust
# webcam position in order to center the face in the window.
#
# Author: Keyan Pishdadian

import sys
import cv2
import serial
import numpy
import time


class FaceFinder(object):

    def __init__(self):
        # Set up the serial connection to interface with the Arduino.
        self.arudino = serial.Serial('/dev/cu.usbmodem411', 9600)
        self.face_cascade = cv2.CascadeClassifier(
            'haarcascade_frontalface_alt.xml'
        )
        self.video_stream = cv2.VideoCapture(0)

        # Uses the propID for the alias CV_CAP_PROP_FRAME_HEIGHT/WIDTH
        self.half_height = int(self.video_stream.get(4) / 2.0)
        self.half_width = int(self.video_stream.get(3) / 2.0)

    def adjust_camera(self, x, y, w, h):
        """
        Takes as parameters the xy and height width position of the detected
        face, finds where the middle of the window is and directs Arduino to
        move to the middle.

        A delay is used so that the servos don't overshoot the midpoint and go
        into an overcompensation loop. This is also the reason why the
        midpoint is allowed to be within +- 125 pixels.
        """
        half_height = self.half_height
        half_width = self.half_width

        mid_y = int(y + (h / 2.0))
        mid_x = int(x + (w / 2.0))

        if mid_y == half_height:
            pass
        elif mid_y < (half_height) - 125:
            self.signal_arduino('u')
        elif mid_y > (half_height) + 125:
            self.signal_arduino('d')

        time.sleep(0.005)

        if mid_x == half_width:
            pass
        elif mid_x < (half_width) - 125:
            self.signal_arduino('l')
        elif mid_x > (half_width) + 125:
            self.signal_arduino('r')

        print "Current Face height is:", mid_y
        print "Current Face width is:", mid_x
        time.sleep(0.005)

    def signal_arudino(self, command):
        """
        Sends a character over serial port to the Arduino to direct it towards
        the middle of the frame.

        u: move up
        d: move down
        l: move left
        r: move right
        """
        self.arduino.write(command)
        print command

    def loop(self):
        while True:
            ret, frame = self.video_stream.read()
            # Converting the captured frame to grayscale simplifies detection.
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                print "Current Face XY location is:", x, y
                self.adjust_camera(x, y, w, h)
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                #self.end_stream()
                break

    def end_stream(self):
        self.video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    f = FaceFinder()
    f.loop()