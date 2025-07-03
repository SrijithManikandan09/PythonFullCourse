'''def painter():
    return "I am a Painter"
print(painter())

def painter():
    return "I am a Painter"
msg=painter()
print(msg)

def valueofa():
    return 10
print(valueofa())

s_username="EMC"
s_passowrd="123"
uname=input("Enter Your Username")
passowrd=input("Enter Your Password")
def validate():
    if uname==s_username and passowrd==s_passowrd:
        print(True)
    else:
        print(False)
validate()

s_username="EMC"
s_passowrd="123"
uname=input("Enter Your Username")
passowrd=input("Enter Your Password")
def validate():
    if uname==s_username and passowrd==s_passowrd:
        return True
    else:
        return False
a=validate()
print(a)
'''
a=int(input("Enter a Number"))
b=int(input("Enter a Number"))
c=int(input("Enter a Number"))
def add():
    return a+b
d=add()
def mul():
    return d*c
print(mul())
    