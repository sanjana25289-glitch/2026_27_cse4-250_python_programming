numbers = range(1, 10)

squares = [x * x for x in numbers]
evens = [x for x in numbers if x % 2 == 0]

print("Squares:", squares)
print("Evens:", evens)


