
list1=[[1,2,3],[4,5,6],[7,8,9]]
print("Before")
for i in list1:
    print(i)
for i in range(len(list1)):
    for j in range(i,len(list1[0])):
        list1[i][j], list1[j][i] = list1[j][i], list1[i][j]
print("After")
for i in list1:
    print(i)
       