tupleExample = (1,2,3.0,"Abhishek")
print(tupleExample)

# Tuple doesnt allow reassignment. This will result in TypeError
tupleExample[0] = 1.2

#print second element of tuple
person = ("Rahul", 25, 5.9)
print("{}{}".format("Age: ", person[1]))