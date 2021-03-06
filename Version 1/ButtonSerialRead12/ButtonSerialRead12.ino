  // Assign button pins to I/O pins on the board for easy use later. There are 12 buttons. 
  // Could I have picked better naming for these constants? Yes. 
  const int pin1 = 9; 
  const int pin2 = 8;
  const int pin3 = 7; 
  const int pin4 = 10; 
  const int pin5 = 11; 
  const int pin6 = 12; 
  const int pin9 = 19; // the I/O pin 13 is connected to the LED on the Teensy so skip that
  const int pin8 = 14; 
  const int pin7 = 15; 
  const int pin10 = 16;
  const int pin11 = 17; 
  const int pin12 = 18; 

  // Reserve some I/O pins for LEDs just incase we want some later... 
  // Currently no LEDs are attached to the Arduino ¯\_(ツ)_/¯
  const int led1 = 20; 
  const int led2 = 21; 
  const int led3 = 22;

  // Set all the initial states of the buttons to 0 - this is the non-pushed state of the button. 
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
  // Start up the Serial! We're going to use that to talk to Python
  Serial.begin(9600);

  // Set all the button pins to INPUTS. 
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

  // Set all the LED pins to OUTPUTS. 
  pinMode(led1, OUTPUT); 
  pinMode(led2, OUTPUT); 
  pinMode(led3, OUTPUT);
}

void loop() {
  // This is the code that will loop forever:

  // Read the states of each button. "1" is pushed, "0" is not pushed. 
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
 
  // Print out the button number and its state. This will be read by Python via pyserial. 
  // Notice the "print" and "println" commands. This is so the button name and state print on the same line. 
  // For example, this prints "011" if the first button is pressed down.
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
  

  if (Serial.available() > 0){
    char data = Serial.read();
    if (data == 1) {
      digitalWrite(led3, LOW);
      digitalWrite(led1, LOW);
    } else if (data == 2) {
      digitalWrite(led1, HIGH);
      digitalWrite(led3, LOW);
    } else {
      digitalWrite(led1, LOW);
      digitalWrite(led3, HIGH);
    }
  }


}
