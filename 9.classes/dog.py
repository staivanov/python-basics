class Dog:
   def __init__(self, name, age, gender):
       """Initialize name, age and gender attributes."""
       self.name = name
       self.age = age
       self.gender = gender

   def sit(self):
      """A dog is sitting after invocation of this method."""
      print(f"{self.name} is now sitting.")

   def present_myself(self):
    """The dog is presenting himself."""
    print(f"My name is {self.name}. I am {self.age} years old. My gender is {self.gender}.")