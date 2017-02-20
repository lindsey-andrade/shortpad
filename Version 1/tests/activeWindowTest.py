from win32gui import GetWindowText, GetForegroundWindow
from WindowMgr import WindowMgr
import time

while 1:
    activeWindow = GetWindowText(GetForegroundWindow())
    print(activeWindow)
    window_title = activeWindow.split('-')[0]
    wildcard = ".*" + window_title + ".*"
    print(wildcard)

    time.sleep(5)

    # WindowMgr().find_Window()
    # print(WindowMgr()._handle)
        
        
