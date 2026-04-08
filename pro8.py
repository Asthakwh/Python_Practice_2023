#scope resolution
temp =10
def func():
    temp=20
    print(temp)

print(temp)
func()
print(temp)


mul = lambda a, b : a*b
print(mul(6, 7))

def myWrapper(n):
    return lambda a: a*n
mulFive =myWrapper(7)
print(mulFive(6))