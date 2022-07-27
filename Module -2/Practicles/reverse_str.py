#---------- Intermediate Assignment ----------#

a=str(input("Enter a string : "))

if len(a)%4==0 :
    print(a[::-1])
else :
    print("STring length is not multiple of 4 .")