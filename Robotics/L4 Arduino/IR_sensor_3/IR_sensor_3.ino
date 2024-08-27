const int analogInPin = A0;  
int sensorValue = 0;        
#define pin1 8
#define pin2 9
#define pin3 10
#define pin4 11
#define led 13


void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
  pinMode(pin3, OUTPUT);
  pinMode(pin4, OUTPUT);
}

void loop() {
  sensorValue = analogRead(analogInPin);
  Serial.print("\nsensor = ");
  Serial.print(sensorValue);
  if(sensorValue < 100){ 
    digitalWrite(13, HIGH);
    Serial.print("\nObject Detected");
    digitalWrite(pin1,HIGH);
    digitalWrite(pin2,LOW); 
    digitalWrite(pin3,HIGH); 
    digitalWrite(pin4,LOW);
    
    }
  else{
    digitalWrite(13, LOW);
    Serial.print("\nNo object in Front");
    digitalWrite(pin1,LOW);
    digitalWrite(pin2,LOW); 
    digitalWrite(pin3,LOW); 
    digitalWrite(pin4,LOW);
    
    }
  delay(500);
} 
