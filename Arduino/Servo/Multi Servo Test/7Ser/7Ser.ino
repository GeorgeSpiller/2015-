#include <Servo.h>
#define PRINTLN(var) Serial.print(#var ": "); Serial.println(var)

Servo Ser_1;
Servo Ser_2;
Servo Ser_3;
Servo Ser_4;
Servo Ser_5;
Servo Ser_6;
Servo Ser_7;
int activeposs = 90;
int delaytime = 995;
int INactiveposs = 10;
int buttonPin = 10;

int buttonState = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("starting...");
  Ser_1.attach(2);
  Ser_2.attach(3);
  Ser_3.attach(4);
  Ser_4.attach(5);
  Ser_5.attach(6);
  Ser_6.attach(7);
  Ser_7.attach(8);
  //test_servos();
  pinMode(buttonPin, INPUT);
}

void loop() {
  test_servos();

  //test_servos();
  //buttonState = digitalRead(buttonPin);
  //PRINTLN(buttonState);
  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  // if (buttonState == HIGH) {
  //
  //    bool comp = false;
  //    comp = displaynumber(0);
  //    delay(delaytime);
  //    comp = displaynumber(1);
  //    delay(delaytime);
  //    comp = displaynumber(2);
  //    delay(delaytime);
  //    comp = displaynumber(3);
  //    delay(delaytime);
  //    comp = displaynumber(4);
  //    delay(delaytime);
  //    comp = displaynumber(5);
  //    delay(delaytime);
  //    comp = displaynumber(6);
  //    delay(delaytime);
  //    comp = displaynumber(7);
  //    delay(delaytime);
  //    comp = displaynumber(8);
  //    delay(delaytime);
  //    comp = displaynumber(9);
  //    delay(delaytime);
  //
  //    Serial.println("itteration done, next itteration");
  //    delay(1000);

  //  } else {
  //  }
}

/*
      a       ,      1
    ----      ,    ----
  f| g  |b    ,  6| 7  |2
    ----      ,    ----
  e|  d |c    ,  5|  4 |3
    ----      ,    ----
  zero = (1,2,3,4,5,6)
  one = (2,3)
  two = (1,2,7,5,4)
  three = (1,2,7,3,4)
  four = (6,7,2,3)
  five = (1,6,7,3,4)
  six = (1,6,7,5,4,3)
  seven = (1,2,3)
  eight = (1,2,3,4,5,6,7)
  nine = (1,2,7,6,3)
*/


int displaynumber(int input_integer) {

  PRINTLN(input_integer);

  if (input_integer == 0) {
    //zero = (1,2,3,4,5,6)
    setServo(Ser_1); setServo(Ser_2); setServo(Ser_3); setServo(Ser_4); setServo(Ser_5); setServo(Ser_6); REsetServo(Ser_7);
  } else if (input_integer == 1) {
    //one = (2,3)
    setServo(Ser_2); setServo(Ser_3); REsetServo(Ser_1); REsetServo(Ser_4); REsetServo(Ser_5); REsetServo(Ser_6); REsetServo(Ser_7);
  } else if (input_integer == 2) {
    // two = (1,2,7,5,4)
    setServo(Ser_1); setServo(Ser_2); setServo(Ser_7); setServo(Ser_5); setServo(Ser_4); REsetServo(Ser_3); REsetServo(Ser_6);
  } else if (input_integer == 3) {
    // three = (1,2,7,3,4)
    setServo(Ser_1); setServo(Ser_2); setServo(Ser_7); setServo(Ser_3); setServo(Ser_4); REsetServo(Ser_5); REsetServo(Ser_6);
  } else if (input_integer == 4) {
    //four = (6,7,2,3)
    setServo(Ser_6); setServo(Ser_7); setServo(Ser_2); setServo(Ser_3); REsetServo(Ser_1); REsetServo(Ser_4); REsetServo(Ser_5);
  } else if (input_integer == 5) {
    //five = (1,6,7,3,4)
    setServo(Ser_1); setServo(Ser_6); setServo(Ser_7); setServo(Ser_3); setServo(Ser_4); REsetServo(Ser_2); REsetServo(Ser_5);
  } else if (input_integer == 6) {
    //six = (1,6,7,5,4,3)
    setServo(Ser_1); setServo(Ser_6); setServo(Ser_7); setServo(Ser_5); setServo(Ser_4); setServo(Ser_3); REsetServo(Ser_2);
  } else if (input_integer == 7) {
    // seven = (1,2,3)
    setServo(Ser_1); setServo(Ser_2); setServo(Ser_3); REsetServo(Ser_4); REsetServo(Ser_5); REsetServo(Ser_6); REsetServo(Ser_7);
  } else if (input_integer == 8) {
    //eight = (1,2,3,4,5,6,7)
    setServo(Ser_1); setServo(Ser_2); setServo(Ser_3); setServo(Ser_4); setServo(Ser_5); setServo(Ser_6); setServo(Ser_7);
  } else if (input_integer == 9) {
    // nine = (1,2,7,6,3)
    setServo(Ser_1); setServo(Ser_2); setServo(Ser_7); setServo(Ser_6); setServo(Ser_3); REsetServo(Ser_4); REsetServo(Ser_5);
  } else {
    Serial.println("Error decoding int to print: ");
    return false;
  }//end of if - int decoder
  return true;
}//end of function

void setServo(Servo S) {
  int Servo_poss = S.read();
  PRINTLN(Servo_poss);
  if (Servo_poss > 10) {
  } else {
    S.write(activeposs);
  }
}

void REsetServo(Servo S) {
  S.write(INactiveposs);
}


void test_servos() {
  //  int activeposs = 180;
  //  int delaytime = 500;
  Serial.println("Test Servos, begin");
  delay(delaytime);
  Ser_1.write(INactiveposs);
  Ser_2.write(INactiveposs);
  Ser_3.write(INactiveposs);
  Ser_4.write(INactiveposs);
  Ser_5.write(INactiveposs);
  Ser_6.write(INactiveposs);
  Ser_7.write(INactiveposs);
  Serial.println("Servo 1");

  Ser_1.write(activeposs);
  delay(delaytime);
  Ser_1.write(INactiveposs);
  delay(delaytime);
  Serial.println("Servo 2");

  Ser_2.write(activeposs);
  delay(delaytime);
  Ser_2.write(INactiveposs);
  delay(delaytime);
  Serial.println("Servo 3");

  Ser_3.write(activeposs);
  delay(delaytime);
  Ser_3.write(INactiveposs);
  delay(delaytime);
  Serial.println("Servo 4");

  Ser_4.write(activeposs);
  delay(delaytime);
  Ser_4.write(INactiveposs);
  delay(delaytime);
  Serial.println("Servo 5");

  Ser_5.write(activeposs);
  delay(delaytime);
  Ser_5.write(INactiveposs);
  delay(delaytime);
  Serial.println("Servo 6");

  Ser_6.write(activeposs);
  delay(delaytime);
  Ser_6.write(INactiveposs);
  delay(delaytime);
  Serial.println("Servo 7");

  Ser_7.write(activeposs);
  delay(delaytime);
  Ser_7.write(INactiveposs);
  

  Serial.println("Test finished");
}










