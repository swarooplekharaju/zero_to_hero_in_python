"""
filter takes a contional function and list
returns the elements where the condtion met is true

"""

# lets see the list comprehension
#list comprehension also uses the same stragey
#[return value , loop/iterable if condition ]
list1=[1,2,3,4]
list_comprehension =[x for x in list1 if x>3 ]
print(list_comprehension)
# let us write the same using the filter
print(list(filter(lambda x:x>3,list1)))