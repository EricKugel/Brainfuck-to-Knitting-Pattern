import random
from collections import OrderedDict

from fpdf import FPDF

class Pattern:
    def __init__(self, title):
        self.title = f"Cozy {title} {get_title()}"
        self.author = "Eric Kugel with BF to Knitting Pattern"
        self.description = f"This {self.title} is a fun, easy pattern to knit up! The perfect blend of style, comfort, and computation, this little {self.title} will help you compute {title} and look good doing it. This pattern was even algorithmically optimized for maximum coziness and comfiness."
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

    def save(self):
        output = f"{self.title}\nBy {self.author}\n{self.description}\n\n"
        for title, rows in self.rows.items():
            output += title + "\n"
            for i, row in enumerate(rows):
                output += f"\tRow {i + 1}: {row}\n"
            output += "\n"
        with open(f"{self.title}.txt", "w") as file:
            file.write(output)

    def save_to_pdf(self):
        pdf = FPDF()

        pdf.add_page()
        pdf.image("/home/eric/Programming/Python/Brainfuck to Knitting Pattern/src/image.png", x=150, y=10, w=50)

        pdf.set_font("Arial", "B", 24)
        pdf.multi_cell(120, 10, self.title)
        pdf.ln(5)
        pdf.set_font("Arial", size=16)
        pdf.multi_cell(120, 5, f"By {self.author}")
        pdf.ln(5)
        pdf.set_font("Times", size=14)
        pdf.multi_cell(120, text=self.description)
        pdf.ln(20)

        for title, rows in self.rows.items():
            pdf.set_x(10)
            pdf.set_font("Times", "B", size=14)
            pdf.multi_cell(160, 5, text=title)
            pdf.ln(1)
            pdf.set_x(20)
            pdf.set_font("Times", size=12)
            text = "\n".join([f"Row {i + 1}: {row}" for i, row in enumerate(rows)])
            pdf.multi_cell(160, text=text)
            pdf.ln(10)

        pdf.output(f"{self.title}.pdf")

used_ideas = set()
def get_title():
    global used_ideas
    ideas = ["Sleeves", "Cuff", "Brim", "Thumb", "Finger", "Back", "Pom Pom", "Side", "Waistband", "Heel", "Toe", "Buttons", "Handles", "Pockets", "Neckline", "Zipper Band", "Sweater", "Hat", "Socks", "Jacket", "Cardigan", "Scarf", "Coaster", "Dish Cloth", "Pantsuit", "Pants", "Suit", "Suit of Armor", "Mug Cozy"]
    idea = random.choice(ideas)
    while idea in used_ideas:
        idea += " Version 2"
    used_ideas |= {idea}
    return idea