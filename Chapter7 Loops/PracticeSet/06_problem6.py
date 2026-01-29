# factorial of given number using for loop

n = int(input("Enter a number to find the factorial: "))
product = 1

for i in range(1,n+1):
    product = product * i
print(f"Factorial of {n} is {product}")