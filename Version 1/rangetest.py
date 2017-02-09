textFile = open("ProgramCommands.txt", 'r')
commands = [line.split() for line in textFile]

modkeyA = 0
modkeyB = 0

temp_array = []
activeWindow = "Notepad"
print(activeWindow)
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
if modkeyA == 1:
    for item in baseRange:
        newRange.append(item + 20)
elif modkeyB == 1:
    for item in baseRange:
        newRange.append(item + 40)
else:
    newRange = baseRange
    
sub_temp_array = []
for i in range(0, 8, 1):
    for line in temp_array:
        if line[0] == newRange[i]:
            sub_temp_array.append(line[2])

print(sub_temp_array)
