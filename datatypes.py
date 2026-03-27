import math
#check even or odd 
num =int(input("Enter a number:"))
def evenorodd(num):
 if num%2==0:
    print("it is even")
 else:
    print("it is odd")
evenorodd(num)
#divisible by 5 not by 10
def divby5notby10(num):
  if num%5==0 and num%10!=0:
    print("satisfy")
  else:
    print("not satisfy")
divby5notby10(num)
#biggest among two numbers 
num1 =int(input("enter number1: "))
num2=int(input("enter a number2: "))
def bigandsmall(num1,num2):
  if(num1>num2):
    print( num1," is greater")
  else: 
    print( num2 ," is greater")
  if(num1<num2):
    print( num1," is smaller")
  else: 
     print( num2 ," is smaller")
bigandsmall(num1,num2)

#divisible by 2 and 3 and 6
def check236(num):
  if num%2==0 and num%3==0 and num%6==0:
    print("satisfy")
  else:
    print("not satisfy")
#checking the age eligibility
age=int(input("enter your age"))
def elegibilty(age):
  if(age>18):
    print("Eligible to vote")
  else:
    print("Not eligible to vote")
elegibilty(age)
#students pass or fail on all subjects

math_marks=int(input("enter your  math marks"))
physics_marks=int(input("enter your physics marks"))
chem_marks=int(input("enter your chemistry marks"))
if math_marks and physics_marks and chem_marks>=35:
  print(" all pass")
 # if student passed the two subjects 
if math_marks or physics_marks or chem_marks>=35:
  print("pass")
if math_marks>=35 and physics_marks>=35:
  print("pass two subjects")
if physics_marks>=35 and chem_marks>=35:
  print("pass two subjects")
if chem_marks>=35 and math_marks>=35:
  print("pass two subjects")
#Biggest among three numbers 
a = int(input("enter a first num"))
b= int(input("enter a second num"))
c = int(input("enter a third num"))
if a>b and a>c:
  print(a,"is big")
elif b>c and b>a:
  print(b,"is big")
else :
  print(c,"is big")
#smallest among three numbers
if a<b and a<c:
  print(a,"is small")
elif b<c and b<a:
  print(b,"is small")
else :
  print(c,"is small")
#perfect square or not
perfect_number =int(input(" enter the perfect square number:"))
root= math.sqrt(perfect_number)
if root==int(root):
  print("perfect square")
else:
  print("not a perfect square")
# how many required  for a given number of people 
pepole =int(input("enter the number of pepole: "))
ans =pepole//5
print("cars needed" ,ans)
#second biggest among the numbers 
if (a > b and a < c) or (a < b and a > c):
    second = a
elif (b > a and b < c) or (b < a and b > c):
    second = b
else:
    second = c

print("Second biggest number is:", second)
# leap year  or not 
year =int(input("enter your year:"))
if year%4==0 and year%100!=0 and year %400!=0:
  print(year," is leap year")
else:
  print(year,"it is not a leap year")

#outputs
#  Enter a number:13
# it is odd
# not satisfy
# enter number1: 100
# enter a number2: 90
# 100  is greater
# 90  is smaller
# enter your age 21
# Eligible to vote
# enter your  math marks 34
# enter your physics marks89
# enter your chemistry marks 90
#  all pass
# pass
# pass two subjects
# enter a first num 25
# enter a second num 78
# enter a third num 90
# 90 is big
# 25 is small
#  enter the perfect square number:49
# perfect square
# enter the number of pepole: 17
# cars needed 3
# Second biggest number is: 78
# enter your year:2024
# 2024  is leap year
# PS D:\10000 coders>


