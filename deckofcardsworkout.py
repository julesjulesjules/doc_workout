
import random
import docw_classes as docw_c
import docw_low_alternate as low_alt
import docw_basic_game as basic


print("DECK OF CARDS WORKOUT GAME\n")

print("Play Options include: \n")
print("\t Basic\n")
print("\t Alternate Low Cards\n")

play_option = input("Choose your style of play: ").lower()
print("\n")

if play_option == "basic":
    print("Great! Let's get started... \n")
    basic.basic_game()
elif play_option == "alternate low cards":
    print("Awesome! \n")
    highest_choice = input("How many alternate cards would you like? Choose 1, 2, 3, 4, or 5. ")
    print("\n")
    high_int = int(highest_choice)
    low_alt.low_alternate(high_int)
