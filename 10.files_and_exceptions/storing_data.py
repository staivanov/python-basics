from pathlib import Path
import json

# Using json.dump() and json.load().

numbers = list(range(1, 21))
contents = json.dumps(numbers)
numbers_file_name = 'numbers.json'
numbers_path = Path(numbers_file_name)
numbers_path.write_text(contents) # The provided content is written to the file with user-defined path.

read_numbers = numbers_path.read_text() # File with a user-defined path is read in the memory.
numbersTwo = json.loads(read_numbers) # A string in a JSON format is deserialized and returns a Python object. In the current case is a list.
print(numbersTwo)