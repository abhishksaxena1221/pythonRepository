dictionary_example = {"Name":"Abhishek", "Company": "XYZ", "Country":"India"}

# print whole dictionary
print(dictionary_example)

# print specific key
print(dictionary_example["Name"])

# print value by key
print(dictionary_example.get("Company"))

# creating dictionary dynamically on runtime
dict1 = {} # empty dictionary
dict1[1] = "Noida"
dict1[2] = "Gurgaon"
print(dict1)

# example of dictionay
car = {"make":"Toyota","model":"Camry","year":2020,"color":"Blue"}
print("Car model: "+car["model"])
car["owner"]="Abhishek"
print("{}{}".format("Updated car dictionary: ",car))



