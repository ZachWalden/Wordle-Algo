import Wordle_Stuff.wordle_sim as sim

answer = open('Wordle_Stuff/word.txt','r').read()   #read in wotd

guess = [['a', 'd', 'i', 'e', 'u'],[0,0,0,0,0]]                #guess word in [0], color value in [1]
#0 = GR, 1 = Y, 2 = G

#list of all vowels & consonants possible
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
yellow_letters = [[],[]] #[0] = letter    ;   [1] = known incorrect location
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

    #update letters with their corresponding value
    for index, i in enumerate(check_result): 
        if i == 'G':
            guess[1][index] = 2
            green_letters.append(index)     #note that a letter is green
        elif i == 'Y':
            yellow_letters.append(guess[0][index])  #append letter to search for
            guess[1][index] = 1
        else:                                       #remove unappeared letters from searchable
            if guess[0][index] in vowels:
                vowels.remove(guess[0][index])
                break
            print(index)
            if guess[0][index] in consonants:
                consonants.remove(guess[0][index])
    print(guess[1]) #print result from removed letters

    guess_valid_letters_total = len(green_letters) + len(yellow_letters[0])
    """"""
    #no yellow nor green:
    #if ((len(yellow_letters) == 0) and not green_letters):      
    for i in guessable_words:

        for j in range(5):    
            if i[j] in vowels or j in consonants:
                guess_valid_letters_total += 1
        if guess_valid_letters_total == 5:
            guess[0] = list(i)
            break
        guess_valid_letters_total = len(green_letters) + len(yellow_letters[0])
            
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
    print(guess)
    remaining_guesses -= 1      #subtract a guess at end of current ieration        

print(consonants, vowels)
                
