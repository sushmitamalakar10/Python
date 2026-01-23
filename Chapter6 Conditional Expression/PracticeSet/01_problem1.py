# WAP to find the greatest of four numbers entered by user.
a1 = int(input("Enter num 1:"))
a2 = int(input("Enter num 2:"))
a3 = int(input("Enter num 3:"))
a4 = int(input("Enter num 4:"))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is: ", a1)
    
elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is: ", a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is: ", a3)

else:
    print("Greatest number is: ", a4)



num =[]

for i in range(4):
    num.append(int(input(f"Enter number {i+1}: ")))
    
print("Greatest number is: ", max(num))