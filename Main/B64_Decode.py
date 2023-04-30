import os
import sys
import base64
import shutil

if len(sys.argv) < 2:
    print("Please drag and drop a .txt file onto this script.")
    sys.exit()

input_file_path = sys.argv[1]

# Check if the input file exists
if not os.path.isfile(input_file_path):
    print(f"{input_file_path} does not exist.")
    sys.exit()

# Check if the input file is a .txt file
if not input_file_path.lower().endswith('.txt'):
    print("Please provide a .txt file.")
    sys.exit()

# Open and read the input file
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    encoded_string = input_file.read()

# Decode the base64 string
decoded_data = base64.b64decode(encoded_string)

# Determine the file extension based on the first few bytes of the decoded data
FILE_EXTENSION = None
if decoded_data[1:4] == b'PNG':
    FILE_EXTENSION = '.png'
elif decoded_data[0:4] == b'GIF8':
    FILE_EXTENSION = '.gif'
elif decoded_data[6:10] == b'JFIF':
    FILE_EXTENSION = '.jpg'

# If the file extension is unknown, exit
if FILE_EXTENSION is None:
    print("Unknown file type.")
    sys.exit()

# Write the decoded data to a new file with the appropriate file extension
output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"decoded_image{FILE_EXTENSION}")
with open(output_file_path, 'wb') as output_file:
    output_file.write(decoded_data)
shutil.move(output_file_path,'decoded_output\\')

print(f"File saved to {output_file_path}")
