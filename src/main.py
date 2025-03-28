# Takes ~1000 rows to knit Hello, World!

import sys
import os

from pattern import Pattern, get_title
from collections import OrderedDict

memory = 10
bf = sys.argv[1]
title = os.path.basename(bf).split(".")[0].capitalize()
if len(sys.argv) > 1:
    memory = int(sys.argv[2])

INSTRUCTION_MAP = {">": "'>',", "<": "'<',", "+": "'+',", "-": "'-',", ".": "'.',", ",": "',',", "[": "(", "]": "),"}

brainfuck = ""
with open(bf, "r") as file:
    brainfuck = eval("".join([INSTRUCTION_MAP[char] for char in file.read() if char in INSTRUCTION_MAP]))

pattern = Pattern(title)
setup_row = f"co 1, psm, co 1 st, psm, *co 1 st, pm: repeat from * until {memory + 1} stitches have been cast on. co 1."
pattern.add_row("Body", setup_row)

def do_block(block, pattern, title, next=None):
    right_side = True

    if next:
        pattern.add_row(title, "Knit until end of current row if necessary.")
        right_side = False

    for instruction in block:
        if isinstance(instruction, tuple):
            child_title = get_title()
            child_next = title + " Cuff"
            pattern.align(right_side, title)
            row = f"Knit until special marker. k1. Slip any markers. Knit until next special marker or end of row. Continue to instructions for {child_title}."
            pattern.add_row(title, row)
            row = f"Continue to instructions for {child_next}."
            pattern.add_row(title, row)
            do_block(instruction, pattern, child_title, next=child_next)
            title += " Cuff"
            right_side = False
        else:
            right_side = follow_instruction(instruction, pattern, right_side, title)
    
    if next:
        back = title + " Back"
        pattern.align(right_side, title)
        row = f"Knit until special marker. k1. Slip any markers. Knit until next special marker or end of row. Continue to instructions for {back}."
        pattern.add_row(title, row)
        row = f"Continue to instructions for {next}."
        pattern.add_row(title, row)
        pattern.add_row(back, f"Continue to instructions for {title}.")
    else:
        pattern.add_row(title, "Cast off all stitches.")

def follow_instruction(instruction, pattern, right_side, title):
    if instruction == ">":
        if not right_side:
            pattern.add_row(title, "Purl until end of row.")
            right_side = not right_side
        row = "Knit until special marker. Replace the special marker with a normal marker. Knit until special marker. Knit until normal marker. Replace the normal marker with a special marker. Knit until end of row."
    elif instruction == "<":
        if right_side:
            pattern.add_row(title, "Knit until end of row.")
            right_side = not right_side
        row = "Purl until special marker. Replace the special marker with a normal marker. Purl until special marker. Purl until normal marker. Replace the normal marker with a special marker. Purl until end of row."
    elif instruction == "+":
        row = f"{'Knit' if right_side else 'Purl'} until special marker. {'kfb' if right_side else 'pfb'}. {'Knit' if right_side else 'Purl'} until end of row."
    elif instruction == "-":
        row = f"{'Knit' if right_side else 'Purl'} until special marker. {'k2tog' if right_side else 'p2tog'}. {'Knit' if right_side else 'Purl'} until end of row."
    elif instruction == ".":
        row = f"{'Knit' if right_side else 'Purl'} until special marker. Switch to sc. {'Knit' if right_side else 'Purl'} until special marker. Switch to mc. {'Knit' if right_side else 'Purl'} until end of row."
    elif instruction == ",":
        row = f"{'Knit' if right_side else 'Purl'} until special marker. Cast off all stitches until special marker. Cast on stitches to the desired length between the special markers. {'Knit' if right_side else 'Purl'} until end of row."
    pattern.add_row(title, row)
    right_side = not right_side
    return right_side

do_block(brainfuck, pattern, "Body")
pattern.save_to_pdf()