int S=13;
void setup() {
   pinMode(S,OUTPUT);
}

void loop() {
  digitalWrite(S,LOW);
  delay(100);
  digitalWrite(S,HIGH);
  delay(100);

}
