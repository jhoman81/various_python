import os 
import sys

def penultimateWord(text):
	split_text = text.split()
	new_line = split_text[len(split_text) - 2]
	return new_line

if __name__ == '__main__':
	word = "The quick dog jumped over the log"
	word2 = "Another one, and a third"
	word3 = "Finally the Rock has come back to Chicago fpr the last time"

	print(penultimateWord(word))
	print(penultimateWord(word2))
	print(penultimateWord(word3))

