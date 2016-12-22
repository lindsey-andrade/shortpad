  const int pin1 = 7; 
  const int pin2 = 8;
  const int pin3 = 9; 
  const int pin4 = 10; 
  const int pin5 = 11; 
  const int pin6 = 12; 
  const int pin7 = 19; 
  const int pin8 = 14; 
  const int pin9 = 15; 
  const int pin10 = 16;
  const int pin11 = 17; 
  const int pin12 = 18; 

  int state1 = 0; 
  int state2 = 0; 
  int state3 = 0;
  int state4 = 0;
  int state5 = 0;
  int state6 = 0;
  int state7 = 0;
  int state8 = 0;
  int state9 = 0;
  int state10 = 0;
  int state11 = 0;
  int state12 = 0;

  
  
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(pin1, INPUT); 
  pinMode(pin2, INPUT); 
  pinMode(pin3, INPUT); 
  pinMode(pin4, INPUT); 
  pinMode(pin5, INPUT); 
  pinMode(pin6, INPUT); 
  pinMode(pin7, INPUT); 
  pinMode(pin8, INPUT); 
  pinMode(pin9, INPUT); 
  pinMode(pin10, INPUT); 
  pinMode(pin11, INPUT); 
  pinMode(pin12, INPUT); 
}

void loop() {
  // put your main code here, to run repeatedly:
  state1 = digitalRead(pin1); 
  state2 = digitalRead(pin2); 
  state3 = digitalRead(pin3); 
  state4 = digitalRead(pin4); 
  state5 = digitalRead(pin5); 
  state6 = digitalRead(pin6); 
  state7 = digitalRead(pin7); 
  state8 = digitalRead(pin8); 
  state9 = digitalRead(pin9); 
  state10 = digitalRead(pin10); 
  state11 = digitalRead(pin11); 
  state12 = digitalRead(pin12);
 

  Serial.print("01");
  Serial.println(state1); 
  Serial.print("02");
  Serial.println(state2); 
  Serial.print("03");
  Serial.println(state3); 
  Serial.print("04");
  Serial.println(state4); 
  Serial.print("05");
  Serial.println(state5); 
  Serial.print("06");
  Serial.println(state6); 
  Serial.print("07");
  Serial.println(state7); 
  Serial.print("08");
  Serial.println(state8); 
  Serial.print("09");
  Serial.println(state9); 
  Serial.print("10");
  Serial.println(state10); 
  Serial.print("11");
  Serial.println(state11); 
  Serial.print("12");
  Serial.println(state12); 
  
  /*
  if (state10 == HIGH) {     
    // turn LED on:    
    digitalWrite(ledPin, LOW); 
  } 
  else {
    digitalWrite(ledPin, HIGH);
  }
  */

}
