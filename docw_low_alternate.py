################################################################################
### DOCW low_alternate function
################################################################################
### Julie Gilbert
### 1/21/2018
################################################################################

### option for if the user would like to use different extra length exercises for
### the lower numbered cards

################################################################################

import random
import docw_classes as docw_c

def low_alternate(max_different=1):

    while max_different > 5:
        max_different = input("That number is too high. Please select a number between 1 and 5.")

    exercises = {"cardio" : ["BURPEES", "JUMPING JACKS", "MOUNTAIN CLIMBERS", "HIGH KNEES", "TUCK JUMPS"], "upper" : ["PUSH-UPS", "BACK PUSH-UPS", "Y'S", "T'S", "W'S", "Y'S-T'S-W'S", "PIKE SHOULDER PRESS"],
    "lower" : ["JUMP SPLIT LUNGE", "LUNGES", "AIR SQUAT", "DONKEY KICKS", "BRIDGES", "SIDE LUNGE", "PISTOL SQUAT", "SINGLE LEG DEADLIFT", "CALF RAISE"],
    "core" : ["SIT-UPS", "V-UPS", "FLUTTER KICKS", "BICYCLE CRUNCHES", "SUPERMAN", "INCHWORM", "RUSSIAN TWIST"],
    "extras": ["PULL-UPS", "WALL SIT", "PLANK"]}

    suits =  ["DIAMONDS","CLUBS","HEARTS","SPADES"]

    exercise_assignment = {}
    for each_category in exercises:
        if each_category == "extras":
            exercise_assignment[each_category] = random.choice(exercises[each_category])
        else:
            suitchoice = random.choice(suits)
            suits.remove(suitchoice)
            exercise_assignment[suitchoice] = random.choice(exercises[each_category])

    for i in range(52):
        workout_deck = docw_c.Deck()
        workout_deck.shuffle()
        action_card = str(workout_deck.pop_card())
        ac = action_card.upper().split()

        print("{}/52\n".format(i+1))

        if ac[0] == "KING":
            print("Do 10 of {}".format(exercise_assignment[ac[2]]))
            if i == 51:
                input("CONGRATULATIONS YOU'RE DONE!")
            else:
                input("Press Enter to continue...\n")
        elif ac[0] == "QUEEN":
            print("Do 10 of {}".format(exercise_assignment[ac[2]]))
            if i == 51:
                input("CONGRATULATIONS YOU'RE DONE!")
            else:
                input("Press Enter to continue...\n")
        elif ac[0] == "JACK":
            print("Do 10 of {}".format(exercise_assignment[ac[2]]))
            if i == 51:
                input("CONGRATULATIONS YOU'RE DONE!")
            else:
                input("Press Enter to continue...\n")
        elif ac[0] == "ACE":
            print("Do 1 of {}".format(exercise_assignment["extras"]))
            if i == 51:
                input("CONGRATULATIONS YOU'RE DONE!")
            else:
                input("Press Enter to continue...\n")
        elif int(ac[0]) <= max_different:
            print("Do {} of {}".format(max_different, exercise_assignment["extras"]))
            if i == 51:
                input("CONGRATULATIONS YOU'RE DONE!")
            else:
                input("Press Enter to continue...\n")
        else:
            print("Do {} of {}".format(ac[0], exercise_assignment[ac[2]]))
            if i == 51:
                input("CONGRATULATIONS YOU'RE DONE!")
            else:
                input("Press Enter to continue...\n")
