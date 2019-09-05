import string, random

def pwdGen():
    n=random.randint(4,12)
    l=random.choice(string.ascii_lowercase)
    u=random.choice(string.ascii_uppercase)
    d=random.choice(string.digits)
    p=random.choice(string.punctuation)
    opt=string.ascii_letters+string.digits+string.punctuation
    s=l+u+d+p+''.join(random.choice(opt) for i in range(n))
    return ''.join(random.sample(s,n+4))

while 1:
    x=input("Generate Password? (y/n): ")
    if x=='y':
        print(pwdGen())
    elif x=='n':
        break
    
