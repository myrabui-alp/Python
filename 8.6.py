# Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
newDict = sample_dict
for x in keys:   
    sample_dict.pop(x)

print(sample_dict)
