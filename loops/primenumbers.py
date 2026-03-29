n=int(input("enter a number"))
for i in range(2,n):
    isprime=True
    for j in range(2,i):
        if i%j==0:
            isprime=False
            break
    if(isprime):
     print(i)
        
