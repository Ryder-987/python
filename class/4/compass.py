from mecrobit import *
compass.calibrate()

while True:
    value = compass.heading()
if (value<=45 or >=314):
    print('N')
elif (value<=46 or >=134):
    print('E')
elif (value<=135 or >=224):
    print('S')
else:
    print('W')