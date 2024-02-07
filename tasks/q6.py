import os
script_directory = os.path.dirname(os.path.realpath(__file__))
input_file_name = os.path.join(script_directory, 'q6file.txt')
output_file_name =  os.path.join(script_directory, 'output.txt')




def fn(file_content):
    lines = file_content.split('\n')
    words = file_content.split(' ')
    return len(lines), len(words)

try:
    with open(input_file_name, 'r') as input_file:
        content = input_file.read()

        line_count, word_count = fn(content)

        print('check the output file for results')

        with open(output_file_name, 'w') as output_file:
            output_file.write(f"Number of lines: {line_count}\n")
            output_file.write(f"Number of words: {word_count}\n")
except FileNotFoundError:
    print(f"Error: The file '{input_file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
