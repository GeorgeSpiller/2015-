/*
  Conditionals - while statement

  This example demonstrates the use of  while() statements.

  While the pushbutton is pressed, the sketch runs the calibration routine.
  The sensor readings during the while loop define the minimum and maximum of
  expected values from the photoresistor.

  This is a variation on the calibrate example.

  The circuit:
  - photoresistor connected from +5V to analog in pin 0
  - 10 kilohm resistor connected from ground to analog in pin 0
  - LED connected from digital pin 9 to ground through 220 ohm resistor
  - pushbutton attached from pin 2 to +5V
  - 10 kilohm resistor attached from pin 2 to ground

  created 17 Jan 2009
  modified 30 Aug 2011
  by Tom Igoe
  modified 20 Jan 2017
  by Arturo Guadalupi

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/WhileLoop
*/

#include <Servo.h>
Servo Ser_10;
Servo Ser_11;
Servo Ser_12;




void setup() {
  Ser_10.attach(10);
  Ser_11.attach(11);
  Ser_12.attach(12);

  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
}

void loop() {

  delay(500);
  //bool comp;
  digitalWrite(7, HIGH);
  Ser_10.write(180);
  delay(1000);
  Ser_10.write(0);
  delay(1000);
  digitalWrite(7, LOW);



  //reset_all_servos();



  //  delay(500);
  //  comp = move_ser(7);
  //  delay(500);
  //  comp = move_ser(8);
  //  delay(500);
  //  comp = move_ser(9);

}

int move_ser(int sernum) {

  int activeposs = 180;
  reset_all_servos();

  if (sernum = 7) {
    digitalWrite(7, HIGH);
    digitalWrite(8, LOW);
    digitalWrite(9, LOW);
    Ser_10.write(activeposs);
  } else if (sernum = 8) {
    digitalWrite(7, LOW);
    digitalWrite(8, HIGH);
    digitalWrite(9, LOW);
    Ser_11.write(activeposs);
  } else if (sernum = 9) {
    digitalWrite(7, LOW);
    digitalWrite(8, HIGH);
    digitalWrite(9, LOW);
    Ser_12.write(activeposs);
  } else {
    Serial.println("Invalid Servo VCC pin number: ");
    Serial.print(sernum);
    return false;
  }

  reset_all_servos();
  return true;
}


void reset_all_servos() {
  int resetpos = 0;
  int delaytime = 1000;
  //Reset all servos to resetpos

  //Ser10, VCC:7
  digitalWrite(7, HIGH);
  Ser_10.write(resetpos);
  delay(delaytime);
  digitalWrite(7, LOW);

  //Ser11, VCC:8
  digitalWrite(8, HIGH);
  Ser_11.write(resetpos);
  delay(delaytime);
  digitalWrite(8, LOW);

  //Ser12, VCC:9
  digitalWrite(9, HIGH);
  Ser_12.write(resetpos);
  delay(delaytime);
  digitalWrite(9, LOW);

}











