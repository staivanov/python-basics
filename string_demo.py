first_name = "stanislav"
last_name = "ivanov"
#f-strings
full_name = f"{first_name} {last_name}"
print(full_name)
name = first_name + " " + last_name
print(name.title())

print("********************")
petName = "Lisa"
print(petName)
print(petName.lower())
print(petName.upper())
print(f"\t{petName.title()}")
print("Pets from last fifteen years: \n\tTomi \n\tLisa \n\tLucky \n\tFabien")
print("********************")
movieName = "Scarface  "
#strip function remove whitespace only temporarily. There are rstrip and lstrip for removing right and left whitespace.
movieName = movieName.strip()
########################################
#Prefix can be removed with .removeprefix
mailClient = "https://gmail.com"
print("Mail client with prefix ", mailClient)
tkn = "https://"
mailClientWithoutPrefix = mailClient.removeprefix(tkn)
print("Mail client without prefix: ", mailClientWithoutPrefix)



