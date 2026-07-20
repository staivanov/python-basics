# 2.3. Personal message
name = "Larry"
greeting = f"Hello, {name}, do you want a coffee?"
print(greeting)

# 2.4 Name cases
name = "tom"
print(name.title())
print(name.upper())
print(name.lower())

# 2.5-6 Famous quote
author = "General George S. Patton Jr."
famous_quote = "\"May God have mercy upon my enemies, because I won't!\""
message_to_all_readers = f"{author} once said: {famous_quote}"
print(message_to_all_readers)

# 2.7 Stripping names
name_with_whitespace = "\tGeneral George S. Patton Jr.   "
print(name_with_whitespace)
print(name_with_whitespace.strip())

# 2.8 File extension
full_file_name = "notes.docs"
print(full_file_name)
file_extension = ".docs"
print(file_extension)
file_name = full_file_name.removesuffix(file_extension)
print(file_name)
