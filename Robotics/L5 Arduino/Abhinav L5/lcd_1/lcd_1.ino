#include<LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2); 
#include<LiquidCrystal.h>
const int rs = 13 ,en = 12 ,d4 = 8,d5 = 9, d6 = 10 , d7 =11;
LiquidCrystal lcd (rs,en,d4,d5,d6,d7);  
const int sensor=A1;
float tempc;
float tempf;
float vout;

void setup()
{
pinMode(sensor,INPUT);
Serial.begin(9600);
lcd.begin(16,2);
delay(500);
}

void loop() 
{
vout=analogRead(sensor);
vout=(vout*500)/1023;
tempc=vout; // Storing value in Degree Celsius
tempf=(vout*1.8)+32; // Converting to Fahrenheit 
lcd.setCursor(0,0);
lcd.print("in DegreeC= ");
lcd.print(tempc);
lcd.setCursor(0,1);
lcd.print("in Fahrenheit=");
lcd.print(tempf);
delay(1000); //Delay of 1 second for ease of viewing in serial monitor
}
