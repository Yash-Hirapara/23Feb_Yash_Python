#---------- Basic Assignment ----------#

a=input("Enter Value : ")

if a.isdigit():
    print("Its Imteger")
elif a.isalpha():
    print("Its String")
else :
    print("Neither Int nor String")