import enchant
import sys

#get the input name from the command line arguments
input_name = sys.argv[1]
input_name = input_name.lower()

#load the list of name from the text file
name_list = enchant.PyPWL("name_list.txt")

#check if the name exist in the text file
name_exist = name_list.check(input_name)

print("Name exist: ", name_exist)

if not name_exist:
	#get the correction/suggestion for the input word
	suggestion = name_list.suggest(input_name)

	print("Input: ", input_name)
	print("Suggestion: ", suggestion)