#include <Servo.h>

Servo pan;
Servo tilt;

void setup() {
  tilt.attach(3);
  pan.attach(4);
  tilt.write(70);
  pan.write(65);
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop(){
  short pos;
  
  digitalWrite(13, HIGH);
  
  switch (Serial.read()){
   case 'u':
   case 'k':
     pos = tilt.read();
     if (pos > 0) tilt.write(pos - 8);
     break;
   case 'd':
   case 'j':
     pos = tilt.read();
     if (pos < 180) tilt.write(pos + 8);
     break;
   case 'l':
     pos = pan.read();
     if (pos > 0) pan.write(pos - 8);
     break;
   case 'r':
   case 'h':
     pos = pan.read();
     if (pos < 180) pan.write(pos + 8);
     break;
  }
  
  delay(300);
}
