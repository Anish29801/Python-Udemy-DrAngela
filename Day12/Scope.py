
# Global Scope
names = ['John','Taylor','Travis'] # Global scope exists in Python
for name in names:
    print(name)
print("Global Scope names list")

def ListOfNames():
    # Local scope
    names = ['Max','Taylor','Kelvin'] # Local scope exists in Python
    for name in names:
        print(name)
    print("Local Scope names list")
    
ListOfNames()

# No Block scope exists in Python