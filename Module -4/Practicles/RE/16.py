import re
a=input("Enter a String : ")

x=re.findall("[\w\d]",a)

str=""
str1=str.join(x)

print(str1)