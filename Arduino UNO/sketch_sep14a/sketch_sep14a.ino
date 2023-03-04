int R= 11;
int Y= 12;
int B= 13;
void setup()
{
  pinMode(R,OUTPUT);
  pinMode(Y,OUTPUT);
  pinMode(B,OUTPUT);
}

void loop()
{
  digitalWrite(R,HIGH);
  digitalWrite(Y,LOW);
  digitalWrite(B,LOW);
  delay(10000);
  digitalWrite(R,LOW);
  digitalWrite(Y,HIGH);
  digitalWrite(B,LOW);
  delay(10000);
  digitalWrite(R,LOW);
  digitalWrite(Y,LOW);
  digitalWrite(B,HIGH);
  delay(10000);
}
