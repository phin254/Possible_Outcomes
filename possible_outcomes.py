# python tool to predict all the possibilities for 6 football(soccer) matches.
import itertools  # pip install itertools

# define the 3 possible outcomes for each game
outcomes = list(itertools.product(["Home, ", "Draw, ", "Away, "], repeat=6))
# create a text file to print out the outcomes.
with open("outcomes.txt", "w") as f:
    # make a loop for all 729 outcomes.
    for outcome in outcomes:
        # print out the outcomes on the text file.
        f.write("".join(outcome) + "\n")
