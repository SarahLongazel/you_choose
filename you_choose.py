
def which_story():
    story_choice = input("Would you like a story about \n 1. A haunted house\n 2. Unicorns? ")
    story_choice = int(story_choice)
    if story_choice == 1:
        story_list = [
                "You are walking in the woods and see a haunted house. Do you...? \n 1. Go in. \n 6. Run to the beach.",
                "Entering the house you see... \n 2. Scarecrows \n 3. Monsters",
                "You fight the scarecrows in the house and then the scarecrows get thirsty. \n They drink strawberry-pineanple-blueberry juice and it turns them into broccoli.\n The End.",
                "You fight the monsters and they run away. You get hungry and make pizza. The pizza in magic and it makes you \n 4. Turn smaller \n 5. Ginormous.",
                "You get smaller and people try to eat you because they think you're mice. \n  The End.",
                "You turn ginormous and walk around the neighborhood and the neighbors get scared. \n  The End.",
                "You run to the beach where there are sharks that want to eat you. Do you...? \n 7. Fight the sharks. \n 8. Run away on a motorbike.",
                "You fight the sharks and they swim away. \n The End.",
                "On the motorbike you go buy groceries. You buy grapes and eat them and you turn into grapes. Then people try to eat you \n and then they spit you out and say, 'Eew, human!' Then you turn back into a human. \n The End." 
                ]

    elif story_choice == 2:
        story_list = [
                "You're walking in an enchanted forest and you see a unicorn surrounded by fire. To save the unicorn, do you...?\n 1. Jump over the fire. \n 6. Put the fire out.",
                "You jump over the fire and ride the unicorn out of the fire. You get the unicorn water from \n 2. The Lake. \n 3. A bottle of water.",
                "You and the unicorn fly to the lake and the unicorn gets water because it was hard for the unicorn to breath in the fire. \n The End.",
                "You were holding a bottle of water and you give it to the unicorn. The bottle of water was magic water. \n 4. You drink it, too. \n 5. Just the unicorn drinks it.",
                "You turn into a unicorn and the unicorn turns into you. In a weird whisper it says, 'We switched bodies.' \n The End.",
                "The unicorn turns into Reese's Puffs and you eat it. \n The End.",
                "You put the fire out and the unicorn eats a magic apple. Then the unicorn turns into \n 7. Sprite \n 8. A person.",
                "The unicorn turns into Sprite and you drink it. You grow a horn and a tail. \n The End.",
                "The unicorn turns into a person and you find two other unicorns and they get mad at the person unicorn. \n They start a war with lego people. \n The End."
                ]
    print(story_list[0])

which_story()

def get_action_choice():
    num_choice = input("Type the number of what you'd like to do: ")
    num_choice = int(num_choice)
    return num_choice


# #run the storyline choices based on returned num_choice variable
# def print_storyline():
#     print()

# while num_choice > 9:
#     choice = input("Choose the number of what you want to do: ")

#     if num_choice == 9:
#         break
#     else:
#         convert_choice()
#         continue