my_list = [2, 3, 5, 7, 11]
squared_list = [x**2 for x in my_list]
print(squared_list)

#condition filtering operation on entire list
squared_dict = { x:x**2 for x in my_list if x%2 !=0}
print(squared_dict)