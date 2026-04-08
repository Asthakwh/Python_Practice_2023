# Step 1: Write sample content to a file (if file doesn't exist)
with open("hello.txt", "w") as file:
    file.write("Hello!!")

# Step 2: Read the content of the file
with open("hello.txt", "r") as file:
    content = file.read()

# Step 3: Add comma between each character
content = ",".join(content)

# Step 4: Write the modified content to a new file
with open("output.txt", "w") as file:
    file.write(content)

# Step 5: Print success message
print("File content processed and saved to: output.txt")
