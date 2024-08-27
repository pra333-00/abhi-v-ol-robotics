#include<Servo.h>
int servopin=3;
int pos=0;
Servo myservo;
void setup()
{

myservo.attach(servopin);
}

void loop()
{

for(pos=0;pos<180;pos++)
{
  myservo.write(pos);
  delay(5);
}
for(pos=180;pos>0;pos--)
{
  myservo.write(pos);
 delay(5);
}

}
