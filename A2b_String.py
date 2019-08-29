def Reversi(s):
    L=s.split(" ")
    for i in L[::-1]:
        print(i[::-1],end=" ")

s=input("Enter string: ")
Reversi(s)
