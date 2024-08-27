const int IRSensor=4;
void setup() {
  pinMode(13,OUTPUT);
  pinMode(IRSensor,INPUT);

}

void loop() {
  if(digitalRead(IRSensor)==HIGH)
  {
    digitalWrite(13,LOW);
   
  }
  else
  {
    digitalWrite(13,HIGH);
  }
}  
