# write a program to input eight numbers from the user and display all the unique numbers(once).

s = set()

for i in range(8):
    n = int(input(f"Enter no. {i+1}: " ))
    s.add(n)

print(s)