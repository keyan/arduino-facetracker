arduino-facetracker
===================

This repo includes a Python script which uses OpenCV's [1] Cascade Classifer library [2] and Haar Cascades to detect faces from a defined video input stream. The location of the face is used to determine how to adjust a physical webcam mounted on servos which are controlled by an Arduino. The Python/Arduino interfacing is handled using the 3rd party pySerial library [3].

-
[1] http://opencv.org/                        
[2] http://docs.opencv.org/modules/objdetect/doc/cascade_classification.html   
[3] http://pyserial.sourceforge.net/shortintro.html
