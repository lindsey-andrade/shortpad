from pyserial import serial
import time
from keydictionary import press, pressAndHold, release, typer, pressHoldRelease
from windowswitch import WindowMgr
from win32gui import GetWindowText, GetForegroundWindow

ser = serial.Serial()
ser.setPort('COM5')
ser.baudrate = 9600
ser.open() #gotta open the ser to flush it
ser.flushInput() #something about clearing the queue of stuff still in there

old = ser.readline()
oldstr = str(old)
# actual serial output comes out looking like b'0\r\n' so i only pull the 3 character
# could probably convert to an int but oh well
oldnum = oldstr[2]


while 1:
    try:
        new = ser.readline()
        if len(str(new)) == 8:
            newstr = str(new)
            newnum = newstr[2]
            if oldnum != newnum: # this is a string comparision. maybe ints are faster?

                #sets reference so it can actually switch
                oldnum = newnum
                
                if newnum == str(1): #has to both be a string or both an int
                    
                    thing = GetWindowText(GetForegroundWindow()) #only acts on active window
                    #don't try this code on the python source while it's running. it hates it
                    w = WindowMgr()
                    w.find_window_wildcard(thing)
                    w.set_foreground()

                    # all the text
                    typer('<3')
                    press('enter')
                    
                    #print(thing) # prints out the window it's typing in
                
    except ser.SerialTimeoutException:
        print('Data could not be read')
