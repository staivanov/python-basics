from pathlib import Path

# 10.4 Prompts the user for their name. Write their response to a file.

prompt_message = "Please, enter your first and last name."
print(prompt_message)
first_name = input("First name: ")
last_name = input("Last name: ")
full_name = f"{first_name} {last_name}"

file_name = "guest.txt"
path = Path(file_name)
path.write_text(full_name)

# 10.5 Guest book. Collect all names from the current user as an input from the console and write these names to a file.
guest_names = ""

while True:
    print("What is your name? Enter \'q\' to quit.")
    print("Enter your full name: ")
    current_full_name = input()
    if current_full_name == 'q': break
    guest_names += current_full_name + '\n'

guests_file_name = 'guest_book.txt'
guests_path = Path(guests_file_name)
guests_path.write_text(guest_names)
