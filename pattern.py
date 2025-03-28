import random
from collections import OrderedDict

class Pattern:
    def __init__(self, title):
        self.title = title
        self.rows = OrderedDict()

    def __str__(self):
        pass

    __repr__ = __str__

    def add_row(self, block, row):
        if block not in self.rows:
            self.rows[block] = []
        self.rows[block].append(row)

    def align(self, right_side, title):
        if right_side:
            return
        self.add_row(title, "Purl until end of row.")

used_ideas = set()
def get_title():
    global used_ideas
    ideas = ["Sleeves", "Cuff", "Brim", "Thumb", "Finger", "Back", "Pom Pom", "Side", "Waistband", "Heel", "Toe", "Buttons", "Handles", "Pockets", "Neckline", "Zipper Band"]
    idea = random.choice(ideas)
    while idea in used_ideas:
        idea += " Version 2"
    used_ideas |= {idea}
    return idea