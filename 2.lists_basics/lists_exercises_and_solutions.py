# 1.
animals: list[str] = ["dog", "eagle", "lion", "cat", "bear", "snake"]
print(animals[0])
print(animals[1])
print(animals[2])
print(animals[3])
print(animals[4])
print(animals[5])
print('*' * 30)
message_to_someone: str = f"Hey, many people like {animals[0]}s"
print(message_to_someone)
print('*' * 30)

# 3.4 Guest List.
invited_people: list[str] = ["Andrew Carnegie", "Adolf Hitler", "Henry Ford"]
message_to_ac: str = invited_people[0]
message_to_ah: str = invited_people[1]
message_to_hf: str = invited_people[2]
print(f"Hello, {message_to_ac}! We will highly appreciate your presence!")
print(f"Guten morgen, {message_to_ah}. We will serve dinner on 6 June.")
print(f"Greeting, Mr.{message_to_hf}. Soon we will make dinner. Please, visit us at June 6.")
print('*' * 30)

# 3.5 Changing Guest List.
print(
    f"Mr.{message_to_ah} has 99 problems in his country and will miss our dinner. In this case i need to invite someone else.")
jimi_hendrix: str = "Jimi Hendrix"
invited_people[1]: str = jimi_hendrix
message_to_jh: str = f"Rock n Roll, {jimi_hendrix}. We will glad to become one of us on June 6 for dinner"
print(message_to_jh)
print('*' * 30)

# 3.6 More guests.
print(
    f"Current list of all guests is {invited_people}, but I find a new, bigger table. Now i will invite three more people.")
stanislav: str = "Stanislav Ivanov"
message_to_s: str = f"Zdrasti, {stanislav}! Shte vecheryame na 6-ti June."
invited_people.insert(0, stanislav)
mid_of_guest_list: int = int(len(invited_people) / 2)
best_football_player: str = "Lionel Messi"
invited_people.insert(mid_of_guest_list, best_football_player)
best_midfielder_in_the_world: str = "Andres Iniesta"
invited_people.append(best_midfielder_in_the_world)
print(f"After last corrections in my list guests are: {invited_people}")
cnt_guests: int = len(invited_people)
print(f"It contains {cnt_guests} guests.")
print('*' * 30)

# 3.7 Shrinking guests list.
MAX_INVITED_GUESTS: int = 2
print("Now i can invites only two people.")
while len(invited_people) > MAX_INVITED_GUESTS:
    current_person: str = invited_people.pop()
    msg_to_the_current_person = f"Sorry, {current_person}, I can't invite you for this dinner."
    print(msg_to_the_current_person)

first_invited: str = invited_people[0]
second_invited: str = invited_people[1]
msg_to_invited_people: str = f'Mr.{first_invited} and Mr.{second_invited} are invited for special dinner on June 6 at Manhattan, NYC.")'
print(msg_to_invited_people)
del first_invited
del second_invited
