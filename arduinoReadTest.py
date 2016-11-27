from pyserial import serial
import time
ser = serial.Serial()
ser.setPort('COM5')
ser.baudrate = 9600
ser.open() #gotta open the ser to flush it
ser.flushInput() #something about clearing the queue of stuff still in there

old = ser.readline()
oldstr = str(old)
oldnum = oldstr[2]

while 1:
    try:
        new = ser.readline()
        if len(str(new)) == 8:
            newstr = str(new)
            newnum = newstr[2]
            if oldnum != newnum:
                oldnum = newnum
                print(newnum)
    except ser.SerialTimeoutException:
        print('Data could not be read')
