from pathlib import Path

python_basics_grade = str(6)
simple_content = f"I am improving my Python skills right now. My current grade on \'Python basics\' is {python_basics_grade}."
simple_content += 'The next step is to learn how to test my code.'
simple_content += 'And then I will be ready to make a small Python project to harden my skills.'

file_name = Path('programming.txt')
file_name.write_text(simple_content)
