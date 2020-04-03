#!/usr/bin/env python

import json
import os

INPUT_DIR = "input"
OUTPUT_DIR = "output"
MAX_LINES = 50
PROMPTS = [
	"most beautiful line",
	"ugliest line",
	]

"""
in this function, "result" will be a dict like this:
{
  "most beautiful line": 17,
  "ugliest line": 7,
}
"""
def process(filename):
	print("=== PROCESSING FILE: {} ===".format(filename))
	result = {}
	# put all the lines of the file in a list
	list_of_lines = open(os.path.join(INPUT_DIR, filename)).readlines()
	# truncate if it's too long
	list_of_lines = list_of_lines[:MAX_LINES]
	for line_number, line in enumerate(list_of_lines):
		line = line.rstrip('\n')
		print("{}\t{}".format(line_number, line))
	for prompt in PROMPTS:
		print("Please enter the {}.".format(prompt))
		print("If there are multiple, enter them all, separated by spaces.")
		line_numbers = input("> ")
		result[prompt] = []
		if line_numbers == "":
			continue
		else:
			line_numbers = line_numbers.split()
			for line_number in line_numbers:
				if line_number.isdigit():
					result[prompt].append(int(line_number))
				else:
					print("{!r} is not a valid number. Trying again."
						.format(line_number))
					return process(filename)
	# ok now we have the dict "result"  
	# now we ask for confirmation
	print(result)
	confirm = input(
		"Press ENTER is this is good.\n"
		"Press anything else + ENTER to try again.\n")
	if confirm == "":
		# save the results
		json_file = os.path.join(OUTPUT_DIR, filename + ".json")
		with open(json_file, "w") as f:
			json.dump(result, f)
		os.rename(
			os.path.join(INPUT_DIR, filename),
			os.path.join(OUTPUT_DIR, filename))
	else:
		return process(filename)


for filename in sorted(os.listdir(INPUT_DIR)):
	process(filename)
