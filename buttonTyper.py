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
button1Old = 1
button2Old = 1
button3Old = 1
button4Old = 1
button5Old = 1
button6Old = 1
button7Old = 1
button8Old = 1
button9Old = 1
button10Old = 1
button11Old = 1
button12Old = 1

button1New = None
button2New = None
button3New = None
button4New = None
button5New = None
button6New = None
button7New = None
button8New = None
button9New = None
button10New = None
button11New = None
button12New = None


def sendToActiveWindow():
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
                
        else:
                print('Do not push the button in this window, dumb fuck')
        ## Type in Window - END

        return full_window_name
        
while 1:
        try:
                new = str(ser.readline())
                

                if len(new) == 10: # sometimes serial outputs messed up strings. this filters it
                        buttonNum = int(new[2:4]);
                        state = int(new[4])
                        

                        # Set button states to the correct button
                        if buttonNum == 1:
                                button1New = state
                        elif buttonNum == 2:
                                button2New = state
                        elif buttonNum == 3:
                                button3New = state
                        elif buttonNum == 4:
                                button4New = state
                        elif buttonNum == 5:
                                button5New = state
                        elif buttonNum == 6:
                                button6New = state
                        elif buttonNum == 7:
                                button7New = state
                        elif buttonNum == 8:
                                button8New = state
                        elif buttonNum == 9:
                                button9New = state
                        elif buttonNum == 10:
                                button10New = state
                        elif buttonNum == 11:
                                button11New = state
                        elif buttonNum == 12:
                                button12New = state
                        else:
                                print('???')

                        # Button 1 pushed
                        if button1Old != button1New:
                                button1Old = button1New
                                if button1New == 0:
                                        print("Button 1 pushed")

                                        windowName = sendToActiveWindow()
                                        
                                        # put key strokes here
                                        typer('button 1')
                                        press('enter')
                                        
                                
                        # Button 2 pushed
                        if button2Old != button2New:
                                button2Old = button2New
                                if button2New == 0:
                                        print("Button 2 pushed")

                                        windowName = sendToActiveWindow()
                                        
                                        # put key strokes here
                                        typer('button 2')
                                        press('enter')

                                                
                        # Button 3 pushed
                        if button3Old != button3New:
                                button3Old = button3New
                                if button3New == 0:
                                        print("Button 3 pushed")

                                        windowName = sendToActiveWindow()
                                        
                                        # put key strokes here
                                        typer('button 3')
                                        press('enter')

                        # Button 4 pushed
                        if button4Old != button4New:
                                button4Old = button4New
                                if button4New == 0:
                                        print("Button 4 pushed")

                                        windowName = sendToActiveWindow()
                                        
                                        # put key strokes here
                                        typer('button 4')
                                        press('enter')

                        # Button 5 pushed
                        if button5Old != button5New:
                                button5Old = button5New
                                if button5New == 0:
                                        print("Button 5 pushed")

                                        windowName = sendToActiveWindow()
                                        
                                        # put key strokes here
                                        typer('button 5')
                                        press('enter')

                        # Button 6 pushed
                        if button6Old != button6New:
                                button6Old = button6New
                                if button6New == 0:
                                        print("Button 6 pushed")

                                        windowName = sendToActiveWindow()
                                        
                                        # put key strokes here
                                        typer('button 6')
                                        press('enter')

                        # Button 7 pushed
                        if button7Old != button7New:
                                button7Old = button7New
                                if button7New == 0:
                                        print("Button 7 pushed")

                                        windowName = sendToActiveWindow()
                                        
                                        # put key strokes here
                                        typer('button 7')
                                        press('enter')

                        # Button 8 pushed
                        if button8Old != button8New:
                                button8Old = button8New
                                if button8New == 0:
                                        print("Button 8 pushed")

                                        windowName = sendToActiveWindow()
                                        
                                        # put key strokes here
                                        typer('button 8')
                                        press('enter')

                        # Button 9 pushed
                        if button9Old != button9New:
                                button9Old = button9New
                                if button9New == 0:
                                        print("Button 9 pushed")

                                        windowName = sendToActiveWindow()
                                        
                                        # put key strokes here
                                        typer('button 9')
                                        press('enter')

                        # Button 10 pushed
                        if button10Old != button10New:
                                button10Old = button10New
                                if button10New == 0:
                                        print("Button 10 pushed")

                                        windowName = sendToActiveWindow()
                                        
                                        # put key strokes here
                                        typer('button 10')
                                        press('enter')

                        # Button 11 pushed
                        if button11Old != button11New:
                                button11Old = button11New
                                if button11New == 0:
                                        print("Button 11 pushed")

                                        windowName = sendToActiveWindow()
                                        
                                        # put key strokes here
                                        typer('button 11')
                                        press('enter')

                        # Button 12 pushed
                        if button12Old != button12New:
                                button12Old = button12New
                                if button12New == 0:
                                        print("Button 12 pushed")

                                        windowName = sendToActiveWindow()
                                        
                                        # put key strokes here
                                        typer('button 12')
                                        press('enter')
                        
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
