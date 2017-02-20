from pyserial import serial
import time
from packages.keydictionary import press, pressAndHold, release, typer, pressHoldRelease
from packages.windowswitch import WindowMgr
from win32gui import GetWindowText, GetForegroundWindow
import struct
from tkinter import *
import threading
from programCommands import programCommands
import win32process
import wmi


class Box(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Simple")
        self.pack(fill = BOTH, expand = 1)

class KeyboardShortCut(threading.Thread):
    def __init__(self, serial):

        threading.Thread.__init__(self)

        self.oldModDict = {1:1, 2:1, 3:1}
        self.newModDict = {1:1, 2:1, 3:1}
        self.modValues = {1:0, 2:0}
        self.oldButtonDict = {4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:1}
        self.newButtonDict = {4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:1}
        self.oldWindow = ""
        self.newWindow = ""

        self.changedModkey = 0

        self.ser = serial

        self.c = wmi.WMI()

        self.exe = ""



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
    def modButtonPush(self):

        for key, value in self.newModDict.items(): 
                if self.oldModDict[key] != self.newModDict[key]:
                    self.oldModDict[key] = self.newModDict[key]
                    if value == 0: 
                        ### testing
                        if key == 1:                           
                            self.modValues[1] = abs(self.modValues[key] - 1) #this is the error
                            self.modValues[2] = 0
                            # print(self.modValues)
                            
                        elif key == 2: 
                            self.modValues[2] = abs(self.modValues[2] - 1)
                            self.modValues[1] = 0
                            # print(self.modValues)

                        self.changedModkey = 1
                        


    """
    buttonPush function takes in old and new button states and the button number and pulls the correct
    key command for the active window. Key commands are kept in a text file called "ProgramCommands.txt"
    in the same folder as this file.

    By total chance, if a program doesn't have defined key commands and a button is pushed in that program
    nothing happens because the temp_array of commands is empty. ¯\_(?)_/¯
    """
    def buttonPush(self):

            # temp_array = []

            for key, value in self.newButtonDict.items(): 
                if self.oldButtonDict[key] != self.newButtonDict[key]:
                    self.oldButtonDict[key] = self.newButtonDict[key]

                    if value == 0:                             
                        # activeWindowName = self.sendToActiveWindow()
                        activeWindowName = self.sendToActiveWindow()
                        # activeWindowName = self.activeWindowName()

                        modkeyA = self.modValues[1]
                        modkeyB = self.modValues[2]


                        for program, commandDict in programCommands.items():
                            if program in activeWindowName:
                                keyval = commandDict[key]
                                if modkeyA == 1: 
                                    keyval = commandDict[key + 20]
                                if modkeyB == 1:
                                    keyval = commandDict[key + 40]
                                

                                if "+" in keyval: 
                                    keys = keyval.split("+")
                                    pressHoldRelease(keys[0], keys[1])
                                elif keyval == 'esc': #lol it tries to type "esc"
                                        press('esc')
                                elif keyval == 'del':
                                        press('del')
                                else:
                                        typer(keyval)
                            
                                      
    def sendToActiveWindow(self):
            ## Type in Window Code - START
            full_window_name = GetWindowText(GetForegroundWindow()) #only acts on active window
            # print(full_window_name)

            w = WindowMgr()
            #don't try this code on the python source while it's running. it hates it
            if "@" in full_window_name:
                window_title = full_window_name.split(" @")[0]
                # print(window_title)
                w.find_window_wildcard(window_title)
            else:
                window_title = full_window_name.split('-')[0]
            
                wildcard = ".*" + window_title + ".*"
            

                # this if loop is to make it not possible to type in the Python Shell
                # if full_window_name != "*Python 3.4.3 Shell*":
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
                    w.find_window_wildcard(wildcard)
                    # print("wild " + wildcard)
                except:   
                    w.find_window_wildcard(full_window_name)
                    # print("full " + full_window_name)
                finally:
                    w.set_foreground()
                    
            # else:
            #         print('Do not push the button in this window')
            # ## Type in Window - END

            return self.activeWindowName()

    def get_app_name(self, hwnd):
        """Get applicatin filename given hwnd."""
        try:
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            for p in self.c.query('SELECT Name FROM Win32_Process WHERE ProcessId = %s' % str(pid)):
                self.exe = p.Name
                break
        except:
            return None
        else:
            return self.exe

    def activeWindowName(self):
        #return program name instead
        # print(self.get_app_name(GetForegroundWindow()))c
        return self.get_app_name(GetForegroundWindow())

        # return GetWindowText(GetForegroundWindow())

    def detectChange(self):
        a = 0
        b = 0
        self.newWindow = GetWindowText(GetForegroundWindow()) 
        # self.newWindow = self.activeWindowName()

        if keyboard.changedModkey == 1:
            a = 1
            keyboard.changedModkey = 0               

        if self.oldWindow != self.newWindow:
            self.oldWindow = self.newWindow
            # print(self.newWindow)
            b = 1
            # print(self.newWindow)

        if a or b:
            # print("change detected")
            return 1
        else:
            # print("no change)")
            return 0
            


    def funct(self, root):
        try:
            new = str(self.ser.readline())
                  
            if len(new) == 10: # sometimes serial outputs messed up strings. this filters it

                buttonNum = int(new[2:4]);

                state = int(new[4])

                if buttonNum < 4: 
                    self.newModDict[buttonNum] = state
                else: 
                    self.newButtonDict[buttonNum] = state

            
                # Button 3 pushed (Modifier key 3)
                if self.newModDict[3] != self.oldModDict[3]:
                    if self.newModDict[3] == 0:
                        #print("Button 3 pushed")
                        windowName = self.sendToActiveWindow()
                        pressAndHold('shift')
                    elif self.newModDict[3] == 1:
                        #print("Button 3 released")
                        release('shift')
                
                # modifier keys
                self.modButtonPush()

                # normal buttons
                self.buttonPush()

        except ser.SerialTimeoutException:
            print('Data could not be read')
                
            

if __name__ == "__main__":
    root = Tk()
    root.geometry("250x150+300+300")
    app = Box(root)

    v = StringVar()
    Label(root, textvariable = v).pack()

    w = Label(root, text = "hello, world!")
    w.pack()
    # root.update_idletasks()
    # root.update()

    
    ser = serial.Serial()
    ser.setPort('COM5')
    ser.baudrate = 9600
    ser.open() #gotta open the ser to flush it
    ser.flushInput() #something about clearing the queue of stuff still in there
    ser.flushOutput()
    print('Serial complete')

    keyboard = KeyboardShortCut(ser)
    

    while 1:
        keyboard.funct(root)

        modkeyA = keyboard.modValues[1]
        modkeyB = keyboard.modValues[2]

        # # Gui update
        if keyboard.detectChange():
            # print(keyboard.activeWindowName())
            if modkeyA == 1:
                pass
                activeWindow = keyboard.activeWindowName()

                q = []


                for program, commandDict in programCommands.items():
                    if program in activeWindow:
                        for i in range(24,33,1):
                            q.append(commandDict[i])
                        v.set(str(q[6]) + "    " + str(q[7]) + "    " + str(q[8]) + "\n" +
                            str(q[3]) + "    " + str(q[4]) + "    " + str(q[5]) + "\n" +
                            str(q[0]) + "    " + str(q[1]) + "    " + str(q[2]))

            elif modkeyB == 1:
                pass
                activeWindow = keyboard.activeWindowName()

                q = []


                for program, commandDict in programCommands.items():
                    if program in activeWindow:
                        for i in range(44,53,1):
                            q.append(commandDict[i])
                        v.set(str(q[6]) + "    " + str(q[7]) + "    " + str(q[8]) + "\n" +
                            str(q[3]) + "    " + str(q[4]) + "    " + str(q[5]) + "\n" +
                            str(q[0]) + "    " + str(q[1]) + "    " + str(q[2]))

            else:
                # pass
                try:

                    activeWindow = keyboard.activeWindowName()
                    # print(activeWindow)

                    q = []

                    for program, commandDict in programCommands.items():
                        if program in activeWindow:
                            # print(program)
                            for i in range(4,13,1):
                                q.append(commandDict[i])
                            v.set(str(q[6]) + "    " + str(q[7]) + "    " + str(q[8]) + "\n" +
                                str(q[3]) + "    " + str(q[4]) + "    " + str(q[5]) + "\n" +
                                str(q[0]) + "    " + str(q[1]) + "    " + str(q[2]))

                except Exception as e:
                    # print(e)
                    v.set("")

        
            root.update()
            # pass
        # 