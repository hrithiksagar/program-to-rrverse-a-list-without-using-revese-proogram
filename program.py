l=[]
s=int(input("enter list size"))
for i in range(s):
    x=input("enter list items: ")    
    l.append(x)
print("the list is",l)
m=[]
for i in range(1,s+1):
    m.append(l[-1*i])
print(m)
