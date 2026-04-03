

#       *
#     * * *
#   * * * * *
# * * * * * * *
n=4
for i in range(1,n+1):
    for k in range(0,n-i):
        print(" ",end=" ")
    for j in range(0,2*i-1):
        print("*",end=" ")
    print()

# Diamond Pattern
#     *
#   * * *
# * * * * *
#   * * *
#     *
print("Diamond pattern: ")
for i in range(1,n+1):
    for k in range(0,n-i):
        print(" ",end=" ")
    for j in range(0,2*i-1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for k in range(0,n-i):
        print(" ",end=" ")
    for j in range(0,2*i-1):
        print("*",end=" ")
    print()  
# Left-Aligned Half Diamond
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
n = 4

for i in range(1, 2*n):
    
    if i <= n:
        for j in range(i):
            print("*", end=" ")
    else:
        for j in range(2*n - i):
            print("*", end=" ")
    
    print()
#       *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *
for i in range(1, 2*n):
   
    if i <= n:
        for k in range(0,n-i):
         print(" ",end=" ")
        for j in range(i):
            print("*", end=" ")
    else:
       for s in range(i-n):
           print(" ",end=" ")
       for j in range(2*n - i):
            print("*", end=" ")
    print()
# Sandglass Pattern
# n=4
# * * * *
#   * * *
#     * *
#       *
#     * *
#   * * *
# * * * *
print("sandglass pattern")
n = 4

for i in range(n, 0, -1):
    for s in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(2, n+1):
    for s in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
#     Increasing Width Triangle

# *
# * *
# * * *
# * * * *
# * * * * *
n=5
print("increase width rectangle")
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
print("Hollow patterns: ")
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(0,2*i-1):
        if j==0 or j==2*i-2 or i==n: 
           print("*",end=" ")
        else: print(" ",end=" ")
    print()

# Hollow Diamond Pattern
# Input: n = 3
# Output:
#     *
#   *   *
# *       *
#   *   *
#     *
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(0,2*i-1):
        if j==0 or j==2*i-2:
         print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n-1,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(0,2*i-1):
        if j==0 or j==2*i-2:
         print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# Hollow Butterfly Pattern
# Input: n = 4
# Output:
# *       *
# * *   * *
# *   *   *
# *       *
# *   *   *
# * *   * *
# *       *
n = 4

# Upper half
for i in range(1, n+1):
    # Left wing
    for j in range(i):
        if j == 0 or j == i-1:
            print("*", end="")
        else:
            print(" ", end="")
    
    # Spaces
    for j in range(2*(n-i)):
        print(" ", end="")
    
    # Right wing
    for j in range(i):
        if j == 0 or j == i-1:
            print("*", end="")
        else:
            print(" ", end="")
    
    print()

# Lower half
for i in range(n, 0, -1):
    # Left wing
    for j in range(i):
        if j == 0 or j == i-1:
            print("*", end="")
        else:
            print(" ", end="")
    
    # Spaces
    for j in range(2*(n-i)):
        print(" ", end="")
    
    # Right wing
    for j in range(i):
        if j == 0 or j == i-1:
            print("*", end="")
        else:
            print(" ", end="")
    
    print()
# Hollow Hourglass Pattern
# Input: n = 5
# Output:
# * * * * *
# *       *
#   *   *
#     *
#   *   *
# *       *
# * * * * *
print("Hollow glass pattern: ")
for i in range(n,0,-1):
    for k in range(n-i):
        print(" ", end=" ")
    for j in range(0,2*i-1):
        if j==0 or i==n or j==2*i-2:
         print("*",end=" ")
        else:
           print(" ",end=" ")
    print()
for i in range(2,n+1):
    for k in range(n-i):
        print(" ", end=" ")
    for j in range(0,2*i-1):
        if j==0 or i==n or j==2*i-2:
         print("*",end=" ")
        else:
           print(" ",end=" ")
    print()
