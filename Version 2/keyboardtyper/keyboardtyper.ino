#include "Keyboard.h"
#include "HID.h"
void setup() {
  // put your setup code here, to run once:
}

void loop() {
  // put your main code here, to run repeatedly:
    delay(5000);
    Keyboard.write('A');
}
