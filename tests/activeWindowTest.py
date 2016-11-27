from win32gui import GetWindowText, GetForegroundWindow
import time

while 1:
    activeWindow = GetWindowText(GetForegroundWindow())
    print(activeWindow)
    time.sleep(5)
        
        
