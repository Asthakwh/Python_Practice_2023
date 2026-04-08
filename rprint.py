def rprint(lst):
    if len(lst) == 0:
        return  # Base case: empty list does nothing
    print(lst[-1], end=" ")  # Print the last element
    rprint(lst[:-1])         # Recursive call with remaining list

rprint([])           # Output: (nothing)
rprint([1, 2, 3])    # Output: 3 2 1
