#include <LiquidCrystal.h>
#include <Servo.h>
#define trig 7
#define echo 8
Servo myservo;

int servopin=6;
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
pinMode(trig,OUTPUT);
pinMode(echo,INPUT);
lcd.begin(16,2);
lcd.print("Please Verify");
myservo.attach(servopin);
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
delay(1000);
if(distance<10)
{
lcd.setCursor(0, 1);
lcd.print("Welcome!");
myservo.write(90);
delay(1000);
}
else
{
lcd.setCursor(0, 1);
lcd.print("LOCKED!!");
myservo.write(0);
delay(1000);
}
}
