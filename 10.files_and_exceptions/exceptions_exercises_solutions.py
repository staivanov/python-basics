from pathlib import Path

#  10.6 Addition. Get two user-defined numbers, sum them and print them on the console. If there is a ValueError catch it.

# try:
#     number_one = int(input("What is your first number? "))
#     number_two = int(input("What is your second number? "))
#     sum_of_the_two_numbers = number_one + number_two
# except ValueError:
#     print("Please, enter a valid number!")
# else:
#     print(sum_of_the_two_numbers)

print('*' * 30)

#  10.7 Addition Calculator.
#  Wrap with loop code from above so that the current user can enter values even if they mistakenly enter text.

# while True:
#     try:
#         number_one = int(input("What is your first number? "))
#         number_two = int(input("What is your second number? "))
#         sum_of_the_two_numbers = number_one + number_two
#     except ValueError:
#         print("Please, enter a valid number!")
#     else:
#         print(sum_of_the_two_numbers)

#  10.8 Cats and Dogs.

cats_file_name = "cats.txt"
dogs_file_name = "dogs.txt"
cats = [];
dogs = []
cats_path = Path(cats_file_name)
dogs_path = Path(dogs_file_name)

try:
    cats = cats_path.read_text()
    dogs = dogs_path.read_text()
except FileNotFoundError:
    print("Error in the file path!")
else:
    print(cats)
    print(dogs)

print('*' * 30)


#  10.10 Common words.

def count_word_occurrences(word: str, path: Path) -> int:
    """Count occurrences of a word in a text file.

Args:
    word: The word to search for.
    path: Path to the text file.

Returns:
    The number of occurrences of the word.
"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print("The file is not found on this path! Check the file name or the file path.")
    else:
        word_occurrence_cnt = contents.lower().split().count(word.lower())
        return word_occurrence_cnt


books_title = ["The story of the world.txt", "The Adventures of Sherlock Holmes.txt", "The Odyssey.txt"]

for book_title in books_title:
    current_path = Path(book_title)
    word_token = "the"
    word_cnt = count_word_occurrences(word_token, current_path)
    print(f"The word \"{word_token}\" is founded {word_cnt} in {current_path}")
print('*' * 30)
