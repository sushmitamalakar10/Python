# Write a program to store seven fruits in a list entered by the user

fruits = []

for i in range(7):
    fr = input(f"Enter fruit {i}: ")
    fruits.append(fr)


print(fruits)