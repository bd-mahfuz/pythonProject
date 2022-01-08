
# while loop
x = 1
while x<=5:
    print(x)
    x = x+1


# triangle of star example using while loop
print('triangle shape using while loop')
a=1
while a <= 5:
    print('*' * a)
    a = a + 1


# guessing game
secretNumber = 9
counter = 1
while counter <= 3:
    guessNumber = input()
    if int(guessNumber) == 9:
        print('Win')
        break
    #else:
    #    if counter == 3:
    #        print('You failed')
    counter = counter + 1
else: # in python while loop also have optional else part, If while condition is not true it will go to else part
    print('You failed')
