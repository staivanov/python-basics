from pathlib import Path

# Reading Pi from a *.txt file on my local machine.
content_name = 'pi_digits.txt'
path = Path(content_name)
contents = path.read_text().rstrip()
lines = contents.splitlines()
pi_string = ''

for line in lines:
   pi_string += line.strip()

print(pi_string)
print(f"The Length on pi_string is {len(pi_string)}")



