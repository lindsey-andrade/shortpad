from pyserial import serial
import time
from packages.keydictionary import press, pressAndHold, release, typer, pressHoldRelease
from packages.windowswitch import WindowMgr
from win32gui import GetWindowText, GetForegroundWindow
import struct
from tkinter import *

textFile = None

textFile = open("ProgramCommands.txt", 'r')
commands = [line.split() for line in textFile]

class Box(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Simple")
        self.pack(fill = BOTH, expand = 1)

"""
modButtonPush function flips the modifier keys on and off. Modifier keys change the functions of the keys
so all keys can have 4 functions (modifier key states of [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]). Only
one modifier key can be active at a time or shit just gets too confusing. Could potentially make more keys
active at once and get even more combonations but that seems excessive. So for now modButtonPush toggles the
pressed key and sets the others to zero.

The "ProgramCommands.txt" now can take in more commands. Button numbers can be from 4-12, 24-32, 34-42, 44-52.
The buttonPush function has been modified to read the modkey states and add 20, 30, or 40 to the number of the
button pushed. This means you don't need an extra column in the text file and it's less searching. 
"""
def modButtonPush(old, new, primary_modkeystate, second_modkeystate1, button_num, gui):
        if old != new:
                old = new
                if new == 0: # button pushed down
                        # flip the sate of modkeystate
                        primary_modkeystate = abs(primary_modkeystate - 1)
                        if primary_modkeystate == 1: # if you're turning a key on ...
                                # ... turn off the other two
                                second_modkeystate1 = 0
                        if button_num == 1:
                                modkeyA = primary_modkeystate
                                modkeyB = second_modkeystate1
                        elif button_num == 2:
                                modkeyB = primary_modkeystate
                                modkeyA = second_modkeystate1

                        if [modkeyA, modkeyB] == [0, 0]:
                                ser.write(struct.pack('>B', 1))
                        elif [modkeyA, modkeyB] == [1, 0]:
                                ser.write(struct.pack('>B', 2))
                        elif [modkeyA, modkeyB] == [0, 1]:
                                ser.write(struct.pack('>B', 3))

        return old, new, primary_modkeystate, second_modkeystate1

"""
buttonPush function takes in old and new button states and the button number and pulls the correct
key command for the active window. Key commands are kept in a text file called "ProgramCommands.txt"
in the same folder as this file.

By total chance, if a program doesn't have defined key commands and a button is pushed in that program
nothing happens because the temp_array of commands is empty. ¯\_(?)_/¯
"""
def buttonPush(old, new, button_num, modkeyA, modkeyB, modkeyC):
        temp_array = []
        newline = [0, 0, 0]

        if old != new:
                old = new
                if new == 0:

                        #print(modkeyA, modkeyB, modkeyC)
                        
                        activeWindowName = sendToActiveWindow()
                        # create a temporary array with only the commands for the active window
                        for line in commands:
                                # pull out the program to test against the active window
                                program = line[1].replace("\'", "")
                                program = str(program.replace(",", ""))
                                
                                if program in activeWindowName:
                                        # pull out the button and keys from the lines
                                        # the correct program
                                        button = int(line[0].replace(",", ""))

                                        key = line[2].replace("\'", "")
                                        
                                        # create a temporary array to store only the commands
                                        # for the active window
                                        temp_array.append([button, program, key])
                                        
                        if modkeyA == 1:
                                button_num = button_num + 20
                        elif modkeyB == 1:
                                button_num = button_num + 40
                                        
                        for line in temp_array:
                                if line[0] == button_num:
                                        key = line[2]
                                        if '+' in key:
                                                keys = key.split('+')
                                                pressHoldRelease(keys[0], keys[1])
                                                print(button_num, key)
                                        elif key == 'esc': #lol it tries to type "esc"
                                                press('esc')
                                        elif key == 'del':
                                                press('del')
                                        else:
                                                typer(key)
                        

        return old, new
                                  
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
                        print(full_window_name)
                except:                    
                        w = WindowMgr()
                        w.find_window_wildcard(wildcard)
                        w.set_foreground()
                        print(wildcard)
                
        else:
                print('Do not push the button in this window')
        ## Type in Window - END

        return full_window_name

def activeWindowName():
    full_window_name = GetWindowText(GetForegroundWindow())
    return full_window_name


if __name__ == "__main__":

    # Gui Set up
    root = Tk()
    root.geometry("250x150+300+300")
    app = Box(root)

    v = StringVar()
    Label(root, textvariable = v).pack()
    w = Label(root, text = "hello, world!")
    w.pack()
    root.update_idletasks()
    root.update()
    ###
    
    ser = serial.Serial()
    ser.setPort('COM5')
    ser.baudrate = 9600
    ser.open() #gotta open the ser to flush it
    ser.flushInput() #something about clearing the queue of stuff still in there
    ser.flushOutput()

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

    count = 1


    modkeyA = 0
    modkeyB = 0
    modkeyC = 0
    
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

                            """ Old comments - not accurate anymore, just ignore
                            Modifier keys: Button 1, Button 2, Button 3
                            
                            These keys will pressAndHold on the down and then release
                            on the up.

                            They need the elif buttonXNew == 1 statement because they
                            will trigger a release if it's just an else statement since
                            the starting value of the new states are None. They only
                            trigger the accidental release on the first and second
                            loop of the overall while loop. The elif statement only
                            gets rid of one accidental release. The counter gets rid
                            of the second one. Since something is up with the serial
                            flush, the button logic has to be delayed until the second
                            read-through. No idea why. The counter plus the elif seem
                            to fix the issue.

                            Having the program always release the modifier keys might
                            be a good thing to have incase the program is stopped before
                            the release is done. Although if that happens then we might
                            have bigger issues. 
                            """
                            """
                            # Button 1 pushed (Modifier key 1)
                            if button1Old != button1New:
                                    button1Old = button1New
                                    if button1New == 0:
                                            print("Button 1 pushed")

                                            sendToActiveWindow()
                                            
                                            # put key strokes here
                                            pressAndHold('shift')
                                    elif button1New == 1:
                                            print("Button 1 released")
                                            release('shift')
                                            
                          
                            # Button 2 pushed (Modifier key 2)
                            if button2Old != button2New:
                                    button2Old = button2New
                                    if button2New == 0:
                                            print("Button 2 pushed")

                                            windowName = sendToActiveWindow()
                                            
                                            # put key strokes here
                                            pressAndHold('ctrl')
                                    elif button2New == 1:
                                            print("Button 2 released")
                                            release('ctrl')

                            """                        
                            # Button 3 pushed (Modifier key 3)
                            if button3Old != button3New:
                                    button3Old = button3New
                                    if button3New == 0:
                                            #print("Button 3 pushed")

                                            windowName = sendToActiveWindow()
                                            
                                            # put key strokes here
                                            pressAndHold('shift')
                                    elif button3New == 1:
                                            #print("Button 3 released")
                                            release('shift')
                            
                            # modifier keys
                            button1Old, button1New, modkeyA, modkeyB = modButtonPush(button1Old, button1New, modkeyA, modkeyB, buttonNum, root)
                            button2Old, button2New, modkeyB, modkeyA = modButtonPush(button2Old, button2New, modkeyB, modkeyA, buttonNum, root)
                            #button3Old, button3New, modkeyC, modkeyA, modkeyB = modButtonPush(button3Old, button3New, modkeyC, modkeyA, modkeyB)



                            # normal buttons
                            button4Old, button4New = buttonPush(button4Old, button4New, buttonNum, modkeyA, modkeyB, modkeyC)
                            button5Old, button5New = buttonPush(button5Old, button5New, buttonNum, modkeyA, modkeyB, modkeyC)
                            button6Old, button6New = buttonPush(button6Old, button6New, buttonNum, modkeyA, modkeyB, modkeyC)
                            button7Old, button7New = buttonPush(button7Old, button7New, buttonNum, modkeyA, modkeyB, modkeyC)
                            button8Old, button8New = buttonPush(button8Old, button8New, buttonNum, modkeyA, modkeyB, modkeyC)
                            button9Old, button9New = buttonPush(button9Old, button9New, buttonNum, modkeyA, modkeyB, modkeyC)
                            button10Old, button10New = buttonPush(button10Old, button10New, buttonNum, modkeyA, modkeyB, modkeyC)
                            button11Old, button11New = buttonPush(button11Old, button11New, buttonNum, modkeyA, modkeyB, modkeyC)
                            button12Old, button12New = buttonPush(button12Old, button12New, buttonNum, modkeyA, modkeyB, modkeyC)
                                            
                                    
            except ser.SerialTimeoutException:
                    print('Data could not be read')

            # Gui update
            if modkeyA == 1:
                temp_array = []
                activeWindow = activeWindowName()
                for line in commands:
                        # pull out the program to test against the active window
                        program = line[1].replace("\'", "")
                        program = str(program.replace(",", ""))
                        
                        if program in activeWindow:
                                # pull out the button and keys from the lines
                                # the correct program
                                button = int(line[0].replace(",", ""))

                                key = line[2].replace("\'", "")
                                
                                # create a temporary array to store only the commands
                                # for the active window
                                temp_array.append([button, program, key])
   
                baseRange = [4, 5, 6, 7, 8, 9, 10, 11, 12]
                newRange = []
                
                for item in baseRange:
                    newRange.append(item + 20)
                    
                sub_temp_array = []
                for i in range(0, 9, 1):
                    for line in temp_array:
                        if line[0] == newRange[i]:
                            sub_temp_array.append(line[2])

                q = sub_temp_array
                v.set(str(q[0]) + "    " + str(q[1]) + "    " + str(q[2]) + "\n" +
                      str(q[3]) + "    " + str(q[4]) + "    " + str(q[5]) + "\n" +
                      str(q[6]) + "    " + str(q[7]) + "    " + str(q[8]))
            elif modkeyB == 1:
                temp_array = []
                activeWindow = activeWindowName()
                for line in commands:
                        # pull out the program to test against the active window
                        program = line[1].replace("\'", "")
                        program = str(program.replace(",", ""))
                        
                        if program in activeWindow:
                                # pull out the button and keys from the lines
                                # the correct program
                                button = int(line[0].replace(",", ""))

                                key = line[2].replace("\'", "")
                                
                                # create a temporary array to store only the commands
                                # for the active window
                                temp_array.append([button, program, key])
   
                baseRange = [4, 5, 6, 7, 8, 9, 10, 11, 12]
                newRange = []
                
                for item in baseRange:
                    newRange.append(item + 40)
                    
                sub_temp_array = []
                for i in range(0, 9, 1):
                    for line in temp_array:
                        if line[0] == newRange[i]:
                            sub_temp_array.append(line[2])

                q = sub_temp_array
                v.set(str(q[0]) + "    " + str(q[1]) + "    " + str(q[2]) + "\n" +
                      str(q[3]) + "    " + str(q[4]) + "    " + str(q[5]) + "\n" +
                      str(q[6]) + "    " + str(q[7]) + "    " + str(q[8]))

            else:
                try:
                    temp_array = []
                    activeWindow = activeWindowName()
                    for line in commands:
                            # pull out the program to test against the active window
                            program = line[1].replace("\'", "")
                            program = str(program.replace(",", ""))
                            
                            if program in activeWindow:
                                    # pull out the button and keys from the lines
                                    # the correct program
                                    button = int(line[0].replace(",", ""))

                                    key = line[2].replace("\'", "")
                                    
                                    # create a temporary array to store only the commands
                                    # for the active window
                                    temp_array.append([button, program, key])
       
                    baseRange = [4, 5, 6, 7, 8, 9, 10, 11, 12]
                    newRange = baseRange
                        
                    sub_temp_array = []
                    for i in range(0, 9, 1):
                        for line in temp_array:
                            if line[0] == newRange[i]:
                                sub_temp_array.append(line[2])

                    q = sub_temp_array
                    v.set(str(q[0]) + "    " + str(q[1]) + "    " + str(q[2]) + "\n" +
                          str(q[3]) + "    " + str(q[4]) + "    " + str(q[5]) + "\n" +
                          str(q[6]) + "    " + str(q[7]) + "    " + str(q[8]))
                except:
                    v.set("")

            root.update()
                    
            count += 1

