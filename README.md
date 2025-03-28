# Brainfuck to Knitting Pattern

This is a program to convert Brainfuck code into knitting patterns, to prove that knitting patterns are turing complete.

This is not made out of love for brainfuck, but because of its simplicity and proven turing-completeness.

This was made as a final project for the UMN Honors Program Knitting (K)nexus.

### Data Representation:
 - Each instruction is represented by one row in the knitting pattern. This could be optimized, but this method stays more true to the actual brainfuck code.
 - Each memory cell is a set of knit stitches, separated by stitch markers.
 - The value of the memory cell is the number of stitches between the markers minus 1.
 - Values are inputted via casting on stitches "to the desired length". All values inputted should be +1.
 - Values are outputted via a secondary color. The output should be read from the bottom up. All values outputted should be -1.
 