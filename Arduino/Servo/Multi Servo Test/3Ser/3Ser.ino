#include <Servo.h>

Servo Ser_10;
Servo Ser_11;
Servo Ser_12;

void setup() {
  Ser_10.attach(10);
  Ser_11.attach(11);
  Ser_12.attach(12);
}


void loop() {
int activeposs = 180;

delay(500);
Ser_10.write(activeposs);
delay(500);
Ser_10.write(0);
delay(500);
Ser_11.write(activeposs);
delay(500);
Ser_11.write(0);
delay(500);
Ser_12.write(activeposs);
delay(500);
Ser_12.write(0);




  
//  reset_all_servos();
//  Ser_10.write(activeposs);
//  reset_all_servos();
//  Ser_11.write(activeposs);
//  reset_all_servos();
//  Ser_12.write(activeposs);
  
}


void reset_all_servos() {
  int resetpos = 0;
  int delaytime = 500;
  //Reset all servos to resetpos

  //Ser10
  Ser_10.write(resetpos);
  delay(delaytime);

  //Ser11
  Ser_11.write(resetpos);
  delay(delaytime);

  //Ser12
  Ser_12.write(resetpos);
  delay(delaytime);

}











