int LED = 13 ;
int SensPin = 7;
void setup() {
  pinMode(LED,OUTPUT);
  pinMode(SensPin,INPUT);

}

void loop() {
  int value  = digitalRead(SensPin);
  if (value == 1)
  {
    digitalWrite(LED,HIGH);
  }
  else
  {
    digitalWrite(LED,LOW);
  }
  delay(300);
}
