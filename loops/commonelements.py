# Write a Python program to find and print all common elements between two lists using nested loops.
l1=[1,2,3,4]
l2=[3,4,5,6]
res=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        if(l1[i]==l2[j]):
         res.append(l2[j])
for i in res:
    print(i)
