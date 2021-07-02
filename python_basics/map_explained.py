"""
map takes input function or functions and applies sequentially
"""
#understanding basic lambda 
#simple lambda function to return cube root 
x= lambda x: x**3
import functools
# calling the lambda function 
print(x(3))
square_root = lambda x:x**2
cube_root = lambda x:x**3
print(square_root(2))
print(cube_root(3))
list_primes =[1,3,5,7,11]
#passing list and function
print(list(map(square_root,list_primes)))
funcs=[square_root,cube_root]
for i in list_primes:
    print(list(map(lambda x:x(i),funcs)))

