# keys()	Returns all keys
# values()	Returns all values
# items()	Returns key-value pairs
# get()	Safe access
# update()	Add/update multiple
# pop()	Remove key
# clear()	Remove all

marks = {
    "Ram" : 100,
    "Hari" : 30,
    "list" : [12, 20]
}

print(marks.keys())
print(marks.values())
print(marks.items())

marks.update({"Ram" : 99, "Sushmita" : 45})
print(marks)

# print(marks.get("Sush")) # prints None
# print(marks["Sush"]) # returns an error

marks.pop("list")
print(marks)