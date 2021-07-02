"""
in this chapter we learn the uses of for with else and break

break plays a major role :
if break is given else part is not executed 
so in the first example else part is executed 
in the second example else part is not ececuted 
even if you remove break and condition is executed the last part will execute

"""

for i in range(4):
    print(i)
else:
    print("end  of the for loop")


names =["heena","sheela","preethi"]

for i in names:
    if i=="heena":
        print("name found")
        break
else :
    print("no name is found")

# lets have a final test 
#lets have a plain for loop with break and else and see the output 


for i in range(5):
    print(i)
    break
else:
    print("end of for with break")