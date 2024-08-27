#define pin1   4
#define pin2   5
#define pin3   6
#define pin4   7
#define led left 8
#define led right 9

void setup()
{
  pinMode(pin1,OUTPUT);
  pinMode(pin2,OUTPUT);
  pinMode(pin3,OUTPUT);
  pinMode(pin4,OUTPUT);
  pinMode(led left,OUTPUT);
  pinMode(led right,OUTPUT);
}
void loop()
{
// FORWARD
if digitalWrite(pin1,HIGH);
   digitalWrite(pin2,LOW);
   digitalWrite(pin3,HIGH);
   digitalWrite(pin4,LOW);
   delay(1000);
{
  digitalWrite(led left,HIGH);
  digitalWrite(led right,HIGH);
}
else if

// BACKWARD
digitalWrite(pin1,LOW);
digitalWrite(pin2,HIGH);
digitalWrite(pin3,LOW);
digitalWrite(pin4,HIGH);
delay(1000);
{ 
  digitalWrite(led left,LOW);
  digitalWrite(led right,LOW);
}
  

// LEFT OR RIGHT
if digitalWrite(pin1,HIGH);
   digitalWrite( pin2,LOW);
   digitalWrite(pin3 ,LOW);
   digitalWrite(pin4,LOW);
   delay(1000);
   {
    digitalWrite(led left,HIGH);
    digitalWrite(led right,LOW);
   }
else if 

// LEFT OR RIGHT
digitalWrite(pin1 ,LOW);
digitalWrite(pin2, LOW);
digitalWrite(pin3 , HIGH);
digitalWrite(pin4, LOW);
delay(1000);
   {
    digitalWrite(led left,LOW);
    digitalWrite(led right,HIGH);
   }

} 
