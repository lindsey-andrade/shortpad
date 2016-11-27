from keydictionary import press, pressAndHold, release, typer, pressHoldRelease
from windowswitch import WindowMgr
import time

pressHoldRelease('LWIN', 'r')
typer('C:/Users/landrade/Desktop/python/source.txt')
press('enter')

w = WindowMgr()
w.find_window_wildcard(".*source.*")
w.set_foreground()

time.sleep(1)

pressHoldRelease('ctrl', 'a')
pressHoldRelease('ctrl', 'c')
pressHoldRelease('alt', 'F4')

w = WindowMgr()
w.find_window_wildcard(".*Messenger.*")
w.set_foreground()

pressHoldRelease('ctrl', 'v')
press('enter')


