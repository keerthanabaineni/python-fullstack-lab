# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
print("repeating numbers")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
# 1
# 2 3
# 4 5 6
# 7 8 9 10
print("continous number traingle")
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
print("reverse num traingle")
for i in range(1,n):
    for j in range(i,0,-1):
        print(j,end=" ")
    
    print()
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
print("inverted number traingle")
for i in range(1,n):
    for j in range(n-i,0,-1):
        print(j,end=" ")
    print()
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5
print("Right aligned right angle traingle")
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()
#       1
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1
# n=4
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
       
    print() 
# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10
print("even number traingle")
for i in range(1,n+1):
    num=2
    for j in range(i):
        print(num,end=" ")
        num+=2
    print()
# 1
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9
print("odd number traingle")

for i in range(1,n+1):
    num=1
    for j in range(i):
        print(num,end=" ")
        num+=2
    print()
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

print("pascal traingle")
for i in range(n):
    val=1
    for j in range(i+1):
        print(val,end=" ")
        val=(val)*(i-j)//(j+1)
    print()
