# Creating a simple calculator
def calculator(a, b, n):
    if n == 1:
        return a + b
    elif n == 2:
        return a - b
    elif n == 3:
        return a * b
    elif n == 4:
        return a / b
    else:
        print("Invalid input")


x = float(input("Enter a number: "))
y = float((input("Enter another number: ")))
m = int((input("Enter 1 for addition, 2 for subtraction, 3 for multiplication or 4 for division: ")))

s = calculator(x, y, m)
print("result =", s)