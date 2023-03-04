#define tri 9
#define echo 10
float duration,distance;
void setup() {
  Serial.begin(9600);
  pinMode(tri,OUTPUT);
  pinMode(echo,INPUT);
}

void loop() {
  digitalWrite(tri,LOW);
  delayMicroseconds(2);
  digitalWrite(tri,HIGH);
  delayMicroseconds(10);
  digitalWrite(tri,LOW);

  duration = pulseIn(echo,HIGH);
  distance =(duration/2)*0.0343;

  Serial.print("Distance=");
  if (distance >= 400 || distance <=2) {
    Serial.println("Out of range");
  }
  else {
    Serial.print(distance);
    Serial.println(" cm");
    delay(500);
  }
  delay(500);
}
