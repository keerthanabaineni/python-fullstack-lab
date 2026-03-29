# .Write a Python program to calculate and print the sum of elements in each row of a 2D list.
l1=[[1,2,3],[3,4,5]]

for i in range(len(l1)):
    sum=0
    for j in range(len(l1[0])):
        sum+=l1[i][j]
    print(sum)