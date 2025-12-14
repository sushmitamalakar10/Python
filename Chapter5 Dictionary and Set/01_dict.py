# Empty dictionary
d = {}
print(d)

# Using dict
d = dict(name = "Sushmita", age = 23)
print(d)

# from list of tuples
d = dict([("a", 1), ("b", 2)])
print(d)

marks = {
    "Ram" : 100,
    "Hari" : 30,
    "list" : [12, 20]
}

print(marks)
print(type(marks))

# accessing the values
print(marks["Ram"], marks["list"])

# dictionary is mutable

marks["Ram"] = 20
print(marks["Ram"])

# Adding elements
marks["Shyam"] = 40
print(marks)
