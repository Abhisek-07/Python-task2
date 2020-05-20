# Addition of two numbers and 5 to their sum using inner and outer function

def nums(a, b):

    def add(x, y):
        sum = x + y
        return sum
    s = add(a, b)
    return s + 5


result = nums(6, 10)
print(result)
