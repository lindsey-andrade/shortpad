from pyserial import serial
import time
ser = serial.Serial()
ser.setPort('COM5')
ser.baudrate = 9600
ser.open() #gotta open the ser to flush it
ser.flushInput() #something about clearing the queue of stuff still in there

button1Old = "1"
button2Old = "1"
button3Old = "1"

button1New = ""
button2New = ""
button3New = ""

while 1:
    try:
        new = str(ser.readline())
        print(new)
        
        if len(new) == 10:
            buttonNum = new[3];
            
            if buttonNum == "1":
                button1New = new[4]
            elif buttonNum == "2":
                button2New = new[4]
            else:
                button3New = new[4]

            if button1Old != button1New:
                button1Old = button1New
                if button1New == "1":
                    print("Button 1 pushed")

            if button2Old != button2New:
                button2Old = button2New
                if button2New == "1":
                    print("Button 2 pushed")

            if button3Old != button3New:
                button3Old = button3New
                if button3New == "1":
                    print("Button 3 pushed")

        
    except ser.SerialTimeoutException:
        print('Data could not be read')
