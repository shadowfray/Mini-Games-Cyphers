#Hangman

from random import *

def main(answer, random=False):
    guessfin, guesscount =  6, 0
    randomwords = ['dungeon','whiteboard','lynx','lament','butterfly','mountain','exposure','jumping'
                   ,'journey','python','pumpkin','exponential','automation','cardboard','ketchup',
                   'pizza','burger','television','monster','monopoly']

    #randomly picks a word for the player
    if random == True:
        ran_n = randrange(len(randomwords))
        answer = randomwords[ran_n]
        
    answerlist,guessed = [],[]
    answerlist += answer

    reveal = []
    blankspacelist = ['- ']
    for xk in range(len(answer)):
        reveal += blankspacelist

    print('Welcome to Hangman!')
    print('Please input a single lower case letter (ex: g)')

    #The game itself is below here, everything above is set up
    while True:
        if guesscount == 1:
            print('|====|')
            print('|    o')
            print('|')
            print('|')
            print('= ')
        if guesscount == 2:
            print('|====|')
            print('|    o')
            print('|    | ')
            print('|')
            print('= ')
        if guesscount == 3:
            print('|====|')
            print('|    o')
            print('|   /| ')
            print('|')
            print('= ')
        if guesscount == 4:
            print('|====|')
            print('|    o')
            print('|   /|\ ')
            print('|')
            print('= ')
        if guesscount == 5:
            print('|====|')
            print('|    o')
            print('|   /|\ ')
            print('|    /')
            print('= ')
        print('')
            
        print(''.join(reveal))
        print('Tries remaining:',guesscount,'/',guessfin)
        
        playerinput = input('Guess a letter: ')

        #makes sure the player guesses only a lower case letter
        if len(playerinput) != 1 or 97 > ord(playerinput) or ord(playerinput) > 122:
            print('Please guess a single letter')
            guesscount -= 1
            playerinput =''

        if playerinput in guessed:
                print('you already guessed that!')
                joinedguessed = ' '.join(guessed)
                print('Guessed:', joinedguessed)
                
        if playerinput not in guessed:
            guessed += playerinput

        if playerinput in answerlist:
            print('!!!')

            for n in range(len(answer)):
                if answerlist[n] == playerinput:
                    reveal[n] = playerinput

        else:
            print('Incorrect, try again')
            guesscount += 1

        empty = 0
        for j in reveal:
            if j == '- ':
                empty +=1

        if empty == 0:
            print('YOU WIN!!!')
            break
        else:
            print(empty, 'spaces remain')

        if guesscount >= guessfin:
            print('|====|')
            print('|    o')
            print('|   /|\ ')
            print('|    /\ ')
            print('= ')
            print('YOU LOSE!')
            break

        print('='*10)
        print('')

    print('ANSWER:', answer)
    input('==[press any key to exit]==')

    
main('calculator', True)
