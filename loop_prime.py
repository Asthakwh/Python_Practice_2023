num = int(input("entrr num:"))
is_prime = True

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

print(f"{num} is prime" if is_prime else f"{num} is not prime")