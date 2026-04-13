s="keerthana"
#length of the string
print(len(s))
s = " Learning Python is very easy "
#strip the spacesin the string
print(s.strip())
#strip the left side space 
print(s.lstrip())
#strip the right strip 
print(s.rstrip())
#strip with the some special charcters 
s = "***Python***" 
print(s.strip('*'))
s = "Learning Python is easy" 
#finding the particular word in the string 
print(s.find("Java"))
print(s.index("Python"))
# -1
# Traceback (most recent call last):
#   File "d:\10000 coders\assignments\stringbuiltinfun.py", line 17, in <module>
#     print(s.index("Java"))
# ValueError: substring not found
#to find the ;ast occurance of the word in the string 
print(s.rfind("Python"))
#count the occurances 
s = "Python python PyThon" 
print(s.count("Python")) # it will be case sesitive count 
s = "Python is easy. Python is powerful."
print(s.replace('Python','Java'))
print(s.replace('Python' ,'Java',1))
s = "Python is very easy"
#split the space 
print(s.split())
#split with some charcter 
s = "Python, Java c"
print(s.split(','))











