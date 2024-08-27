#include <Servo.h>
int servopin = 3;
Servo servo1;
void setup() {
servo1.attach(servopin);
}
void loop() {
servo1.write(0);
delay(1000);
servo1.write(90);
delay(1000);
servo1.write(180);
delay(1000);
}
