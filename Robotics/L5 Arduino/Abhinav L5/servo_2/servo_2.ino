#include <Servo.h>
int servopin1 = 3;
int servopin2 = 4;
Servo servo1;
Servo servo2;
void setup() {
servo1.attach(servopin1);
servo2.attach(servopin2);
}
void loop() {
servo1.write(0);
servo2.write(0);
delay(500);
servo1.write(90);
servo2.write(90);
delay(500);
servo1.write(180);
servo2.write(180);
delay(500);
}
