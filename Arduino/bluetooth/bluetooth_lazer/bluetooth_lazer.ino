int ledred=8;
int tx=1;
int rx=0;
int i = 0;
int a = 0;
char inSerial[1];

void setup(){
  Serial.begin(9600);
  pinMode(ledred, OUTPUT);
  pinMode(tx, OUTPUT);
  pinMode(rx, INPUT);
}

void loop(){
    delay(1000);                                         
    if (Serial.available() > 0) {
       while (Serial.available() > 0) {
         inSerial[a]=Serial.read(); 
         a++;      
       }
       inSerial[a]='\0'; 
      if (i = 0) {
        i = 1;
        }
      if (i = 1){
          i = 0;
          }; 
    Serial.println(i);
      if (i = 1){
        digitalWrite(ledred, HIGH);
        } else {
        digitalWrite(ledred, LOW);
        };
     }} 
     








  
