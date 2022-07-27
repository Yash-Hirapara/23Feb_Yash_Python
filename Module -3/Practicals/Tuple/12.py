#----- Intermediate Assignment -----#

'''
for this solution we have to create some tuples in one list
then we have to replace last value of all the tuple in the list
'''

#----- SOLUTION -----#

thislist=[(1,2,3,4,5),(1,2,3,4,5),(1,2,3,4,5),(1,2,3,4,5)]
print([t[:-1]+(9,)for t in thislist])