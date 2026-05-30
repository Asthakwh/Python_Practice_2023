squares = [x**2 for x in range(1, 6)]
for i in range(len(squares)):
    if i == 3:
        break
print(squares)  # Output: [1, 4, 9, 16, 25]
