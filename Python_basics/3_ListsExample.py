# creating a simple list and printing values
values = [1,2.0,"Abhishek"]
print(values[2])
print(values[-1])
print(values[0:3])


# inserting value in list
values.insert(3,"Saxena")
print(values)
values.append(" is learning python")
print(values)
values[2] = "ABHISHEK"
print(values)

# deleting values from a list
del values[0]
print(values)


# Example of list program - # printing first and last fruit from the list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# printing first and last fruit from the list
print("First fruit: "+fruits[0])
print("Last fruit: "+fruits[-1])

# print second and third fruit from the list
print("{}{}".format("Fruits from index 1 to 2: ", fruits[1:3]))

