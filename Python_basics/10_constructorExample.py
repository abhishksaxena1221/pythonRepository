class Calculator:
    num = 100

    # default constructor
    def __init__(self):
        print("Calling the default constructor")

    # parameterised constructor
    def __init__(self, a, b):
        print("Calling the parameterised constructor")
        self.firstNumber = a
        self.secondNumber = b
    
    def summation(self):
        sum = self.firstNumber + self.secondNumber
        print(sum)
     
#obj = Calculator()
obj1 = Calculator(2, 3)
obj1.summation()




