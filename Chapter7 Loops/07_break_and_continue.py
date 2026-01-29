# for i in range(100):
#     if(i==50):
#         break # Exit the loop right now
#     print(i)
    

# i = 0
# while(i<100):
#     print(i)
#     if(i==50):
#         break
#     i += 1
    
for i in range(100):
    if(i==30):
        break # exit the loop right now
    print(i)
    

for i in range(100):
    if(i==30):
        continue # skip this iteration
    print(i)
    
for i in range(4):
    print("Printing")
    if i == 2: # if i is 2, the iteration is skipped
        continue
    print(i)