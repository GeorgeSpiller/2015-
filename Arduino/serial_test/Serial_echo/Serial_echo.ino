String serialData;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  Serial.println(serialData);
  delay(500);
}


void serialEvent() {
  serialData = Serial.readString();
}


