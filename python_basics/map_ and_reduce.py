"""
map is for any single operations applied on all the list
eg like square , cubes , additions and subrations
one application on the all values

filter is like applying a single condition to the list
and return the true cases

reduce is like apply the operation like addition/subration
"""
import functools
import operator
list_numbers = [1,2,3,4]
#filter for conditional returns
print([x  for x in list_numbers if x>2])
print(list(filter(lambda x:x >2,list_numbers)))
print(list(map(lambda x:x >2,list_numbers)))
print(functools.reduce(lambda x,y :x+y,list_numbers))
# for working on multiple lists , map is the best option
# mathematical expressions
list2,list3 =[3,4],[4,5]
print(list(map(operator.add,list2,list3)))
