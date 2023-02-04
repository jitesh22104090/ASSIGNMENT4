import random
for i in range(0,10):
    a=random.randint(1,10)
    b=random.randint(1,10)
    print(a,'*',b)
    c=int(input('enter multiplication of the two numbers :- '))
    if c==a*b:
        print('Right!')
    else:
        print('Wrong.The correct answer is',a*b)