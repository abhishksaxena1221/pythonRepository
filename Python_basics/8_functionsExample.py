# simple method
def greetMe():
    print("Good morning!")

# method with String parameter
def greetMe(name):
    print("Good morning! " + name)

# method with integer parameters
def addIntegers(a,b):
    print("{}{}".format("Sum of integers is: ", a+b))


greetMe()
greetMe("Abhishek")
addIntegers(5,6)