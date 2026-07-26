car_brands = {"porsche", "bmw", "mercedes", "audi", "ruf", "opel"}
BMW = "bmw"
RUF = "ruf"

for car_brand in car_brands:
    if (car_brand == BMW) or (car_brand == RUF):
        print(car_brand.upper())
    else:
        print(car_brand.title())
print("*****************************************")

my_age = 36
colleague_age = 36
age_to_verify = 36
if my_age and colleague_age:
    print("\tMy colleague and I are at the same age.")
print("*****************************************")

person_age_one = 15
person_age_two = 18
adult_age = 18

if (person_age_one < adult_age) or (person_age_two < adult_age):
    print("One of them is not at or above the adult age.")
print("*****************************************")
# Check if the item is in the list with keyword `in`.
is_bmw_available = BMW in car_brands
print("Is BMW in my list of car brands? Result is .... ", is_bmw_available)
# Check if the item is not in the list.
ford = "FORD"
is_ford_available = ford in car_brands
print("Is FORD in my list of car brands? Result is .... ", is_ford_available)

# Boolean expressions
can_edit = False
is_it_dependable = True
print("*****************************************")

# if-elif-else
print("Welcome to the National Zoological Park")
current_age = 21
infant = 1
toddler = 3
teenager = 17
adult = 18
max_possible_age = 110

if current_age <= infant or current_age <= toddler:
    print("You don't have to pay for entry ticket.")
elif toddler < current_age <= teenager:
    print("Your entry ticket is 5 euro.")
elif adult <= current_age <= max_possible_age:
    print("Your ticket is 8 euro.")
else:
    print("Invalid age.")
