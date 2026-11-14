# 1. List of cars demo.
famous_car_brands: list[str] = ["Porsche", "BMW", "Audi", "Mercedes", "VW", "Opel", "RUF", "Peugeot", "Renault",
                                "Citroen", "Jaguar"]
print("All car brands in my list are: ", famous_car_brands)
print('*' * 30)

my_fav_car_brand: str = famous_car_brands[0]  # Returns the first element from the list.
print("My favorite car brand is", my_fav_car_brand)
print('*' * 30)

last_car_brand: str = famous_car_brands[-1]  # Returns the last element from the list.
print("The last car brand is: ", last_car_brand)
print('*' * 30)

message_to_all_bmw_fans: str = f"I like very much {famous_car_brands[1]}"
print(message_to_all_bmw_fans)
print('*' * 30)
# 2. CRUD over the list.
famous_car_brands[-1]: str = "Range Rover"
print("All car brands in my list are: ", famous_car_brands)
english_car_brand: str = "Jaguar"
famous_car_brands.append(english_car_brand)

famous_american_car_brand: str = "FORD"
luxury_american_car_brand: str = "Cadillac"
famous_car_brands.insert(7, famous_american_car_brand)
famous_car_brands.insert(8, luxury_american_car_brand)
print("All car brands in my list now are: ", famous_car_brands)

# del keyword
del famous_car_brands[-1]
del famous_car_brands[-1]
print("All car brands in my list now are: ", famous_car_brands)
last_french_car_brand = famous_car_brands.pop()
print("Last french brand in my list of car brands is", last_french_car_brand)
print('*' * 30)

# Removing with pop() function from the list by providing index.
motorcycles: list[str] = ["Honda", "Kawasaki", "Suzuki", "BMW", "Yamaha"]
top_brand_motorcycle: str = motorcycles.pop(0)
sold_number: float | int = 20.2
print("Top sold motorcycle brand for 2025 is", top_brand_motorcycle, "with", sold_number, "millions unit.")
# removing with remove() function by value from the list
yamaha: str = "yamaha"
motorcycles.remove(yamaha.title())
print(f"Current list of motorcycles brands. {motorcycles}")
print('*' * 30)

# 3. Organizing a list.
rock_bands: list[str] = ["The Rolling Stones", "Led Zeppelin", "Queen", "Deep Purple", "Pink Floyd"]
rock_bands.sort()
print("Rock bands in my list are sorted now.", rock_bands)
rock_bands.sort(reverse=True)
print("Rock bands in my list are in reverse order now.", rock_bands)

# 4. Sorting the list temporarily.
sorted(rock_bands)
# Reversing a list from n-th to 0 element.
rock_bands.reverse()
print("Reverse order of a list", rock_bands)
rock_bands_len: int = len(rock_bands)
print("Length of rock bands list is", rock_bands_len)
