"""You are given a text. Write a program which outputs its lines according to the following rules:

If line length is ≤ 55 characters, print it without any changes.
If the line length is > 55 characters, change it as follows:
Trim the line to 40 characters.
If there are spaces ‘ ’ in the resulting string, trim it once again to the last space (the space should be trimmed too).
Add a string ‘... <Read More>’ to the end of the resulting string and print it.
"""

import sys

def trim_line(text):
	text = text.split()
	new_arr = []
	for i in range (len(text)):
		if i > 39:
			break
		new_arr.append(text[i])
	new_string = " ".join(new_arr)
	new_string = new_string.rstrip()
	return("%s... <Read More>" % (new_string))

if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
		lines = list(f)
	for line in lines:
		if len(line) > 55:
			print(trim_line(line))
		else:
			print(line)
	f.close()