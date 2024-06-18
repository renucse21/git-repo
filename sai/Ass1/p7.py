n=input("Enter your string:")
for i in range(len(n)):
    print(n[i])
print("slice")
print(n[5:8])
print("range slice")
print(n[:5])
n=input("Enter your string:")
s=[]
for i in n:
    if i not in s:
        s.append(i)
print(s)


