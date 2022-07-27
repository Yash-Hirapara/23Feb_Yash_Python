#---------- Intermediate Assignment ----------#
a=str(input("Enter a String : "))

if len(a)<=2 :
    print("Enter a String More than 2 length.")
elif len(a)>=3:
    if a[-3:]=='ing':
        a+='ly'
        print(a)
    else :
        a+='ing'
        print(a)
