
x = 1

def change():
    # using a global keyword
    global x
    # increment value of x by 5
    x = x + 5
    print("Value of x inside a function:", x)

change()

