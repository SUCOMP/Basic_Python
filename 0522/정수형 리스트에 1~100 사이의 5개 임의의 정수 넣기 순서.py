import random

a = random.randint(1,100)
b = random.randint(1,100)
c = random.randint(1,100)
d = random.randint(1,100)
e = random.randint(1,100)

list = [a,b,c,d,e]

print(list)

intlist = []
for i in range(5):
    intlist.append(random.randint(1,100))
print(intlist)

for i in range(0,4):
    for j in range(i+1,5):
        if intlist[i]>intlist[j]:
            temp = intlist[i]
            intlist[i]=intlist[j]
            intlist[j]=temp
            

print(intlist)
    
    
    
    

