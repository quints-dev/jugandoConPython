myString = "This is a string."
print(myString)

print(type(myString))
print(myString + " is of the data type " + str(type(myString)) + "\n")


firstString = 1.3
secondString = "2.1"
thirdString = firstString + float(secondString)
print(thirdString, "\n")

name = input("Whats you name")
print(name, "\n")

color = input("what's your favorite color")
animal = input("what's your favorite animal")
print("{}, you like a {} {}!".format(name,color,animal))

