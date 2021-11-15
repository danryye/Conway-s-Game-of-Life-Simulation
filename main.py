import random, time, copy

WIDTH = 60
HEIGHT = 20

# Initial list creation and population
nextcells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(' ')
    nextcells.append(column)

# Main loop
while True:
    print('\n\n\n')
    currentcells = copy.deepcopy(nextcells)

    # Prints currentcells
    print('+' + ('-' * WIDTH) + '+')  # Prints outside box
    for y in range(HEIGHT):
        print('|', end='')  # Prints outside box
        for x in range(WIDTH):
            print(currentcells[x][y], end='')  # Prints '#' or ' '
        print('|')  # Prints outside box
    print('+' + ('-' * WIDTH) + '+')  # Prints outside box
    
    # Logic for nextcells based on currentcells placement
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # Tracks neighboring cells
            leftcell  = (x - 1) % WIDTH
            rightcell = (x + 1) % WIDTH
            abovecell = (y - 1) % HEIGHT
            belowcell = (y + 1) % HEIGHT
    
            # counts neightboring cells that are alive
            numofneighbors = 0
            if currentcells[leftcell][abovecell] == '#':
                numofneighbors += 1  # Above left cell is alive.
            if currentcells[x][abovecell] == '#':
                numofneighbors += 1  # Above cell is alive.
            if currentcells[rightcell][abovecell] == '#':
                numofneighbors += 1  # Above right cell is alive.
            if currentcells[leftcell][y] == '#':
                numofneighbors += 1  # Left cell is alive.
            if currentcells[rightcell][y] == '#':
                numofneighbors += 1  # Right cell is alive.
            if currentcells[leftcell][belowcell] == '#':
                numofneighbors += 1  # Below left cell is alive.
            if currentcells[x][belowcell] == '#':
                numofneighbors += 1  # Below cell is alive.
            if currentcells[rightcell][belowcell] == '#':
                numofneighbors += 1  # Below right cell is alive.

            # Sets alive or dead state
            # By the rules of conway's Game of Life, a cell stays alive if
            # it has 2 ir 3 neighboring cells. A dead cell becomes alive if
            # there are 3 neighboring cells. All other cells die or remains dead.
            if currentcells[x][y] == '#' and (numofneighbors == 2 or numofneighbors == 3):
                nextcells[x][y] = '#'  # Cell stays alive
            elif currentcells[x][y] == ' ' and numofneighbors == 3:
                nextcells[x][y] = '#'  # Dead cell becomes alive
            else:
                nextcells[x][y] = ' '  # All other cells die or remain dead.
    time.sleep(2)  # 2 second delay
