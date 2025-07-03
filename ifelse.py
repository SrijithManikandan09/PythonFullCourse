'''
if(False):
    print("Yes")
else:
    print("NO")
#true and false are Boolean Value 0 and 1
print("win"=="winn")
#Compare
Rcb="winn"
if(Rcb=="win"):
    print("yes,CUp")
else:
    print("NO")

meghna = input("IS meghna Died or Alive ?")
if(meghna=="Died"):
    print("he meets she")
else:
    print("he doesnt meet's she")

mark = int(input("Enter Your MArk ?"))
if(mark>35):
    print("Pass")
else:
    print("Fail")

Income = int(input("Enter the Income ?"))
if(Income>7000):
    print("Not eligible for scholarship")
else:
    print("Eligible for scholarship")

number = int(input("Enter A Number"))
if(number%5==0 & number%3==0):
    print("Divisible by both 5 and 3")
else:
    print("Not Divisible by both 5 and 3")

number=int(input("Enter A Number"))
if(number%2==0):
    print("Even Number")
else:
    print("Odd Number")

mark = int(input("Enter your mark ? "))
if(mark<35):
    print("Poor Student")
elif(mark>=35 & mark<70):
    print("Average Student")
elif(mark>70 & mark<=100):
    print("Good Student")
else:
    print("Invalid Mark")

a= int(input("Enter your Mark ? "))
b= int(input("Enter Your Mark ? "))
c= (input("What Should I do ? (add/sub/div/mul)"))
if(c=="add"):
    print(a+b)
elif(c=="sub"):
    print(a-b)
elif(c=="Div"):
    print(a/b)
elif(c=="mul"):
    print(a*b)
else:
    print("Invalid Operation")

score=int(input("Enter Your Score ?"))
if(score>=70):
    name=input("Enter Your Name ?")
    department= input("Enter the department")
    location= input("enter your Location?")
    print("eligible")
else:
    print("Not Eligible")

salary = int(input("Enter Your Salary ? "))
age = int(input("Enter Your Age ?"))
if(salary>=20000 or age<=25 ):
    print("You Are Eligible  Loan")
    loan=int(input("Enter The loan amount ?"))
    if(loan<=50000):
        print("Eligible for Loan")
    else:
        print("Not Eligible for loan")    
else:
    print("You are not Eligible ")

mark1 = int(input("Enter the Mark subject 1 ?"))
mark2 = int(input("Enter the Mark subject 2 ?"))
mark3 = int(input("Enter the Mark subject 3 ?"))
mark4 = int(input("Enter the Mark subject 4 ?"))
mark5 = int(input("Enter the Mark subject 5 ?"))
total = mark1 + mark2 + mark3 + mark4 + mark5
average = total/5
if(average<35):
    print("addition class needed")
else:
    print("You are good to go")
print(total , average )
'''
n = int(input())
if(n%2==0):
    if(n>=2 and n<=5):
        print("Not Weird")
    elif(n>=6 and n<=20):
        print("weird")
    elif(n>20):
        print("Not Weird")
else:
    print("Weird")

