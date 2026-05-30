# Print each element of the list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)



# Print numbers from 1 to 5
for i in range(1, 50):
    print(i)

# Print numbers from 1 to 5 using while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# Skip number 3 in the loop
for i in range(10, 60):
    if i == 3:
        continue
    print(i)


# Print a 3x3 grid of *
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
