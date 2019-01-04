#!/usr/bin/python
# Import sys for exit()
import sys
# Import os for checking the file if present
import os.path

# Check if input has provided
if len(sys.argv) <= 1:
    print('Enter file name to parse the content: ./sample.py <filename>')
    sys.exit()

# Get input file from commandline arg
input_file = sys.argv[1]
# Check if file is present or not
file_present_flag = os.path.isfile(input_file)

# If file is not present ask the user to check if file exist!
if not file_present_flag:
    print('Error: Input file \"{}\" is not present!'.format(input_file))
    sys.exit()

'''
Steps:
1. Open the file in read mode.
2. Traverse word by word
3. While traversing if the first character is not a capital letter
   also last charcater of previuos string ends with '.' then
   copy word into list
4. Convert list into string for formatted output screen
'''
list = []
previous_word = ""
with open(input_file, 'r') as fd:
    for line in fd:
        for word in line.split():
            flag = previous_word.endswith('.')
            if word[0] >= 'a' and word[0] <= 'z' or flag:
                list.append(word)
            # print(word)
            previous_word = word

parse_string_reslt = ' '.join(list)
print(parse_string_reslt)

