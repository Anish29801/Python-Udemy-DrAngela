class BandNameGenerator:
    # Create a constructor
    def __init__(self):
        print("Welcome to Bandname Generator.")
# Creating a new function
    def Generator (city,pet):
        return str(city +'' + pet) # String concatenation
       
# Asking user for information
# Asking user for city name
myCity = str(input('What is the city you grew up?'))

# Asking user for pet name
myPet = str(input('What is the pet your pet nome?'))

#Creating a new instance of the class
obj = BandNameGenerator
#calling function via object
print ("Your band name could be: "+ obj.Generator(myCity,myPet))