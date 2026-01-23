a = int(input("Enter your age:"))

# If statement 1
if(a%2 ==0):
    print("a is even")


# If statement 2

# if elif else ladder
if(a>=18):
    print("You are above the age of consent")
    
elif(a<0):
    print("Age can't be less than 0)!")

elif(a==0):
    print("Invalid age")
    
else:
    print("You are below the age of consent")
    
print("end of program")