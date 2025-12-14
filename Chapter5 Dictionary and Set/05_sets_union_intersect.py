s1 = {1, 5, 6}
s2 = {7, 9, 1, 10}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))


# Subset and superset

A = {1, 2, 3, 4}
B = {2, 3}

print(B.issubset(A)) # True
print(A.issubset(B)) # False

print(A.issuperset(B)) # True
print(B.issuperset(A)) # False