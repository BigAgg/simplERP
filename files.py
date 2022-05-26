import os

def read_file(path):
	""" Reads given file if existing

	Args:
		path (String): Path to file that should be read

	Returns:
		Tuple: Without '\n'
	"""
	if os.path.exists(path):
		with open(path, mode="r", encoding="utf-8") as file:
			return file.read().splitlines()
	return("File doesn't exist")


def write_file(path, content):
	""" Writes / creates file with given path and content

	Args:
		path (String): Path to either an existing or new file
		content (Tuple): Written 1 by 1 / line by line into the given file
	"""
	with open(path, mode="w", encoding="utf-8") as file:
		for i in content: file.write(f"{i}\n")


def get_string(content):
	""" Return a String out of a tuple

	Args:
		content (Tuple): Given tuple to convert

	Returns:
		String: Converted tuple
	"""
	final_string = ""
	for i in content: final_string += f"{i}\n"
	return final_string