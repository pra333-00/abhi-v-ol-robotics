#define led 13
#define IRSensor 4
void setup() {
  pinMode(led,OUTPUT);
  pinMode(IRSensor,INPUT);

}

void loop() {
  if(digitalRead(IRSensor)==HIGH)
  {
    digitalWrite(13,HIGH);
   
  }
  else
  {
    digitalWrite(13,LOW);
  }
} 
