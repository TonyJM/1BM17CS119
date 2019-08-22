L=input("Enter integer: ").split(",")
A=[]
for i in L:
    if (int(i)%2==0):
        A.append(int(i))
print("\nEven Elements: ",A)
