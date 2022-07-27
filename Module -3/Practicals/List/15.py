#----- Intermediate Assignment -----#

thislist=[]

for i in range(1,6):
    thislist += [i**2]

for i in range(6,26):
    thislist += [i]

for i in range(26,31):
    thislist += [i**2]

print(thislist)