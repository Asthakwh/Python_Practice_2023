# add 2 integers without using +operator

def add_num(num1, num2):
    while num2 !=0:
        data = num1 & num2
        num1 = num1^num2
        num2 = data<<1
    return num1
print (add_num(2,10))    
    