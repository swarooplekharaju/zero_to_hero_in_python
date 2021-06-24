"""
when we dont know how many times the loop should iterate we do use the while loop

lets see how the while works with else and break 
when break else will not get executed
when break is not there else will be executed
while loop runs for ever untill the conditon is true
"""

counter = 0

while counter < 3:
    print("Inside while")
    counter = counter + 1
else:
    print("Inside else")

abc=5 

while abc>=0 : 
    print("inside abc while loop",abc)
    abc =  abc-1
    break
else:
    print("else for abc while loop")