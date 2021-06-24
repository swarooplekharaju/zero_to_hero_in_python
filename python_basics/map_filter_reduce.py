"""
map takes input function or functions and applies sequentially
"""
list1=[1,2,3,4]
f1= lambda x : x**2
f2 = lambda x : x**3
# lambdas in a variable 
# passing the list to the variable using maps 
f2(list1)