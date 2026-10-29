
import random 
num = random.randint(1,100)
print (num)
abs
listofguess = []
guess = int(input('enter your number'))
if guess == num:
    print ('First time guest!')
else:  
    if guess<1 or guess > 100:
            print('out of bounds')
    else:
        if abs(guess-num) < 10:
            print('WARM')
        else:
            print('COLD')
    listofguess.append(guess)
while guess!=num:
    guess = int(input('enter your number'))
    if guess == num:
        print('winner!, it took you this many tries:',len(listofguess))
    if guess<1 or guess > 100:
        listofguess.append(guess)
        print('out of bounds')
        continue
    if guess != num:
        if  abs(guess-num) < abs(listofguess[-1]-num):
            print('warmer',listofguess)
        else:
            print('colder',listofguess)
        listofguess.append(guess)
        
