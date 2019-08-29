def bSearch(L,x):
    b=0
    e=len(L)
    while(b<=e):
        m=int((b+e)/2)
        if (L[m]==x):
            return True
        elif(L[m]>x):
            e=m-1
        elif(L[m]<x):
            b=m+1
    return False


L=input("Enter integers: ").split(",")
A=[]
for i in L:
    A.append(int(i))
x=int(input("Enter number to search for: "))



print(bSearch(A,x))
