def marks(*marks):
    total=sum(marks)
    count=0
    for i in marks:
        count+=1
    avg=total/count
    print(avg)
marks(10,20,30)
def details(*subjects ,**info):
    print(f"{subjects} and the name {info['name']} and age is {info['age']}")
details("maths","physics", "socail" , name="keerthana" ,age=21)
 
def acceptproduc(*names,**metadata):
    for name in names:
     print(f"name is {name} and category{metadata['category']} and the brand is {metadata['brand']} and price is {metadata['price']} and the range is : {metadata['price']}")
acceptproduc("keerthana" ,"parinaya",category="shopping" , brand= "apple", price=10000)
# to double the numbers using the pure functions 
def double_numbers(numbers):
   return [n*2  for n in numbers]
print(double_numbers([1,2,3]))
# celusis to farheat
def ctof(temp):
   return [c*(9/5)+32 for c in  temp]
print(ctof([32,94,54]))
# cube of numbers
def cubeofnumbers(numbers):
   return [n*3 for n in numbers]
print(cubeofnumbers([1,2,3,4,5]))
#odd or even 
def oddoreven(num):
   if num%2==0:
      print("even")
   else:
      print("odd")
oddoreven(11)
#min and max
def get_min_max(numbers):
    return min(numbers), max(numbers)

print(get_min_max([4, 2, 9, 1]))
def sum_and_avg(numbers):
    sum1=sum(numbers)
    count=0
    for i in numbers:
       count+=1
    avg =sum1/count
    return sum1,avg


print(sum_and_avg([4, 2, 9, 1]))
def divide(a, b):
    quotient = a // b
    remainder = a % b
    print("Quotient:", quotient)
    print("Remainder:", remainder)

divide(10, 3)
def squareandcube(numbers):
   return[ n*2 for n in numbers] ,[n*3 for n in numbers]
print(squareandcube([1,2,3,4]))
#to print numbers from n  to 1 
def rev_num(n):
   if n==0:
      return 1
   return n-1
rev_num(5)



