#This is  a guess the numvber game
import random,sys

#ask the player to guess 6 times
def game(choice1):
    if choice1== 'y' or choice1== 'yes':
        for guessTaken in range(1,7):
            print('Take a guess')
            guess=int(input())
            if guess<SecretNumber:
                print('Guess is too low!!!!')
            elif guess>SecretNumber:
                 print('Guess is too high!!!!')
            elif guess==SecretNumber:
                print ('Good job, '+name+' you guessed my number in' + str(guessTaken)+ ' guesses!!! WOILA!!!!.')
                print('!!! wanna Play a again? Enter y for yes or n for No')
                choice1=input()
                game(choice1)
            elif guess!=SecretNumber and guessTaken==6:
                print (' you falied to  guessed my number in' + str(guessTaken)+ ' guesses!!! OOpsie!!!!.')
                print('!!! wanna Try again? Enter y for yes or n for No')
                choice1=input()
                game(choice1)           
    else:
        print('!!! Thank you for your time!!!!')
        sys.exit()       
    
print('Hello What is your Name?')
name=input()
SecretNumber=random.randint(1,20)
print('Hello '+name+'!!! wanna Play a Game? Enter y for yes or n for No')
choice1=input()
game(choice1)




