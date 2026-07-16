#1.
animals = ["dog", "eagle", "lion", "cat", "bear", "snake"]
print(animals[0])
print(animals[1])
print(animals[2])
print(animals[3])
print(animals[4])
print(animals[5])
print("*******************")
message_to_someone= f"Hey, many people like {animals[0]}s"
print(message_to_someone)
print("*******************")
#2. List of four dead people who I can  invite on dinner.
invited_people = ["Andrew Carnegie", "Adolf Hitler", "Henry Ford"]
message_to_ac = invited_people[0]
message_to_ah = invited_people[1]
message_to_hf = invited_people[2]
print(f"Hello, {message_to_ac}! We will highly appreciate your presence!")
print(f"Guten morgen, {message_to_ah}. We will serve dinner on 6 June.")
print(f"Greeting, Mr.{message_to_hf}. Soon we will make dinner. Please, visit us at June 6.")
#3 Something surprisingly happens.
print(f"Mr.{message_to_ah} has 99 problems in his country and will miss our dinner. In this case i need to invite someone else.")
jimi_hendrix = "Jimi Hendrix"
invited_people[1] = jimi_hendrix
message_to_jh = f"Rock n Roll, {jimi_hendrix}. We will glad to become one of us on June 6 for dinner"
print(message_to_jh)
#4. Our dinner will have more guests.
print(f"Current list of all guests is {invited_people}, but I find a new, bigger table. Now i will invite three more people.")
stanislav = "Stanislav Ivanov"
message_to_s = f"Zdrasti, {stanislav}! Shte vecheryame na 6-ti June."
invited_people.insert(0, stanislav)
mid_of_guest_list = int(len(invited_people) / 2)
best_football_player = "Lionel Messi"
invited_people.insert(mid_of_guest_list, best_football_player)
best_midfielder_in_the_world = "Adres Iniesta"
invited_people.append(best_midfielder_in_the_world)
print(f"After last corrections in my list guests are: {invited_people}")
#5 Something unexpected happens.
print("Now i can invites only two people.")
while len(invited_people) > 2:
    current_person = invited_people.pop()
    print(f"Sorry, {current_person}, I can't invite you for this dinner.")

first_invited = invited_people[0]
second_invited = invited_people[1]
print(f"Mr.{first_invited} and Mr.{second_invited} are invited for special dinner on June 6 at Manhatta, NYC ")
del first_invited
del second_invited



