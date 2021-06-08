#This is a guess the number game
import random,sys

#ask the player to guess 6 times
def game(choice):
    if choice== 'y' or choice== 'yes':
         for guessTaken in range(1,7):
              print('Take a guess')
              try:
                  guess=int(input())
                  if guess!=SecretNumber and guessTaken==6:
                      print ('Oooopsie..... you falied to  guessed my number in ' + str(guessTaken)+ ' guesses!!! OOpsie!!!!.')
                      print('!!! wanna Try again? Enter y for yes or n for No')
                      choice=input()
                      game(choice)                  
                  elif guess<SecretNumber:
                        print('Guess is too low!!!!')
                  elif guess>SecretNumber:
                         print('Guess is too high!!!!')
                  elif guess==SecretNumber:
                        print ('Woila !!!!Good job, '+name+' you guessed my number in' + str(guessTaken)+ ' guesses!!! WOILA!!!!.')
                        print('!!! wanna Play a again? Enter y for yes or n for No')
                        choice=input()
                        game(choice)
              except:
                  print('you did not enter a number Please enter correct inputs')
                  print('!!! wanna Try again? Enter y for yes or n for No')
                  choice=input()
                  game(choice)
    elif  choice== 'n' or choice== 'No':
        print('!!! Thank '+name+'  you for your time!!!!')
        sys.exit()

    else:
        print('please Enter correct input y for yes or n for No to Play')
        choice=input()
        game(choice)
        
   
print('Hello What is your Name?')
name=input()
SecretNumber=random.randint(1,20)
print('Welcome... '+name+'!!! You want to play Gueess The Number Game....Enter y for yes or n for No')
choice=input()
game(choice)
