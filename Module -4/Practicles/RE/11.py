import re

a=input("Enter a string : ")
us_pattern="[a-z]+[_]+[a-z]"

x=re.findall(us_pattern,a)

if x:
    print("Pattern Matches")
else :
    print("Error")