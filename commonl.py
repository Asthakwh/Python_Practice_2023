# Take input from user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Convert to sets to find common letters
common = set(str1) & set(str2)

# Remove spaces and show results
print("The common letters are:")
for ch in common:
    if ch != " ":
        print(ch)
