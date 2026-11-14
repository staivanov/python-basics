first_name: str = "stanislav"
last_name: str = "ivanov"
# f-strings
full_name: str = f"{first_name} {last_name}"
print(full_name)
name: str = first_name + " " + last_name
print(name.title())

print('*' * 40)
pet_name: str = "Lisa"
print(pet_name)
print(pet_name.lower())
print(pet_name.upper())
print(f"\t{pet_name.title()}")
pets: str = f'Pets from last fifteen years: \n\tTomi \n\tLisa \n\tLucky \n\tFabien'
print(pets)
print('*' * 20)

# strip function remove whitespace only temporarily. There are rstrip and lstrip for removing right and left whitespace.
movie_name: str = "Scarface  "
movie_name: str = movie_name.strip()

# Prefix can be removed with .removeprefix
mail_client: str = "https://gmail.com"
print("Mail client with prefix ", mail_client)
tkn: str = "https://"
mail_client_without_prefix: str = mail_client.removeprefix(tkn)
print("Mail client without prefix: ", mail_client_without_prefix)
