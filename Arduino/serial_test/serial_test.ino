#include <ESP8266WiFi.h>

int var = 0;
WiFiServer server(80);


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
    delay(10);

  Serial.println(WiFi.localIP());
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(var);
  digitalWrite(LED_BUILTIN, HIGH);   
  delay(1000);                       
  digitalWrite(LED_BUILTIN, LOW);    
  delay(2000);   
  var = var +1;
}
