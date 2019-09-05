import string, random

def pwdGen():
    n=random.randint(8,31)
    opt=string.ascii_letters+string.digits+string.punctuation
    return ''.join(random.choice(opt) for i in range(n))

while 1:
    x=input("Generate Password? (y/n): ")
    if x=='y':
        print(pwdGen())
    elif x=='n':
        break
    
