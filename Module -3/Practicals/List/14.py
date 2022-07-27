#----- Intermediate Assignment -----#

from unittest import result


list1=[1,2,3,4,5,6,7,8,9,0]
list2=[1,2,3,4,5,6,7,8,9,0]

for element in list1 :
    if element in list2:
        result = True
    else:
        result = False
print(result)
