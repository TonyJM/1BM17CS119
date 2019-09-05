n=int(input("Enter number: "))
print("Divisors:")
for i in range(1,n+1):
    if n%i==0:
        print(i)
