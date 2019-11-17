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

// These variables will change:
int Min = 0;  // minimum sensor value
int Max = 180;     // maximum sensor value
int val = 0;         // the sensor value

#include <Servo.h>
Servo myservo;  // create servo object to control a servo

void setup() {
myservo.attach(9);
}

void loop() {
  while (val != Max) {
  myservo.write(val);
  val = val + 1;
  delay(15);
  }
  while (val != Min) {
  myservo.write(val);
  val = val - 1;
  delay(15);
  }
}















