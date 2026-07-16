first_name = "stanislav"
last_name = "ivanov"
#f-strings
full_name = f"{first_name} {last_name}"
print(full_name)
name = first_name + " " + last_name
print(name.title())

print("********************")
pet_name = "Lisa"
print(pet_name)
print(pet_name.lower())
print(pet_name.upper())
print(f"\t{pet_name.title()}")
print("Pets from last fifteen years: \n\tTomi \n\tLisa \n\tLucky \n\tFabien")
print("********************")
movie_name = "Scarface  "
#strip function remove whitespace only temporarily. There are rstrip and lstrip for removing right and left whitespace.
movie_name = movie_name.strip()
########################################
#Prefix can be removed with .removeprefix
mail_client = "https://gmail.com"
print("Mail client with prefix ", mail_client)
tkn = "https://"
mail_client_without_prefix = mail_client.removeprefix(tkn)
print("Mail client without prefix: ", mail_client_without_prefix)



