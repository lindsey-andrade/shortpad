from buttonTyper import sendToActiveWindow
from packages.keydictionary import press
import time

time.sleep(3)

with open("ProgramCommands.txt") as textFile:
        commands = [line.split() for line in textFile]

def buttonPush(old, new, button_num):
        temp_array = []
        activeWindowName = sendToActiveWindow()
        newline = [0, 0, 0]

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
                        
                        print(newline)

                        # create a temporary array to store only the commands
                        # for the active window
                        temp_array.append([button, program, key])
                        
                else:
                        print('No Program Commands Found')

        
        if old != new:
                old = new
                if new == 0:
                        print('Button ' + str(button_num) + ' Pushed')
                        for line in temp_array:
                                if line[0] == button_num:
                                        print("button match")
                                        key = line[2]
                                        press(key)
        
        return old, new

buttonPush(1, 0, 1)
