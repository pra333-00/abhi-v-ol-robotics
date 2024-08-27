#include<Servo.h>
Servo myservo;
int servopin=3;
int val=0;
int potpin=0;
void setup() {
myservo.attach(servopin);

}

void loop() {
val=analogRead(potpin);
val=map(val,0,1023,0,180);
myservo.write(val);

}
