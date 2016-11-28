/*
  Button
 
 Turns on and off a light emitting diode(LED) connected to digital  
 pin 13, when pressing a pushbutton attached to pin 2. 
 
 
 The circuit:
 * LED attached from pin 13 to ground 
 * pushbutton attached to pin 2 from +5V
 * 10K resistor attached to pin 2 from ground
 
 * Note: on most Arduinos there is already an LED on the board
 attached to pin 13.
 
 
 created 2005
 by DojoDave <http://www.0j0.org>
 modified 30 Aug 2011
 by Tom Igoe
 
 This example code is in the public domain.
 
 http://www.arduino.cc/en/Tutorial/Button
 */

// constants won't change. They're used here to 
// set pin numbers:
const int buttonPin1 = 15;     // the number of the pushbutton pin
const int buttonPin2 = 16;
const int buttonPin3 = 17;
const int ledPin =  13;      // the number of the LED pin
  // Pin 13: Arduino has an LED connected on pin 13
  // Pin 11: Teensy 2.0 has the LED on pin 11
  // Pin  6: Teensy++ 2.0 has the LED on pin 6
  // Pin 13: Teensy 3.0 has the LED on pin 13

// variables will changeys
int buttonState1 = 0;         // variable for reading the pushbutton status
int buttonState2 = 0;
int buttonState3 = 0;
String outputString1 = "";
String outputString2 = "";
String outputString3 = "";

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);      
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin1, INPUT);  
  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin3, INPUT);   
  Serial.begin(9600);


}

void loop(){
  // read the state of the pushbutton value:
  buttonState1 = digitalRead(buttonPin1);
  buttonState2 = digitalRead(buttonPin2);
  buttonState3 = digitalRead(buttonPin3);

  Serial.print("1");
  Serial.println(buttonState1);
  Serial.print("2");
  Serial.println(buttonState2);
  Serial.print("3");
  Serial.println(buttonState3);

  // check if the pushbutton is pressed.
  // if it is, the buttonState is HIGH:
  if (buttonState3 == HIGH) {     
    // turn LED on:    
    digitalWrite(ledPin, HIGH);  
  } 
  else {
    // turn LED off:
    digitalWrite(ledPin, LOW); 
  }
}
