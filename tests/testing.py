import keydictionary
import time
from windowswitch import WindowMgr


w = WindowMgr()
w.find_window_wildcard(".*source.*")
w.set_foreground()

time.sleep(1)

keydictionary.pressHoldRelease('alt', 'tab')

'''
w = WindowMgr()
w.find_window_wildcard(".*testing.*")
w.set_foreground()
'''
