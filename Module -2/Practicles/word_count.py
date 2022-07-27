#---------- Basic Assignment ----------#

a="This is Python Program , Welcome to the Python"
word='Python'
list=[]
wordcount=0
list=a.split(" ")
for i in range (0,len(list)):
    if word==list[i]:
        wordcount=wordcount+1
print("Number of word found in a string : ")
print(wordcount)