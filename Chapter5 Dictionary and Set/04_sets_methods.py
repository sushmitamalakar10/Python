s = {1, 2, 5 ,6}
s.add("Sushmita") # adds single element


print(s)

new_set = s.copy()
print(new_set)

s.remove(2)
print(s)

s.update([50,8]) # adds multiple elements
print(s)

print(len(s))