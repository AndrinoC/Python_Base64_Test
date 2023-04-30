import base64
import sys

if len(sys.argv) < 2:
    print("Please drag and drop an image or GIF file onto this script.")
    sys.exit()

input_file_path = sys.argv[1]

with open(input_file_path, 'rb') as input_file:
    encoded_string = base64.b64encode(input_file.read())
with open('encoded_output/EncondedFile.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(encoded_string.decode('utf-8'))
    print("Encoded base64 saved to EncodedFile.txt")