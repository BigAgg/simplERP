import PySimpleGUI as sg
import os
from files import *
from layouts import *
from time import perf_counter

__version__ = "0.0.1"
__author__ = "Adrian Jahraus"

sg.theme("DarkGrey8")

current_size = (300, 100)

selected = None
start_window = main_window(__version__, current_size)
while 1:
	window, event, values = sg.read_all_windows()
	if event == sg.WIN_CLOSED or event == "Exit":
		window.close()
		if window == start_window:
			break
	
	if event == "-IN-":
		filter_list = values.get("-IN-")
		if window == start_window:
			try:
				final = []
				for i in read_file("options.txt"):
					if filter_list in i.lower():
						final = final.append(i)
					if filter_list == "":
						final = final.append(i)
				window["-OPTIONS-"].Update(final)
			except:
				window["-OPTIONS-"].Update(read_file("options.txt"))
				
		elif window == browse_article_window:
			try:
				final = []
				for i in os.listdir("articles"):
					if filter_list in i.lower():
						final = final.append(i)
				window["-OPTIONS-"].Update(final)
			except:
				window["-OPTIONS-"].Update(os.listdir("articles"))
	
	if event == "-OPTIONS-":
		if selected == values.get("-OPTIONS-")[0]:
			if selected == "Browse articles":
				browse_article_window = browse_articles_window(current_size)
				selected = None
		else:
			selected = values.get("-OPTIONS-")[0]
			window["-INFOBOX-"].Update(get_string(read_file(f"info/{selected}.txt")))

