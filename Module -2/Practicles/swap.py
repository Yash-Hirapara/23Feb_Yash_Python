#---------- Intermediate Assignment ----------#

a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))

#using temp var
c=a
a=b
b=c

print("\nValue is Swapped..... ")
print("\nNow First Number is : ",a)
print("Now Second Number is : ",b)

#without temp var
x=int(input("\nEnter First Number : "))
y=int(input("Enter Second Number : "))

x=x+y
y=x-y
x=x-y

print("\nValue is Swapped..... ")
print("\nNow First Number is : ",x)
print("Now Second Number is : ",y)