def fibo(n):
    if(n<=1):
        return n
    return fibo(n-1)+fibo(n-2)

n=int(input("Enter no. of elements: "))
for i in range(n):
    print(fibo(i))
