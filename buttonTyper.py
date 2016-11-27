from pyserial import serial
import time
#from packages import keydictionary
#from packages import windowswitch
#above stuff not working
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
                    
                    full_window_name = GetWindowText(GetForegroundWindow()) #only acts on active window
                    #don't try this code on the python source while it's running. it hates it
                    #print(full_window_name) # prints out the window it's typing in
                    window_title = full_window_name.split('-')[0]
                    wildcard = ".*" + window_title + ".*"
                    print(wildcard)

                    # this if loop is to make it not possible to type in the Python Shell
                    if full_window_name != "*Python 3.4.3 Shell*":
                        """
                        the following try/except is to get around a weird error when 
                  	switching between multiple window. some full window names would 
                  	not work when put into set_foreground() but some would. either
                  	it uses the full name of a window (ie "Messenger - Google Chrome")
                  	or it uses just the first part (ie "Messenger ") to call the window
                  	forward. it tries the full name first and if that doesn't work it'll
                  	try the shortened name. unsure why it does this and unsure if this is
                  	the best solution. 
                        """
                        try:
                            w = WindowMgr()
                            w.find_window_wildcard(full_window_name)
                            w.set_foreground()
                        except:                    
                            w = WindowMgr()
                            w.find_window_wildcard(wildcard)
                            w.set_foreground()

                        # all the text
                        if "Notepad" in full_window_name:
                            typer('notepad')
                            press('enter')
                        elif "SOLIDWORKS" in full_window_name:
                            press('f')
                        else:
                            typer('<3')
                            press('enter')
                    else:
                        print('Do not push the button in this window, dumb fuck')
                        

                    
                
    except ser.SerialTimeoutException:
        print('Data could not be read')
