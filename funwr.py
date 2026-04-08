#with open("demo.txt", "w") as f:
 #   f.write("Hello AKTU Students\n")
#    f.write("Python is easy!")
#lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
#with open("demo.txt", "w") as f:
#    f.writelines(lines)

with open("demo.txt", "r") as f:
    f.seek(6)  # Move pointer to 6th byte
    print(f.read())  # Reads from 6th byte to end
