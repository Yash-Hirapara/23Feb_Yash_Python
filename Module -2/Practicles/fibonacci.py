#---------- Basic Assignment ----------#

a=int(input("Enter how many No. want to print : "))
n1=0
n2=1
cout=0

if a <= 0 :
    print("Please enter positive Integer.")
elif a==1:
    print(f"Fibonacci sequence upto {a} is : {n1}")
else :
    print("Fibonacci Sequence : ")
    while cout < a :
        print(n1)
        nth=n1+n2

        #to update values
        n1=n2
        n2=nth
        cout += 1