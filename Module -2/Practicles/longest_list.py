#---------- Intermediate Assignment ----------#

a=['Apple','Mango','Kiwi','Strawberry','Guava']

lenstr= len(a[0])
temp= a[0]

for i in a:
    if len(i) > lenstr :
        lenstr = len(i)
        temp = i

print(f"The Word With Longest Length Is : {temp}")