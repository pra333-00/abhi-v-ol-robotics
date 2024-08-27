#include<Servo.h>
Servo myservo1;
Servo myservo2;
int servopin1=3;
int servopin2=4;
int val=0;
int potpin1=0;
int potpin2=0;
void setup() {
myservo1.attach(servopin1);
myservo2.attach(servopin2);
Serial.print(val);
}

void loop() {
val=analogRead(potpin1);
val=analogRead(potpin2);
val=map(val,0,1023,0,180);
myservo1.write(val);
myservo2.write(val);

}
