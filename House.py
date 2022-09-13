items = ["the house that Jack built.", 
         "the malt",
         "the rat",
         "the cat",
         "the dog",
         "the cow with the crumpled horn",
         "the maiden all forlorn",
         "the man all tattered and torn",
         "the priest all shaven and shorn",
         "the rooster that crowed in the morn",
         "the farmer sowing his corn",
         "the horse and the hound and the horn"]
verb = ["is", 
        "lay in",
        "ate",
        "killed",
        "worried",
        "tossed",
        "milked",
        "kissed",
        "married",
        "woke",
        "kept",
        "belonged to"]
def recite(start_verse, end_verse):
    rhyme = []
    for verses in range(start_verse, end_verse+1):
        verse = ""
        verse = "This " + verb[0] + " " + items[verses-1]
        for iter in range(1, verses):   
            verse += " that " + verb[verses-iter] + " " + items[verses-iter-1]
        rhyme.append(verse)
    return rhyme
    