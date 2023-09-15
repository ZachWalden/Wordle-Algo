def check_word(guess_word, word):

    #word = (open('Program\Wordle_Stuff\word.txt','r').read())

    guess_word = guess_word.upper()

    color_word = ["GR"]*5
 
    repeats = {}

    for i in word:
        try:
            repeats[i] = repeats[i] + 1
        except:
            repeats[i] = 1


    for count, i in enumerate(guess_word):

        if i.upper() == word[count]:
            color_word[count] = "G"
            repeats[i] -= 1
    for count, i in enumerate(guess_word):

        if word.find(i.upper()) >= 0 and repeats[i] > 0 and color_word[count] != "G":
            color_word[count] = "Y"

    #returns a list with 
    # 'GR' being gray
    # 'Y' being yellow
    # 'G' being green


    return color_word
