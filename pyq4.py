L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#1. Return a list of numbers starting from the last to second item of the list
print(L[::-1][0:-1])
# OR simply:
print(L[-1:0:-1])

#2. Return a list that starts from 3rd item to second last item
print(L[2:-1])

#3. Return a list that has only even position elements of list L to list M
M = L[1::2]
print(M)

#4. Return a list that starts from the middle of the list L
middle = len(L) // 2
print(L[middle:])

#5. Return a list that reverses all elements from index 0 to middle index only
middle = len(L) // 2
print(L[middle::-1])
