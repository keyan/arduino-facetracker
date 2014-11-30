#include <Servo.h>

Servo pan;
Servo tilt;

void setup() {
  tilt.attach(3); //tilt servo attached to pin 3
  pan.attach(4); // pan servo attached to pin 4
  tilt.write(70); //set intial position of tilt servo to 70
  pan.write(65); //set initial position of pan servo to 65
  Serial.begin(9600); //Serial port which will have recieved chars from Python
  pinMode(13, OUTPUT);
}

void loop(){
  short pos; //hold position of servo
  
  digitalWrite(13, HIGH); //random LED for coolness factor
  
  switch (Serial.read()){
   case 'u':
   case 'k':
     pos = tilt.read();
     if (pos > 0) tilt.write(pos - 5);
     break;
   case 'd':
   case 'j':
     pos = tilt.read();
     if (pos < 180) tilt.write(pos + 5);
     break;
   case 'l':
     pos = pan.read();
     if (pos > 0) pan.write(pos - 5);
     break;
   case 'r':
   case 'h':
     pos = pan.read();
     if (pos < 180) pan.write(pos + 5);
     break;
  }
  
  delay(300);
}
