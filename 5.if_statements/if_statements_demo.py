car_brands: set[str] = {"porsche", "bmw", "mercedes", "audi", "ruf", "opel"}
BMW: str = "bmw"
RUF: str = "ruf"

for car_brand in car_brands:
    if (car_brand == BMW) or (car_brand == RUF):
        print(car_brand.upper())
    else:
        print(car_brand.title())
print("*" * 30)

my_age: int = 36
colleague_age: int = 36
age_to_verify: int = 36
are_we_on_same_age: bool = my_age and colleague_age

if are_we_on_same_age:
    msg_to_all: str = f"\tMy colleague and I are at the same age."
    print(msg_to_all)
print("*" * 30)

person_age_one: int = 15
person_age_two: int = 18
adult_age: int = 18
are_adults: bool = (person_age_one < adult_age) or (person_age_two < adult_age)

if are_adults:
    msg_for_clarification: str = "One or both of them aren't adult."
    print(msg_for_clarification)
print("*" * 30)

# Check if the item is in the list with keyword `in`.
is_bmw_available: bool = BMW in car_brands
msg_for_BMW_availability: str = f"Is BMW in my list of car brands? Result is {is_bmw_available}"
print(msg_for_BMW_availability)

# Check if the item is not in the list.
ford: str = "FORD"
is_ford_available: bool = ford in car_brands
msg_for_ford_availability: str = f"Is FORD in my list of car brands? Result is {is_ford_available}"
print(msg_for_ford_availability)

# Boolean expressions
can_edit: bool = False
is_it_dependable: bool = True
print("*" * 30)

# if-elif-else
print("Welcome to the National Zoological Park")
current_age: int = 21
infant: int = 1
toddler: int = 3
teenager: int = 17
adult: int = 18
max_possible_age: int = 110

if current_age <= infant or current_age <= toddler:
    print("You don't have to pay for entry ticket.")
elif toddler < current_age <= teenager:
    print("Your entry ticket is 5 euro.")
elif adult <= current_age <= max_possible_age:
    print("Your ticket is 8 euro.")
else:
    print("Invalid age.")
