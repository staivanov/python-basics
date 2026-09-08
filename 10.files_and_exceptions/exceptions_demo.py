from pathlib import Path

# Using try-except blocks

try:
    print(79 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
print("*" * 50)
# Using exceptions to prevent crashes.

# print("This is a very simple program that divide two user-defined numbers.")
# print("Enter \'q\' to exit.")
#
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q': break
#
#     second_number = input("\nSecond number: ")
#     if second_number == 'q': break
#
#     try:
#         result = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by zero.")
#     else:
#         print(result)

# Handling the FileNotFoundError exception.
pipi_file = "pippi longstocking.txt"
pippi_longstocking_path = Path(pipi_file)

try:
    pippi_longstocking_content = pippi_longstocking_path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"This file path doesn't exist.")
print("*" * 50)

# Analyzing text and count all words from the provided text by path reference.
python_file_name = "learning_python.txt"
path_to_python_file_name = Path(python_file_name)

try:
    contents_python_file_name = path_to_python_file_name.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"The file {python_file_name} does not exist!")
else:
    words = contents_python_file_name.split()
    wordsCnt = len(words)
    print(f"The number of words is {wordsCnt} in the {python_file_name} file.")
print("*" * 50)

