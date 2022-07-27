#----- Intermediate Assignment -----#

thislist=[1,2,2,3,4,55,56,7,9,97,99,97,55]
newlist=[]

for x in thislist:
    if x not in newlist :
        newlist.append(x)
print(newlist)