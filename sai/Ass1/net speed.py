n=10
f0= 0
f1=1
f2=f1
count=1
print(f0,f1)
while(count<=n):
    print(f2)
    fo, f1= f1, f2
    f2=f0+f1
    count+= 1
