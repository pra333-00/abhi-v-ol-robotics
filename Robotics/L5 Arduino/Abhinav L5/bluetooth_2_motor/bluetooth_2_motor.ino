void setup() {
  Serial.begin(9600);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);

}

void loop() {
  unsigned char data= 0;
  if (Serial.available ()>0);
  {
    data= Serial.read();
    Serial.print(data);
    Serial.println();
    delay(1000);
    if(data==70)
    {
    digitalWrite(8,HIGH);
    digitalWrite(9,HIGH);
    }
    if else(data==76)
    {
    digitalWrite(8,LOW);
    digitalWrite(9,HIGH);
    }
     if(data==82)
    {
    digitalWrite(8,HIGH);
    digitalWrite(9,LOW);
    }
    else(data==66)
    {
    digitalWrite(8,LOW);
    digitalWrite(9,LOW);
  }

}
}
