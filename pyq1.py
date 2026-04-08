import math

def perfect_square(number):
    # Calculate the integer square root
    root = int(math.sqrt(number))
    
    # Check if square of the root is equal to the number
    if root * root == number:
        return number
    else:
        return -1
    
    # Example usage
print(perfect_square(1))  # Output: 1
print(perfect_square(2))  # Output: -1
print(perfect_square(16)) # Output: 16
print(perfect_square(20)) # Output: -1