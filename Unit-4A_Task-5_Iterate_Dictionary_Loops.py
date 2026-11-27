scores = {"maths": 85, "science": 75, "english": 92}

print("Keys:")
for key in scores:
    print(key)

print("Values:")
for value in scores.values():
    print(value)

print("Items:")
for key, value in scores.items():
    print(key, "→", value)


