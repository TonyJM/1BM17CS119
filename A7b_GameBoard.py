def printBoard(n):
    for i in range(n):
        print(' ---'*n)
        print('|   '*(n+1))
    print(' ---'*n)
    
n=int(input("Enter value : "))
printBoard(n)
