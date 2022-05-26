import os

def read_file(path):
	if os.path.exists(path):
		with open(path, mode="r", encoding="utf-8") as file:
			return file.read().splitlines()
	return("File doesn't exist")


def write_file(path, content):
	with open(path, mode="w", encoding="utf-8") as file:
		for i in content: file.write(f"{i}\n")


def get_string(content):
	final_string = ""
	for i in content: final_string += f"{i}\n"
	return final_string