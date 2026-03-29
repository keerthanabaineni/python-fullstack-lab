# Write a Python program to add two 2D lists (matrices) element by element using nested loops.
list1=[[1,2,3],[3,4,5]]
list2=[[6,7,8],[8,9,10]]
result=[[0,0,0],[0,0,0]]
for i in range(len(list1)):
    for j in range(len(list1[0])):
        result[i][j]=list1[i][j]+list2[i][j]
for i in result:
    print(i)
