# Step 1: Read from Input.txt
with open('Input.txt', 'r') as infile:
    lines = infile.readlines()

# Step 2: Prepare output files
odd_file = open('ODD.txt', 'w')
even_file = open('EVEN.txt', 'w')

# Step 3: Process each line
for line in lines:
    try:
        number = int(line.strip())  # Convert line to integer
        if number % 2 == 0:
            even_file.write(str(number) + '\n')
        else:
            odd_file.write(str(number) + '\n')
    except ValueError:
        pass  # Ignore lines that are not valid integers

# Step 4: Close the output files
odd_file.close()
even_file.close()
