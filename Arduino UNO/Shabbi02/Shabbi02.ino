int R=2;
int Y=3;
int G=4;

void setup() {
  pinMode(R,OUTPUT);
  pinMode(Y,INPUT);

}

void loop() {
  digitalWrite(R,HIGH);
  digitalWrite(Y,LOW);
  digitalWrite(G,LOW);
  delay(100);

  digitalWrite(R,LOW);
  digitalWrite(Y,HIGH);
  digitalWrite(G,LOW);
  delay(100);

  
  digitalWrite(R,LOW);
  digitalWrite(Y,LOW);
  digitalWrite(G,HIGH);
  delay(100);
  
  
}
