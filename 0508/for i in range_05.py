for i in range(1,6):
    print(i,end="")
print()

for Num in range(2,10):
    print("="*80)
    for i in range(1,10):
        print("%d*%d=%d" %(Num,i,Num*i), end="   ")
