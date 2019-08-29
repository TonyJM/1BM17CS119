def Reversi(s):
    L=s.split(" ")
    for i in L[::-1]:
        print(i,end=" ")
    print()
    for i in L:
        print(i[::-1],end=" ")

s=input("Enter string: ")
Reversi(s)
