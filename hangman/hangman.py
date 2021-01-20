# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if len(secretWord) == 1 and secretWord[0] in lettersGuessed:
        return True
    elif secretWord[0] in lettersGuessed:
        return isWordGuessed(secretWord[1 : ], lettersGuessed)
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    if len(secretWord) == 1 and secretWord[0] in lettersGuessed:
        return secretWord[0]
    elif len(secretWord) == 1 and secretWord[0] not in lettersGuessed:
        return ' _ '
    elif secretWord[0] in lettersGuessed:
        return secretWord[0] + getGuessedWord(secretWord[1 : ], lettersGuessed)
    else:
        return '_ ' + getGuessedWord(secretWord[1 : ], lettersGuessed)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    x = [letter for letter in string.ascii_lowercase if letter not in lettersGuessed]
    return ''.join(x)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    
    n = number of guesses remaining
    guess = list of strings; letters guessed
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secretWord)))
    print('_ _ _ _ _ _ _ _ _ _ _ \n')
    n = 8
    guess = []
    import string
    while isWordGuessed(secretWord, guess) == False:
        print('You have {n} guesses left.'.format(n = n))
        print('Available letters: {letters}'.format(letters = getAvailableLetters(guess)))
        x = input('Please guess a letter: ').lower()
        if len(x) > 1 or x not in string.ascii_lowercase or x in guess:
            if x in guess:
                print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, guess)))
                print('_ _ _ _ _ _ _ _ _ _ _ \n')
                continue
            else:
                print('invalid input!')
                print('_ _ _ _ _ _ _ _ _ _ _ \n')
                continue
        elif x in secretWord:
            guess.append(x)
            print('Good guess: {}'.format(getGuessedWord(secretWord, guess)))
            print('_ _ _ _ _ _ _ _ _ _ _ \n')
            continue
        else:
            n -= 1
            guess.append(x)
            print('Oops! That letter is not in my word: {}'.format(getGuessedWord(secretWord, guess)))
            print('_ _ _ _ _ _ _ _ _ _ _ \n')
            if n > 0:
                continue
            else:
                return print('Sorry, you ran out of guesses. The word was "{}".'.format(secretWord))
    return print('Congratulations, you won!')
            
        







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
