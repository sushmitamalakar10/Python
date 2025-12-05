import os
directory = 'e:/Python/Chapter1/'

contents = os.listdir(directory)

for item in contents:
    print(item)