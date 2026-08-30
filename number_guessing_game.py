print('='*60)
print('NUMBER GUESSING GAME')
print('='*60)
import random
number=random.randint(1,100)
guess=int(input('enter your guessing number :'))
if number==guess:
    print('congratulation you guessed it')
elif guess<number:
    print('to small try again')
else:
    print('to high try again ')
while True:
    guess=int(input('enter your guess:'))
    if guess==number:
        print('congratulation u guessed it')
        break
    elif guess<number:
        print('too small try again')
    else:
        print('too high try again ')