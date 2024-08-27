float temp;
void setup() {
  pinMode(8,OUTPUT);
  Serial.begin(9600);
}

void loop() 
{
  temp=analogRead(A2);
  temp=temp*0.48828125;
  Serial.print("temp ");
  Serial.print(temp);
  Serial.print("c");
  Serial.println();
  delay(1000);
  if (temp>30)
  {digitalWrite(8,HIGH);
  }
  else
  {digitalWrite(8,LOW);
  }
}
