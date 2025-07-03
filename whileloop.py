'''
i = 0
while(i==0):
    print(i)
    i=1

i=1
while(i<=5):
    print(i)
    i=i+1

i=10
while(i<=200):
    print(i)
    i=i+10

i=10
while(i>0):
    print(i, end= ",")
    i=i-1
'''
i=int(input("Enter A Value 5 "))
fact=1
while(i>0):
    fact=fact*i
    i=i-1
print(fact)