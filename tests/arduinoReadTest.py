from pyserial import serial
import time
ser = serial.Serial()
ser.setPort('COM5')
ser.baudrate = 9600
ser.open() #gotta open the ser to flush it
ser.flushInput() #something about clearing the queue of stuff still in there

button1Old = "0"
button2Old = "0"
button3Old = "0"

button1New = ""
button2New = ""
button3New = ""

while 1:
    try:
        new = str(ser.readline())

        if len(new) == 9:
            buttonNum = new[2];
            
            if buttonNum == "1":
                button1New = new[3]
            elif buttonNum == "2":
                button2New = new[3]
            else:
                button3New = new[3]

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
            
        
        
        """
        if len(str(new)) == 8:
            newstr = str(new)
            newnum = newstr[2]
            if oldnum != newnum:
                oldnum = newnum
                print(newnum)
        """
    except ser.SerialTimeoutException:
        print('Data could not be read')
