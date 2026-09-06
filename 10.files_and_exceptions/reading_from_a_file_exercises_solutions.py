from pathlib import Path

# 10.1 Learning Python

file_name = 'learning_python.txt'
file_name_path = Path(file_name)
learning_python_content = file_name_path.read_text().rstrip()
print(learning_python_content)
print('*' * 30)
# Storing every line from the read file in a list.
content_of_lines = learning_python_content.splitlines()

for line in content_of_lines:
    print(line)
print('*' * 30)

# 10.2 Learning C. Replace every word Python with user defined word.
for line in content_of_lines:
    line = line.replace('Python', 'C')
    print(line)
print('*' * 30)
