
# Online Python - IDE, Editor, Compiler, Interpreter

import random
h = 0 
t = 0


for x in range(3):
    print('Tossing a coin...')
    y = random.randint(1,2)
    print('Round ' ,x+1,':' )
    if y == 1:
        print('Heads')
        h+=1
    elif y == 2: 
        print('Tails')
        t+=1
print('Heads:' , h , 'Tails:' , t)

if h > t:
     print('You won')
else: 
    print('You lost')
