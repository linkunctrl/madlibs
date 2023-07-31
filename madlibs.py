def madlibs():
    story = """
    Once upon a time, in a <adjective> kingdom, there lived a <noun>. 
    This <noun> had always dreamed of becoming a <profession> and traveling to <place>.
    One day, a <adjective> fairy appeared before the <noun> and granted them three <plural_noun> as a reward for their kindness.

    Excitedly, the <noun> packed their bags and set off on a journey to <place>. 
    Along the way, they met a <adjective> <animal> who became their loyal companion.
    They encountered many challenges, but with the help of their new friend, the <noun> overcame each obstacle.

    Finally, they reached <place>, where they found a hidden <noun> filled with <plural_noun>. 
    The <noun> decided to share their discovery with the world, and soon, their name became synonymous with <plural_noun> and <profession>.

    And so, the <noun> lived happily ever after, forever cherishing the memory of their adventures in <place>.
    """
     
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    profession = input("Enter a profession: ")
    place = input("Enter a place: ")
    plural_noun = input("Enter a plural noun: ")
    animal = input("Enter an animal: ")

    # replace placeholders in story with user input 
    story = story.replace("<adjective>", adjective)
    story = story.replace("<noun>", noun)
    story = story.replace("<profession>", profession)
    story = story.replace("<place>", place)
    story = story.replace("<plural_noun>", plural_noun)
    story = story.replace("<animal>", animal)

    print("\nYour madlibs story:\n")
    print(story)

# call function to run all 
madlibs()


