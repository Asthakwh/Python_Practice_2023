num1 = int(input("enter 1 value"))
num2 = int(input("enter 2 value"))
opr = input("enter the operator")
if opr == "+":
    print(num1 + num2)
elif opr == "-":  
    print(num1 - num2)
elif opr == "*":
    print(num1 * num2)
elif opr == "/":       
    print(num1 / num2)
else:
    print("invalid")