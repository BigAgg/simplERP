import PySimpleGUI as sg
import os
from files import *
from screeninfo import get_monitors

screen = get_monitors()[0]
width = screen.width / 3
height = screen.height / 3


def main_window(__version__, current_size):
	layout = [[sg.Text(f"Simple ERP Version {__version__}")],
	[sg.Input(key="-IN-", enable_events=True, size=(30,1), tooltip="Module searchbar"), sg.Text(f"{' ' * 4}Module information:")],
	[sg.Listbox(values=read_file("options.txt"), key="-OPTIONS-", enable_events=True, size=(30, current_size[1] // 3)), 
	sg.Multiline(disabled=True, key="-INFOBOX-", size=(50, current_size[1] // 3 + 2))]]
	return sg.Window("Simple ERP", layout, default_element_size=(12, 1), resizable=False, location=(width, height)).Finalize()


def browse_articles_window(current_size):
	layout = [[sg.Text("Browse articles")],
	[sg.Input(key="-IN-", enable_events=True)],
	[sg.Listbox(values=os.listdir("articles"), key="-OPTIONS-", size=(30, 6))]]
	return sg.Window("Simple ERP - Browse articles", layout, resizable=False, location=(100,100)).Finalize()


def create_articles_window(current_size):
	layout = [[sg.Text("Create articles")],
	[sg.Text(f"Select Parent-Article:{' ' * 5}Name:")]]
