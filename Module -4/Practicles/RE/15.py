import re
a=input("Enter a String : ")

x=re.findall("\S",a)

# converting list into string here to see the result properly
str=""
str1=str.join(x)


print("String Without White space is : ",str1)