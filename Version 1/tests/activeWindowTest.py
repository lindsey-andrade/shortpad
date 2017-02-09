from win32gui import GetWindowText, GetForegroundWindow
from WindowMgr import WindowMgr
import time

while 1:
    activeWindow = GetWindowText(GetForegroundWindow())
    print(activeWindow)
    time.sleep(5)

    WindowMgr().find_Window()
    print(WindowMgr()._handle)
        
        
