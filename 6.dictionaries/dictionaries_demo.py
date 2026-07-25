#1. Start with an empty dictionary
car_0 = {}

#2. Adding items.
car_0["brand"] = "Porsche"
car_0["model"] = "Panamera"
car_0["engine_type"] = "Petrol - Twin Turbo"
car_0["kW"] = 600
car_0["color"] = "black"

#3. Print every key-value pair in the dictionary.
for spec in car_0:
    print(f"{spec}: {car_0[spec]}")

#4. Remocing key-value pari
del car_0["color"]

#5. It's an error if I try to access not existing element in a dictionary.
#print(car_0["coupe_type]"). Method .get() is an easy solution for this problem.
coupe_type = car_0.get("coupe_type", "There is not suck key.")
print(coupe_type)



