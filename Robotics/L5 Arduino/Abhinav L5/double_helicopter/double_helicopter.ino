#include<Servo.h>
int servopin1=3;
int servopin2=4;
int pos=0;
Servo myservo1;
Servo myservo2;
void setup()
{

myservo1.attach(servopin1);
myservo2.attach(servopin2);
}

void loop()
{

for(pos=0;pos<=180;pos+10)
{
  myservo1.write(pos);
  myservo2.write(pos);
  delay(15);
}
for(pos=180;pos>=0;pos-10)
{
  myservo1.write(pos);
  myservo2.write(pos);
  delay(15);
}

}
