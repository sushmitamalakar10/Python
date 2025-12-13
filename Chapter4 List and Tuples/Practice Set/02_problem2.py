# Write a program to accept marks of 6 students and display them in a sorted manner

marks = []

for i in range(6):
    m = int(input(f"Enter marks of {i} student: "))
    marks.append(m)
    
print(f"Marks: {marks}")

marks.sort()

print(f"Sorted marks: {marks} ")

