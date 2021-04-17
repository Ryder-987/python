from microbit import *
heart = Image ('09090:'
               '99999:'
               '99999:'
               '09990:'
               '00900:')
heart1 = Image('00000:'
               '09990:'
               '09990:'
               '00100:'
               '00000:')
heart2 = Image('00000:'
               '00900:'
               '00900:'
               '00000:'
               '00000:')
heart3 = Image('00000:'
               '00000:'
               '00000:'
               '00000:'
               '00000:')
heart4 = Image('90909:'
               '09990:'
               '90009:'
               '09990:'
               '90909:')
heart5 = Image('00000:'
               '00000:'
               '00000:'
               '00000:'
               '00000:')
heart6 = Image('90909:'
               '09990:'
               '90009:'
               '09990:'
               '90909:')

all_hearts = [heart, heart1, heart2, heart3, heart4, heart5, heart6]
display.show(all_hearts, delay=200)