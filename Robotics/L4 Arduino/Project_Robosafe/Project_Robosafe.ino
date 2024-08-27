#define IRSensorRight 5
#define IRSensorLeft 6
#define trig 7
#define echo 8
#define rightled 9
#define leftled 10
#define rightbuzzer 11
#define leftbuzzer 12

void setup() {

pinMode(4,OUTPUT);
pinMode(IRSensorRight,INPUT);
pinMode(IRSensorLeft,INPUT);
pinMode(trig,OUTPUT);
pinMode(echo,INPUT);
pinMode(rightled,OUTPUT);
pinMode(leftled,OUTPUT);
pinMode(rightbuzzer,OUTPUT);
pinMode(leftbuzzer,OUTPUT);
Serial.begin(9600);
}
void loop() {

long duration,distance;
digitalWrite(trig,HIGH);
delay(1000);
digitalWrite(trig,LOW);
duration=pulseIn(echo,HIGH);
distance=duration/58.2;
Serial.print("Distance:");             
Serial.println(distance);
delay(1);
if(distance>50)
{
  digitalWrite(rightled,LOW);
  digitalWrite(leftled,LOW);
  digitalWrite(rightbuzzer,LOW);
  digitalWrite(leftbuzzer,LOW);
}
else
{
digitalWrite(rightled,HIGH);
digitalWrite(rightbuzzer,HIGH);
delay(2000);
digitalWrite(rightled,LOW);
digitalWrite(rightbuzzer,LOW);
delay(1000);
digitalWrite(leftled,HIGH);
digitalWrite(leftbuzzer,HIGH);
delay(2000);
digitalWrite(leftled,LOW);
digitalWrite(leftbuzzer,LOW);
delay(1000); 
}
if(digitalRead(IRSensorLeft)==HIGH)
{
digitalWrite(rightled,HIGH);
digitalWrite(rightbuzzer,HIGH);
delay(2000);
digitalWrite(rightled,LOW);
digitalWrite(rightbuzzer,LOW);
delay(1000);
digitalWrite(leftled,HIGH);
digitalWrite(leftbuzzer,HIGH);
delay(2000);
digitalWrite(leftled,LOW);
digitalWrite(leftbuzzer,LOW);
delay(1000);  
}
else
{
  digitalWrite(rightled,LOW);
  digitalWrite(leftled,LOW);
  digitalWrite(rightbuzzer,LOW);
  digitalWrite(leftbuzzer,LOW);  
}
if(digitalRead(IRSensorRight)==HIGH)
{
digitalWrite(rightled,HIGH);
digitalWrite(rightbuzzer,HIGH);
delay(2000);
digitalWrite(rightled,LOW);
digitalWrite(rightbuzzer,LOW);
delay(1000);
digitalWrite(leftled,HIGH);
digitalWrite(leftbuzzer,HIGH);
delay(2000);
digitalWrite(leftled,LOW);
digitalWrite(leftbuzzer,LOW);
delay(1000);  
}
else
{
  digitalWrite(rightled,LOW);
  digitalWrite(leftled,LOW);
  digitalWrite(rightbuzzer,LOW);
  digitalWrite(leftbuzzer,LOW);  
}
}
