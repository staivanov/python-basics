import json
from pathlib import Path

#  10.11-10.12 Favorite number.

filename = 'favorite-number.json'
path = Path(filename)

if path.exists():
    fav_user_number_serialized = path.read_text()
    fav_user_number = json.loads(fav_user_number_serialized)
    print(fav_user_number)
else:
    fav_number = int(input("What is your favorite number? "))
    fav_number_serialized = json.dumps(fav_number)
    path.write_text(fav_number_serialized)
