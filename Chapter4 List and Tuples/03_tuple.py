a = (1, 2, 3, 4, False, "Ram")
print(type(a)) # <class 'tuple'>

b = (1)
print(type(b)) # <class 'int'>

b = (1,)
print(type(b)) # <class 'tuple'>

a[0] = 100 # tuples are immutable
print(a)