print('Number Guessing Game')
print('Enter a number between 1-10')


firstGuess=int(input('Enter your first guess:'))


if firstGuess==7:
    print("Superb! You guessed the Number !!")
elif firstGuess<3:
    print("Too low, try a higher number...")
elif firstGuess<2:
    print("Too low, try a higher number...")
elif firstGuess<4:
    print("Too low, try a higher number...")
elif firstGuess==5:
    print("Close... Keep trying")
elif firstGuess==8:
    print("Too far, try a lower number")
elif firstGuess==9:
    print("Too far, try a lower number")
elif firstGuess==6:
    print("Close... Keep trying")
elif firstGuess==1:
    print("Too low, try a higher number...")
elif firstGuess>11:
    print("Too far, try a lower number")
