def removenth(s, n):
    if n >= len(s):
        return s
    return s[:n] + s[n+1:]

print(removenth("MANGO", 1))  # Output: MNGO
print(removenth("MANGO", 3))  # Output: MANO
print(removenth("MANGO", 10)) # Output: MANGO (index out of range)
