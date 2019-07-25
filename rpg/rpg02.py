#!/usr/bin/python3
'''My RPG Game in my NAPYA Class'''

def showInstructions():
    print('''
    RPG Game 
    --------
    Commands:
        go [direction]
        get [item]
    ''')

def showStatus(): 
    print('====================')
    print('You are in the ', currentRoom)
    # show inventory
    print('Inventory : ', str(inventory))
    #show item if one is in the room
    if 'item' in rooms[currentRoom]:
        print('You see a ', rooms[currentRoom]['item'])
        print('===============')

# int a empty list
inventory = []

rooms = {
        'Hall' : {
            'south' : 'Kitchen',
            'item' : 'key'
            },
        'Kitchen' : {
            'north' :'Hall'
            }
        }
# player start location
currentRoom = 'Hall'

# show instructions to player
showInstructions()

# create an infinite loop
while True:
    showStatus()
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
          print('You can\'t go that way!')
    
    if move[0] == 'get':
       if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(move[1] + ' got!')
            del rooms[currentRoom]['item']
       else:
            print('Can\'t get' + move[1] + '!')








