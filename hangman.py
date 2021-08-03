import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    k=0
    for letters in letters_guessed:
        for number in range(0,len(secret_word)):
            if letters==secret_word[number]:
                k=k+1
    if k==len(secret_word):
        return True
    else:
        return False




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    spaceletter=[]
    for namber in range(0,len(secret_word)):
        spaceletter.append("_ ")

    for letters in letters_guessed:
        for number in range(0,len(secret_word)):
            if letters==secret_word[number]:
                spaceletter[number]=secret_word[number]
    stringspaceletter=""
    for x in spaceletter:
        stringspaceletter=stringspaceletter+x
    return stringspaceletter



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessedlst=[]

    for x in string.ascii_lowercase:
        letters_guessedlst.append(x)
    for x in letters_guessed:
        if x in letters_guessedlst:
            letters_guessedlst.remove(x)
    letters_guessed=''
    for x in letters_guessedlst:
        letters_guessed=letters_guessed+x
    return letters_guessed

    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to game hangman.")
    n=len(secret_word)
    print("Hey idiot I am thinking of words which is",n,"letters long")
    print("----------------------------------------------------")
    print("You have 6 guesses left and 3 warning.")
    print("Available letters:",get_available_letters(["0"]))

    userinput=[]
    x=True
    k=6
    warning=3
    l=0
    userinputt=[]


    while x==True:

      userinputstring=str.lower(input("Please guess a letter: "))

      l=l+1

      if userinputstring not in userinputt and userinputstring in secret_word:
        userinputt.append(userinputstring)

      if userinputstring in secret_word and userinputstring!="" and userinputstring:
        print("Good guess:",get_guessed_word(secret_word,userinputt))
        print("----------------------------------------------------")
      print("available letters:",get_available_letters(userinput))
      

      if userinputstring in userinput:
        warning=warning-1
        print("Warning: Dude you have already input that letter. Now you got",warning,"warnings.")
        print(get_guessed_word(secret_word,userinput))
        print("----------------------------------------------------")
      
      if warning==0:
        k=k-1
        warning=3

      if userinputstring not in userinput and userinputstring in secret_word:
        userinput.append(userinputstring)
      

      if is_word_guessed(secret_word,userinput)==True:
        x=False
        print("You Win! This is your score",len(userinput)*k, "The word is", secret_word)
        return 0
      
      if str.isalpha(userinputstring)==False:
        warning=warning-1
        print("Oops! That letter is not valid you got",warning," warning left.",get_guessed_word(secret_word,userinput))
        print("----------------------------------------------------")
        warning=warning-1
      

      if userinputstring not in secret_word and bool(str.isalpha(userinputstring))==True:
        print("Oops! That letter is not in my word.")
        print("Please guess a letter:",get_guessed_word(secret_word,userinput))
        print("----------------------------------------------------")
        if userinputstring in "aeiou":
          k=k-2
        else:
          k=k-1

      
      print("You have",k,"guesses left.")
    

      if k==0:
        x=False
        print("You lose. Loserrrr! The word was", secret_word ,"! And your score is 0 as your life. You worthless piece of shit.")
    




def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    x=0
    c=0
    while x<len(other_word):
        if my_word[c]!=other_word[x] and my_word[c]!="_":
            return False
        if my_word[c]=="_":
            c=c+2
        else:
            c=c+1
        x=x+1
    else:
        return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    hint=[]
    for words in wordlist:
        c=0
        x=0
        conditional=True
        while conditional:
            if my_word[c]!='_' and my_word[c]!=words[x]:
                conditional=False
            x=x+1
            if my_word[c]=='_':
                c=c+2
            else:
                c=c+1
            if conditional==True and x==(len(words)) and c==(len(my_word)):
                hint.append(words)
                conditional= False
            elif x==(len(words)) or c==(len(my_word)):
                conditional=False
    wordstr=''
    if len(hint)==0:
        return "Not found"
    else:
        for wordd in hint:
            wordstr=wordstr+wordd+" "
        return wordstr


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to game hangman.")
    n=len(secret_word)
    print("Hey idiot I am thinking of words which is",n,"letters long")
    print("----------------------------------------------------")
    print("You have 6 guesses left and 3 warning.")
    print("Available letters:",get_available_letters(["0"]))

    userinput=[]
    x=True
    k=6
    warning=3
    l=0
    userinputt=[]
    asterikbuster=None


    while x==True:

      userinputstring=str.lower(input("Please guess a letter: "))


      l=l+1

      if type(asterikbuster)==int:
        asterikbuster=asterikbuster+1

      if asterikbuster==2:
        asterikbuster=None

      userinputt.append(userinputstring)

      if userinputstring=="*" and asterikbuster==None:
        print(show_possible_matches(get_guessed_word(secret_word,userinputt)))
        asterikbuster=0
      
      
        

      if userinputstring in secret_word and userinputstring!="" and userinputstring:
        print("Good guess:",get_guessed_word(secret_word,userinputt))
        print("----------------------------------------------------")
      print("available letters:",get_available_letters(userinputt))
      

      if userinputstring in userinput:
        warning=warning-1
        print("Warning: Dude you have already input that letter. Now you got",warning,"warnings.")
        print(get_guessed_word(secret_word,userinput))
        print("----------------------------------------------------")
      
      if warning==0:
        k=k-1
        warning=3

      if userinputstring not in userinput and userinputstring in secret_word:
        userinput.append(userinputstring)
      

      if is_word_guessed(secret_word,userinput)==True:
        x=False
        print("You Win! This is your score",len(userinput)*k, "The word is", secret_word)
        return 0
      
      if str.isalpha(userinputstring)==False and userinputstring!="*":
        warning=warning-1
        print("Oops! That letter is not valid you got",warning," warning left.",get_guessed_word(secret_word,userinput))
        print("----------------------------------------------------")
        warning=warning-1
      

      if userinputstring not in secret_word and bool(str.isalpha(userinputstring))==True:
        if asterikbuster==1:
          x=False
          print("You lose. Loserrrr! The word was", secret_word ,"! And your score is 0 as your life. You worthless piece of shit.")
          return "shit"
        print("Oops! That letter is not in my word.")
        print("Please guess a letter:",get_guessed_word(secret_word,userinput))
        print("----------------------------------------------------")
        if userinputstring in "aeiou":
          k=k-2
        else:
          k=k-1

      
      print("You have",k,"guesses left.")
    

      if k==0:
        x=False
        print("You lose. Loserrrr! The word was", secret_word ,"! And your score is 0 as your life. You worthless piece of shit.")




