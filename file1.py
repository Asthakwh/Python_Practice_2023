#file = open("demo.txt", "r")
#content = file.read()
#print(content)
#file.close()


#with open("demo.txt", "w") as file:
 #   file.write("Hello, World!")


file = open("demo.txt", "r")
content = file.readline() # only first line also we can use readlines() foe all line

print(content)
file.close()
