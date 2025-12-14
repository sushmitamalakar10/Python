# create an empty dictionary. Allow 4 friends to enter their favourite language as value and use key as their names. assume that the names are unique
# if the names of 2 friends are same; what will happen to the program.
# if hte languages of 2 friends are same; what will happen to the program.

friends_lang = {}

for i in range(4):
    name = input("Enter name: ")
    lang = input("Enter language: ")
    
    friends_lang[name] = lang

print(friends_lang)
    
    