from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    #guess에 랜덤단어 저장
    guess = Guess(word.randFromDB())

    finished = False
    hangman = Hangman()
    maxTries = hangman.getLife()

    while guess.numTries < maxTries:

        display = hangman.get(maxTries - guess.numTries)
        print(display)
        print(guess.word)
        guess.display()


        guessedChar = input('Select a letter: ')
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue

        finished = guess.guess(guessedChar)
        if finished == True:
            break 

    if finished == True:
        print('Success')
        print("Answer is ", guess.word)
    else:
        print(hangman.get(0))
        print('word [' + guess.word + ']')
        print('guess [' , guess.currentStatus , ']')
        print('Fail')
        print("Answer is ",guess.word)

if __name__ == '__main__':
    gameMain()
