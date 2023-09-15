import Wordle_Stuff.wordle_sim as sim

answer = open('Wordle_Stuff/word.txt','r').read()   #read in wotd

guess = [['a', 'd', 'i', 'e', 'u'],[0,0,0,0,0]]                #guess word in [0], color value in [1]
#0 = GR, 1 = Y, 2 = G

#list of all vowels & consonants possible
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
yellow_letters = {} #key = letter, value = [#,#,#,#,#] of boolean know incorrect location
remaining_guesses = 6
green_letters = []

"""Import the answer"""
append_word = ""
guessable_words = []
for i in open('Wordle_Stuff/lists/guessable.txt','r').read():
    if i == '\n':
        guessable_words.append(append_word)
        append_word = ''
    else:
        append_word += i
guessable_words.append(append_word)
#print(guessable_words)


#loop until all guesses used / break upon answer
while (remaining_guesses > 0):

    """CHECK GUESS"""
    check_result = sim.check_word(''.join(guess[0]), answer)
    if(check_result == ['G','G','G','G','G']):
        print("Answer:", ''.join(guess[0]))
        break
    print("Word Guess Result: ", check_result)

    #update letters with their corresponding value
    for index, i in enumerate(check_result): 
        if i == 'G':
            guess[1][index] = 2 #update in guessed word
            green_letters.append(guess[0][index])     #note that a letter is green
        elif i == 'Y':
            if not yellow_letters.get(i):   #if first time finding yellow
                templist = [False,False,False,False,False]
                templist[index] = True
                yellow_letters.update({guess[0][index] : templist})  #append letter to search for
            else:
                templist = yellow_letters.get(guess[0][index])
                templist[index] = True
                yellow_letters.update({guess[0][index] : templist})
            guess[1][index] = 1 #update in guessed word
        else:                                       #remove unappeared letters from searchable
            if guess[0][index] in vowels:
                vowels.remove(guess[0][index])
                continue
            if guess[0][index] in consonants:
                consonants.remove(guess[0][index])
            guess[1][index] = 0 #update in guessed word
    print("Word Grade: ", guess[1]) #print result from assigned letters

    """"""
    #no yellow nor green:
    #if ((len(yellow_letters) == 0) and len(green_letters) == 0):  
    for i in guessable_words:
        guess_valid_letters_total = 0
        yellows_needed = len(yellow_letters)
        for j in range(5):    #iterate thru word
            if i[j] in vowels or i[j] in consonants:    #if is a remaining letter
                if guess[1][j] == 2 and guess[0][j] != i[j]:  #if letter is green & matches
                    break
                guess_valid_letters_total += 1
        if guess_valid_letters_total == 5:  #if 5 possible letters, guess
            guess[0] = list(i)
            break
            
    """        
    #yellow, no green:
    elif ((len(yellow_letters) > 0) and not green_letters):     
        for i in guessable_words:      #check if current guessable word is valid first
            for j in range(5):          #isolate chars of word
        pass

    #green, no yellow:
    elif ((len(yellow_letters) == 0) and green_letters):        
        for i in len(guessable_words):      #check if current guessable word is valid first
            for j in range(5):          #isolate chars of word
        pass

    #otherwise, green & yellow
    else:                                                       
        pass"""
    print("\nGuess:", guess[0])
    print("Consonants:", consonants)
    print("Vowels: ", vowels)
    remaining_guesses -= 1      #subtract a guess at end of current ieration        
print(consonants, vowels)