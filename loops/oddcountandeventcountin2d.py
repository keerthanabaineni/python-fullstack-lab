list1=[[1,2,3],[3,4,5]]
list2=[[6,7,8],[8,9,10]]
oddcount=0
evencount=0
for i in range(len(list1)):
    for j in range(len(list1[0])):
        if list1[i][j]%2==0:
            evencount+=1
        else:
            oddcount+=1
print("oddcount:",oddcount)
print("evencount:",evencount)

