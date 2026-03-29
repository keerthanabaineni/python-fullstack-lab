

# * * * *
# * * * *
# * * * *
# * * * *
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()
# Hollow square
# * * * *
# *     *
# *     *
# * * * *
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==n or i==1 or i==n:
         print("*",end=" ")
        else:
           print(" ",end=" ")
    print()
# * * * * *
# * * * * *
# * * * * *
for i in range(1,n+1):
   for j in range(1,2*n):
      print("*",end=" ")
   print()
# * * * * *
# *       *
# * * * * *
print("rectangular hollow")
for i in range(1,n+1):
    for j in range(1,2*n):
        if j==1 or j==2*n or i==1 or i==2*n or j==2*n-1  or i==n:
         print("*",end=" ")
        else:
           print(" ",end=" ")
    print()

# *
# * *
# * * *
# * * * *
for i in range(1,n+1):
   for j in range(i):
      print("*",end=" ")
   print()
# * * * *
# * * *
# * *
# *
print("inverse right angle")
for i in range(n,0,-1):
   for j in range(i):
      print("*",end=" ")
   print()
# *
# * *
# *   *
# * * * *
print("Hollow right angle: ")
for i in range(1,n+1):
   for j in range(1,i+1):
      if j==1 or j==i or i==n :
       print("*",end=" ")
      else:
         print(" ",end=" ")
   print()
# * * * *
# *   *
# * *
# *
print(" reverse Hollow right angle: ")
for i in range(n,0,-1):
   for j in range(1,i+1):
      if j==1 or j==i or i==n :
       print("*",end=" ")
      else:
         print(" ",end=" ")
   print()
#       *
#     * *
#   * * *
# * * * * 
print(" right angle(right aligned)")

for i in range(1,n+1):
   for k in range(0,n-i):
      print(" ",end=" ")
   for j in range(i):
      print("*" ,end=" ")
   print()


# * * * *
#   * * *
#     * *
#       *
print("reverse right angle(right aligned)")
for i in range(n,0,-1):
   for k in range(0,n-i):
      print(" ",end=" ")
   for j in range(i):
      print("*" ,end=" ")
   print()
#       *
#     * *
#   *   *
# * * * *
print("  hollow right angle(right aligned)")
for i in range(1,n+1):
   for k in range(0,n-i):
      print(" ",end=" ")
   for j in range(1,i+1):
      if j==1 or j== i or i==n :
        print("*" ,end=" ")
      else:
         print(" ",end=" ")
   print()
# * * * *
#   *   *
#     * *
#       *
print(" reverse hollow right angle(right aligned)")
for i in range(n,0,-1):
   for k in range(0,n-i):
      print(" ",end=" ")
   for j in range(1,i+1):
      if j==1 or j== i or i==n :
        print("*" ,end=" ")
      else:
         print(" ",end=" ")
   print()



