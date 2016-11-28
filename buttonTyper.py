from pyserial import serial
import time
from packages.keydictionary import press, pressAndHold, release, typer, pressHoldRelease
from packages.windowswitch import WindowMgr
from win32gui import GetWindowText, GetForegroundWindow

ser = serial.Serial()
ser.setPort('COM5')
ser.baudrate = 9600
ser.open() #gotta open the ser to flush it
ser.flushInput() #something about clearing the queue of stuff still in there

# initialize the button variables
button1Old = "0"
button2Old = "0"
button3Old = "0"

button1New = ""
button2New = ""
button3New = ""


while 1:
    try:
        new = str(ser.readline())

        if len(new) == 9: # sometimes serial outputs messed up strings. this filters it
            buttonNum = new[2];

            # Set button states to the correct button
            if buttonNum == "1":
                button1New = new[3]
            elif buttonNum == "2":
                button2New = new[3]
            else:
                button3New = new[3]

            # Button 1 pushed
            if button1Old != button1New:
                button1Old = button1New
                if button1New == "1":
                    print("Button 1 pushed")

                    ## Type in Window Code - START
                    full_window_name = GetWindowText(GetForegroundWindow()) #only acts on active window
                    #don't try this code on the python source while it's running. it hates it
                    window_title = full_window_name.split('-')[0]
                    wildcard = ".*" + window_title + ".*"
                    

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
                            #print(full_window_name)
                        except:                    
                            w = WindowMgr()
                            w.find_window_wildcard(wildcard)
                            w.set_foreground()
                            #print(wildcard)

                        # put key stroke actions here
                        typer("f")
                        
                    else:
                        print('Do not push the button in this window, dumb fuck')
                    ## Type in Window - END

                    
                    
            # Button 2 pushed
            if button2Old != button2New:
                button2Old = button2New
                if button2New == "1":
                    print("Button 2 pushed")

                    ## Type in Window Code - START
                    full_window_name = GetWindowText(GetForegroundWindow()) #only acts on active window
                    #don't try this code on the python source while it's running. it hates it
                    window_title = full_window_name.split('-')[0]
                    wildcard = ".*" + window_title + ".*"
                    

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
                            #print(full_window_name)
                        except:                    
                            w = WindowMgr()
                            w.find_window_wildcard(wildcard)
                            w.set_foreground()
                            #print(wildcard)

                        # put key stroke actions here
                        typer("n")
                        
                    else:
                        print('Do not push the button in this window, dumb fuck')
                    ## Type in Window - END

                        
            # Button 3 pushed
            if button3Old != button3New:
                button3Old = button3New
                if button3New == "1":
                    print("Button 3 pushed")

                    ## Type in Window Code - START
                    full_window_name = GetWindowText(GetForegroundWindow()) #only acts on active window
                    #don't try this code on the python source while it's running. it hates it
                    window_title = full_window_name.split('-')[0]
                    wildcard = ".*" + window_title + ".*"
                    

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
                            #print(full_window_name)
                        except:                    
                            w = WindowMgr()
                            w.find_window_wildcard(wildcard)
                            w.set_foreground()
                            #print(wildcard)

                        # put key stroke actions here
                        typer("m")
                        
                    else:
                        print('Do not push the button in this window, dumb fuck')
                    ## Type in Window - END
                
                        
            """
            if "Notepad" in full_window_name:
                typer('notepad')
                press('enter')
            elif "SOLIDWORKS" in full_window_name:
                press('f')
            else:
                typer('<3')
                press('enter')
            """
                    
                
    except ser.SerialTimeoutException:
        print('Data could not be read')
