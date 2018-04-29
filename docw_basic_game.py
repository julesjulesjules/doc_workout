################################################################################
### DOCW basic_game function
################################################################################
### Julie Gilbert
### 1/21/2018
################################################################################

### default game style

################################################################################

import random
import docw_classes as docw_c

def basic_game():
    exercises = {"cardio" : ["BURPEES", "JUMPING JACKS", "MOUNTAIN CLIMBERS", "HIGH KNEES", "TUCK JUMPS"], "upper" : ["PUSH-UPS", "PULL-UPS", "BACK PUSH-UPS", "Y'S", "T'S", "W'S", "Y'S-T'S-W'S", "PIKE SHOULDER PRESS"],
        "lower" : ["JUMP SPLIT LUNGE", "LUNGES", "AIR SQUAT", "DONKEY KICKS", "BRIDGES", "WALL SIT", "SIDE LUNGE", "PISTOL SQUAT", "SINGLE LEG DEADLIFT", "CALF RAISE"],
        "core" : ["SIT-UPS", "V-UPS", "PLANK", "SIDE PLANK", "BACK PLANK", "FLUTTER KICKS", "BICYCLE CRUNCHES", "SUPERMAN", "INCHWORM", "RUSSIAN TWIST"]}

    suits =  ["DIAMONDS","CLUBS","HEARTS","SPADES"]

    #assign 1 exercise from each category to a suit
    exercise_assignment = {}
    for each_category in exercises:
        suitchoice = random.choice(suits)
        suits.remove(suitchoice)
        exercise_assignment[suitchoice] = random.choice(exercises[each_category])

    for each in exercise_assignment:
        print("If the suit is {} then the exercise to complete is {}".format(each, exercise_assignment[each]))

    print("\n")

    #create deck of cards
    #shuffle it
    workout_deck = docw_c.Deck()
    workout_deck.shuffle()

    for i in range(52):
        action_card = str(workout_deck.pop_card())
        ac = action_card.upper().split()

        print("{}/52\n".format(i+1))

        if ac[0] == "KING":
            print("Do 10 of {}\n".format(exercise_assignment[ac[2]]))
            if i == 51:
                input("CONGRATULATIONS YOU'RE DONE!")
            else:
                input("Press Enter to continue...\n")
        elif ac[0] == "QUEEN":
            print("Do 10 of {}\n".format(exercise_assignment[ac[2]]))
            if i == 51:
                input("CONGRATULATIONS YOU'RE DONE!")
            else:
                input("Press Enter to continue...\n")
        elif ac[0] == "JACK":
            print("Do 10 of {}\n".format(exercise_assignment[ac[2]]))
            if i == 51:
                input("CONGRATULATIONS YOU'RE DONE!")
            else:
                input("Press Enter to continue...\n")
        elif ac[0] == "ACE":
            print("Do 1 of {}\n".format(exercise_assignment[ac[2]]))
            if i == 51:
                input("CONGRATULATIONS YOU'RE DONE!")
            else:
                input("Press Enter to continue...\n")
        else:
            print("Do {} of {}\n".format(ac[0], exercise_assignment[ac[2]]))
            if i == 51:
                input("CONGRATULATIONS YOU'RE DONE!")
            else:
                input("Press Enter to continue...\n")
