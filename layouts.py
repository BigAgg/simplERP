import PySimpleGUI as sg
import os
from files import *
from screeninfo import get_monitors

screen = get_monitors()[0]
width = screen.width / 3
height = screen.height / 3
TESTSIZE = (300,100)


def main_window(__version__, current_size):
	""" Startup window - control window

	Args:
		__version__ (String): Project version number to display on window
		current_size (Tuple): Current window size to calculate Listbox size

	Returns:
		Window: Finished and finalized window settings ready to be used
	"""
	layout = [[sg.Text(f"Simple ERP Version {__version__}")],
	[sg.Input(key="-IN-", enable_events=True, size=(30,1), tooltip="Module searchbar"), sg.Text(f"{' ' * 4}Module information:")],
	[sg.Listbox(values=read_file("options.txt"), key="-OPTIONS-", enable_events=True, size=(30, current_size[1] // 3)), 
	sg.Multiline(disabled=True, key="-INFOBOX-", size=(50, current_size[1] // 3 + 2))]]
	return sg.Window("SimplERP", layout, default_element_size=(12, 1), resizable=False, location=(width, height)).Finalize()


def browse_articles_window(current_size):
	""" Browse articles window

	Args:
		current_size (Tuple): Current window size to calculate boxes (not used right now)

	Returns:
		Window: Finished and finalized window settings ready to be used
	"""
	layout = [[sg.Text("Browse articles")],
	[sg.Input(key="-IN-", enable_events=True)],
	[sg.Listbox(values=os.listdir("articles"), key="-OPTIONS-", size=(30, 6))]]
	return sg.Window("SimplERP - Browse articles", layout, resizable=False, location=(100,100)).Finalize()


def create_articles_window(current_size):
	""" Create articles window

	Args:
		current_size (Tuple): Current window size to calculate boxes (not used right now)

	Returns:
		Window: Finished and finalized window settings ready to be used
	"""
	layout = [[sg.Text("Create articles")],
	[sg.Text(f"Select Parent-Article:{' ' * 5}Name:")]]
	return sg.Window("SimplERP - Create articles", layout, resizable=False, location=(100,100)).Finalize()


def testrun():
	win = main_window(0,TESTSIZE)
	win = browse_articles_window(TESTSIZE)
	win = create_articles_window(TESTSIZE)


if __name__ == "__main__":
	testrun()