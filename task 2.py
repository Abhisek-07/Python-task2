# Sorting a string so that all lowercase letters come before all uppercase letters

string = input("Enter a string: ")
lower = []
upper = []
for letter in string:
    if letter.islower():
        lower.append(letter)
    else:
        upper.append(letter)


sorted_string = "".join(lower + upper)
print(sorted_string)




