# Getting the corresponding key to the minimum value from a dictionary
sample = {
    "Physics": 88,
    "Maths": 75,
    "Chemistry": 72,
    "Basic Electrical": 89
}

key_max = max(sample, key=sample.get)
key_min = min(sample, key=sample.get)

print(key_max)
print(key_min)
