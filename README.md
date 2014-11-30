arduino-facetracker
===================

This repo includes a Python script which uses OpenCV's [1] Cascade Classifer library [2] and Haar Cascades [3] to detect faces from a defined video input stream. The location of the face is used to determine how to adjust a physical webcam mounted on servos which are controlled by an Arduino. The Python/Arduino interfacing is handled using the 3rd party pySerial library [4].

-
[1] http://opencv.org/                        
[2] http://docs.opencv.org/modules/objdetect/doc/cascade_classification.html   
[3] http://docs.opencv.org/trunk/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html    
[4] http://pyserial.sourceforge.net/shortintro.html
