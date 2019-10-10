with open('Happy.txt','r') as f:
    a=f.read()
    a=a.strip()
    a=a.split(',')

with open('Prime.txt','r') as f:
    b=f.read()
    b=b.strip()
    b=b.split(',')

print("Overalapping Happy and Prime Numbers:")
for i in a:
    if i in b:
        print(i)


