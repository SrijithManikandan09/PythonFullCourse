'''
for i in range(1,11):
    print(i , "* 2 = " , i*2 )

a = int(input())
b = int(input())
for i in range(a,b+1):
    print(i)
    
how Count works ?
Step 1:
i runs around 10 times 
Step 2:
i is multiplied by 2 and the result is printed
Step 3:

count=0
for i in range(0,10):
    if i%2==1:
        print(i)
        count=count+1
print("Odd =" , count)

countEven=0
countOdd=0
for i in range(0,20):
    if i%2==1:
        print(i)
        countOdd=countOdd+1
    elif(i%2==0):
        print(i)
        countEven=countEven+1
print("Odd" ,countOdd)
print("Even" ,countEven)

count3 = 0
count5 = 0
for i in range(1,101):
    if i%3==0:
        count3=count3+1
    if i%5==0:
        count5=count5+1
print(count3)
print(count5)
print(count3+count5)

sum = 0
for i in range(1,6):
    sum=sum+i
print(sum)

a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    print(i)

a=[]
a.append(10)
a.append(20)
b=int(input())
a.append(b)
print(a)

a=[]
num=[]
print("Enter 10 Number")
for i in range(1,10):
    num=int(input("Enter Num  " + str(i) ) )
    a.append(num)
print(a)

a=[]
num=0
sum=0
for i in range(1,11):
    num=int(input("Enter a Number " + str(i) + ": "))
    sum=sum+num
    a.append(num)
print(sum)
print(sum/10)
print(a)

a=[]
sum=0
num=0
n=0
n=int(input("Enter the N value"))
for i in range(1,n):
    num=int(input("Enter a Number " + str(i) + ":"))
    sum=sum+num
    a.append(num)
print("The First" , n , "Natural Number is" , a)
print(sum)

a=[]
sum=0
num=0
n=int(input("Number of Natural number to be printed "))
for i in range(1,n+1):
    sum=sum+i
    print(i, end=" ")
print(sum)

n=int(input("Enter the Number of term for Cube : "))
for i in range(1,n+1):
    print("The Number is : ", i , "and" , "Cube of the ", i , "is" , i*i*i )

for i in range(1,5):
    print("*" * i)

rows = 5
for i in range(rows):
    spaces = ' ' * (rows - i -1)
    stars = '*' * (2*i+1)
    print(spaces + stars + spaces)
'''
