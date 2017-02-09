import sys
from cx_Freeze import setup, Executable

exe = Executable(
	script = r"buttonTyper.py",
	base = 'WIN32GUI'
)

packages = ['serial.win32']
include = ['serial']
includefiles = ['ProgramCommands.txt']

setup(
	name = "ShortPad",
	version = "0.1",
	description = "A programable keyboard shortcut for any program",
	executables = [exe],
	options = {'build_exe': {'packages':packages,'include_files':includefiles}}
)