# Author: Omeed Tabrizi #
# Course: CSCI 1470.01 #
# Assignment: Term Project Code#
# Algorithm:

#imports system parameters
import sys
# Imports a module to add a pause between lines of text
import time
# Imports a module to play sounds
import winsound

#sleep values
a = 1
b = 2.5
c = 0.5
d = 0.1

required = ("I don't understand")
#############################################################################################################
# The game is in sections, starting with 'intro' #
def intro(): 
    print('\n Every day is the same...\n'
        ' You\'ve desperately tried to save\n'
        ' yourself from the clutches of groundhog day.\n')
    time.sleep(b)
    print(' "I have to find a way to escape this time'
        ' loop!"\n You tell yourself.\n\n')
    time.sleep(b)        
    print(' You look at your surroundings and see that \n'
        ' there is a vehicle in front of you \n'
        ' ...it looks like a really big shoe \n')
    time.sleep(b)
    print()
    print(' You look in the distance and there is a large\n'
        ' structure that is the biggest you\'ve ever'
        ' seen.\n\n')
    time.sleep(b)
    print(' You look down at your wrist and you see\n'
        ' that you still have on your watch\n'
        ' your mother gave you back in 1992')
    time.sleep(b)
    print()
    print('You have three choices:\n'
          '1: You can investigate the really big '
          'shoe-pod.\n'
          '2: You can go explore the really big '
          'building \n'
          '3: Look busy and stare at your watch.\n')
    time.sleep(a)
    #Here are your choices 
    firstChoice = input('What would '
                        'you like to do? (1/2/3): ')
    if firstChoice == '1':
        path1()
    elif firstChoice == '2':
        path2()
    elif firstChoice == '3':
        path3()
    else:
        print(required)
        print(' \n You can\'t do that,',name,'\n')
        time.sleep(a)
        intro()
#############################################################################################################
def path1():
    time.sleep(b)
    print()
    print()
    print()
    print()
    print(' Upon closer inspection the very big \n'
          ' shoe on wheels is a time machine \n'
          ' You know this since you\'ve read the manual\n'
          ' The machine is locked, but it has one of\n'
          ' those keypad things by the door\n'
          ' handle that lets you punch in a combination\n'
          ' to open the pod bay door,', name)
    print()
    print()
    time.sleep(a)
    print(' You guess the combination...')
    combo = '0 0 0 0'
    print()
    for character in combo:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(d)
    print()
    time.sleep(b)
    print()
    print(' Hurray! It worked!')
    print()
    time.sleep(b)
    print(' You climb inside the time machine and you'
          ' find the middle\n console displaying'
          ' a series of strange symbols\n\n '
          ' You make a note of these symbols on a piece'
          ' of paper. \n')
    print()
    time.sleep(b)
    print(' You take a look in the glove compartment\n'
          ' only to find to your dissapointment that there\n'
          ' aren\'t very many gloves.\n\n'
          ' You do however find a note.\n'
          ' It reads:\n')
    time.sleep(b)
    note ='To whom it may concern:\n\nThis is the worst time loop we\'ve come across.\nWe must stop this thing.\nHere are the instructions for the plans to build the device\nThis device will save us all from this\nhorrible abomination of an event.'
    for character in note:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(d)
    print()
    time.sleep(b)
    print()
    print(' Amazing')
    print(' \n And just like that you are one step closer to'
          ' going back home to '
          '  your time on a land, before the future,\n'
          ' underneath the wormhole that gave us more time\n'
          ' to be amazing dinasour people that speak and get busy.')
    time.sleep(a)
    print()
    print(' You must choose a path:\n'
          ' 1: Look busy and look at your watch.\n'
          ' 2: You can go to the big scary structure\n')
    time.sleep(a)
    #choices to make
    secondChoice = input(' What would'
                        ' you like to do?(1/2): ')
    if secondChoice == '1':
        path3()
    elif secondChoice == '2':
        path2()
    else:
        print(required)
        print(' \n No',name,'No.\n')
        time.sleep(a)
        intro()
#############################################################################################################
#def path1_2():

def path2():
    time.sleep(a)
    print()
    print(' Oh my...\n')
    time.sleep(a)
    print(' This place is big, green and slimy.'
          ' You find a man in the corner.\n'
          ' You ask him if he remembers the events of\n'
          ' Yesterday.\n He tells you:' )
    print()
    time.sleep(a)
    print(' Where we are right now there is no yesterday.\n'
          ' There is no tomorrow.'
          ' There is only about a buck fitty and this\n'
          ' here banjo!')
    print()
    time.sleep(a)
    print(' Clearly this toothless old man has lost his marbles...\n')
          
    print(' Would you like to hear a tune?')
    time.sleep(a)
    print('[1]"Yes, I would like to hear your silly song.\n'
          '[2]"No, not today."')
    time.sleep(a)
    #choices to make
    thirdChoice = input(' What would'
                        ' you like to do?(1/2): ')
    if thirdChoice == '1':
        path2_1()
    elif thirdChoice == '2':
        path2_2()
    else:
        print(required)
        print(' \n No',name,'No.\n')
        time.sleep(a)
    print()
    print('hot dog')
    time.sleep(a)
#############################################################################################################
def path2_1():
    time.sleep(a)
    print()
    print(' The old man sings the best song you\'ve ever'
          ' heard in your life ')
    winsound.PlaySound("Eighty.wav", winsound.SND_ASYNC)

    delay = input("press ENTER to finish")
    #winsound.PlaySound(None, winsound.SND_PURGE)
    intro()
#############################################################################################################
def path2_2():
    print()
    print(' You continue on your way to discover that there\n'
          ' is nothing else to do around here.')
    intro()
#############################################################################################################
def path3():
    time.sleep(a)
    print()
    print()
    print(' Your watch is telling you the time and date.\n'
          ' It is 10 PM and the year is 1995.\n\n'
          ' You also see an inscription on the back.\n '
          ' It says:\n\n'
          '         To my one and only son \n'
          '         You are the future.\n'
          '                    Love,\n'
          '                    your mother.')
    print()
    print('You win!')
    quit()
#############################################################################################################
#def path3_1():


#############################################################################################################
# Title Screen #
#title
title ='*************************\n8                       8\n8     Adventure Game    8\n8                       8\n*************************\n\n'
#prints your title one character at a time
for character in title:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
print('"Wuh..wuh..what!!??? Why is every day the same?')
print('How am I going to get out of this one?')
print('Wup wuuuuuuuuup \n')
# When you hit 'Y' or 'y' your game starts. #
startGame = input('Do you want to play? (Y/N): ').lower()
print()
print()
if startGame == 'y':
    # Store user's name #
    name = input('What is your name?\n')
    print('Ok,', name)
    time.sleep(a)
    intro()
else:
    print('Buh-Bye!')
 
