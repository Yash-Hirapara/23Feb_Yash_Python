import re
a=input("Enter a String : ")

x=re.sub("[ .,]",":",a)

print(x)