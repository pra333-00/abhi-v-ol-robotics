#define trig 9
#define echo 8
#define led 10

void setup() {
  
pinMode(trig,OUTPUT);
pinMode(echo,INPUT);
pinMode(led,OUTPUT);
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
  digitalWrite(led,LOW);
}
else if(distance<50)
{
  digitalWrite(led,HIGH);
}
}
