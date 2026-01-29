# WAP to find whether a given number is prime or not

num = int(input("Enter a num: "))

if num==1:
    print(f"{num} is not a prime number")
    
for i in range(2, num):
    if(num % i) == 0:
        print("Number is not prime")
        break
    
else:
        print("Number is prime")