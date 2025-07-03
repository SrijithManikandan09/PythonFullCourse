'''List []
a=[1,2,3,4,5,6,7,8,9]
print(a)
a.append(6)
a.append("Emc")
a.append("True")
print(a)
a.insert(3,25)
print(a)
a.pop()
a.pop(3)
print(a)
b=[12,13,14,15,16]
a.extend(b)
print(a)

Tuple
a=(1,2,3,4)
print(a)
b=list(a)
print(b)
b.append(24)
c=(5,6,7,8,9)
d=list(c)
b.extend(d)
print(b)
b.insert(4,45)
b.pop()
a=tuple(b)
print(a)

Set {}
a={1,2,3,4,12,14,7,8,9}
a.add(10)
a.remove(12)
a.pop()
print(a)

Dictionary{} '''
a={
    "name":"Srijith",
    "age":20,
    "location":"Vellore",
    "class Member":["Abi","Sri","bala"]
}
print(a["location"])
print(a)
print(a["age"])
print(a)
a["age"]=23
print(a.keys())
print(a.values())
print(a)
