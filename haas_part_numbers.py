ht_part_number_rules = {
    'type': [1],
    'height': [2,2],
    'construction': [4],
    'color': [5],
    'thickness': [7],
    'outside_skin': [8],
    'outside_treatment': [9],
    'outside_grooving':[10],
    'inside_skin': [12],
    'inside_grooving': [13],
    'length': [15,4],
    'end_stiles': [19],
    'backer_stile_placement': [20]
}

thickness = {'6': '1-3/8', '7': '1-3/4', 'T': '2', '8': '3'}
color = {
    '1': 'Trinar White', 
    '2': 'Trinar Brown', 
    '3': 'Trinar Beige', 
    '4': 'Trinar Polar White', 
    '5': '5', 
    'A': 'Almond', 
    'B': 'Brown', 
    'D': 'Charcole', 
    'E': 'English Oak Woodgrain', 
    'G': 'Gray', 
    'H': 'H', 
    'K': 'Carbon Black', 
    'L': 'L', 
    'N': 'Embossed Ash Woodgrain', 
    'M': 'M',
    'Q': 'American Walnut Woodgrain', 
    'R': 'Bronze (Terratone)', 
    'S': 'Sandstone', 
    'T': 'Sahara Tan', 
    'U': 'U', 
    'W': 'Polar White', 
    'X': 'Embossed Cherry Woodgrain', 
    'Y': 'Cherry Woodgrain', 
    'U': 'Custom'         
    }

stamp = {
    'B': 'CH SHORT DIE, CH SPACE, NO RIBS (61 SERIES)',
    'C': 'CH SHORT DIE, CH SPACE, RIBBED (60 SERIES)',
    'D': 'CH SHORT DIE, OLD STD SPACE, NO RIBS (81 SERIES)',
    'E': 'CH SHORT DIE, OLD STD SPACE, RIBBED (82 SERIES)',
    'F': 'STD DIE, STD SPACE, FRENCH PRESS (90 SERIES)',
    'G': 'CH LONG DIE, CH SPACE, NO RIBS (63 SERIES)',
    'H': 'CH LONG DIE, CH SPACE, RIBBED (64 SERIES)',
    'I': 'FLUSH SECTION, IMPACT STD LITE SPACING (80 & 90 SERIES)',
    'L': 'CH SHORT DIE, RANCH SPACE, NO RIBS (71 SERIES)',
    'M': 'CH SHORT DIE, RANCH SPACE, RIBBED (72 SERIES)',
    'N': 'NO RAISED PANEL',
    'P': 'CH LONG DIE, RANCH SPACE, NO RIBS (73 SERIES)',
    'Q': 'CH LONG DIE, RANCH SPACE, RIBBED (74 SERIES)',
    'R': 'RANCH DIE, RANCH SPACE (70 SERIES)',
    'S': 'STD DIE, STD SPACE, STD PRESS (80 SERIES)',
    'T': 'CH SHORT DIE, STD SPACE, NO RIBS (81 SERIES)',
    'U': 'CH SHORT DIE, STD SPACE, RIBBED (82 SERIES)',
    'V': 'CH SHORT DIE, INTL SPACE, NO RIBS (81 SERIES)',
    'W': 'CH SHORT DIE, INTL SPACE, RIBBED (82 SERIES)',
    'X': 'STD DIE, OLD STD SPACE, (80 SERIES)',
    'Z': 'STD DIE, INTL SPACE, STD PRESS (80 SERIES)'
}

outside_groove = {
    'B': 'CARRIAGE HOUSE SHADOW GROOVE (FLUSH SECTION)',
    'N': 'NO V-GROOVE OR SHADOW GROOVE',
    'S': 'SHADOW GROOVE',
    'V': 'V-GROOVED',   
    'R': 'RANCH/STANDARD SHADOW GROOVE (FLUSH SECTION)'
}