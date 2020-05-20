# Removing all even numbers from a list and saving those in another list
List1 = [69, 57, 78, 10, 45]
even = []
odd = []
for num in List1:
    print(num)
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(odd)
print(even)



