import Wordle_Stuff.wordle_sim as sim
import time



def guess():
    #sim.check_word works both with uper and lowercase words
    print(sim.check_word("TESTS"))

    #lists also work
    guess_word = ['t','e','s','t','s']

    print(sim.check_word(guess_word))

#start time
t0 = time.time()

guess()

#end time
t1 = time.time()

elapsed = t1-t0

#total time passed
print(elapsed)