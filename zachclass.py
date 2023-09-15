import Wordle_Stuff.wordle_sim as sim

class Guesser:
    
    def __init__(self):
        guess = [['a', 'd', 'i', 'e', 'u'],[0,0,0,0,0]]     #guess word in [0], color value in [1]
        remaining_guesses = 6                               #total allowed guesses
        answer = open('Wordle_Stuff/word.txt','r').read()   #read in wotd
        vowels = ['a', 'e', 'i', 'o', 'u']                  
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        

    def check_guess(self):
        check_result = sim.check_word(''.join(self.guess[0]), self.answer)

        pass

    def remove_nonexisting_letter(self, letter):

        pass