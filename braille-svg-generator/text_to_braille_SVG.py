import svgwrite
import sys

TEXT_TO_CONVERT = 'Sveiki!'

# check if the script was run with a text argument
if len(sys.argv) > 1:
    TEXT_TO_CONVERT = sys.argv[1]


map = {
    "a": 1,
    "ā": 16,
    "b": 12,
    "c": 14,
    "č": 146,
    "d": 145,
    "e": 15,
    "ē": 156,
    "f": 124,
    "g": 1245,
    "ģ": 12456,
    "h": 125,
    "i": 24,
    "ī": 246,
    "j": 245,
    "k": 13,
    "ķ": 136,
    "l": 123,
    "ļ": 1236,
    "m": 134,
    "n": 1345,
    "ņ": 13456,
    "o": 135,
    "p": 1234,
    "r": 1235,
    "s": 234,
    "š": 2346,
    "t": 2345,
    "u": 34,
    "ū": 346,
    "v": 2456,
    "w": 2456,
    "z": 345,
    "ž": 3456,
    '.': 256,
    ',': 2,
    ';': 23,
    ':': 25,
    '–': 36,
    '/': 34,
    '1': 1,
    '2': 12,
    '3': 14,
    '4': 145,
    '5': 15,
    '6': 124,
    '7': 1245,
    '8': 125,
    '9': 24,
    '0': 245,
    '»': 6

}

def braille_to_svg(text):
    """
    Generates an SVG file representing the braille translation of the given text.

    Args:
    text: The text to translate to braille.
    filename: The name of the SVG file to generate.
    """

    filename = text

    if '!' in filename:
        filename = filename.replace('!', '')

    if ('?' in filename):
        filename = filename.replace('?', '')    

    dwg = svgwrite.Drawing(filename + '.svg', profile='full')
    multiplier = 10
    cell_size = 1.6 * multiplier
    cell_spacing = 2.5 * multiplier
    letter_spacing = 6 * multiplier
    x_offset = cell_spacing
    y_offset = cell_spacing

    # process the text first
    # if there is a number, put a ž before it
    # if there is a capital letter, put a @ before it

    new_text = ""
    for char in text:
        if char.isdigit():
            new_text += 'ž' + char
        elif char.isupper():
            new_text += '»' + char.lower()
        else:
            new_text += char
    text = new_text

    print(text)
    
    
    for i, char in enumerate(text):

        #  get the value from the dict
        if(char in map):
            dots = str(map[char])
            
            #  loop through the code
            for dot in dots:
                cy = y_offset + (int(dot) - 1) % 3 * cell_spacing
                cx = x_offset + (int(dot) > 3) * cell_spacing + (i * letter_spacing)
                dwg.add(dwg.circle(center=(cx, cy), r=cell_size/2, fill='black'))

    # check if the text includes a ? or !
    # if it does, remove them from the string

   

    dwg.save()

braille_to_svg(TEXT_TO_CONVERT) 

