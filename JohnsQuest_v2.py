# This is the game of John's Quest, YOU ARE JOHN
# Made by: Ralph Migals

from time import sleep
from os import system
import os.path
from datetime import datetime
import json

debug = True; #Set this flag to enable debug msgs (mainly systemtype for now) - Kana Inoue

#Set clear screen cmd, as they are system dependant - Kana Inoue
if os.name == 'posix':
    clr="clear"
else: clr="cls"

# Note for later: add a language select choice as well as maybe add latvian?



system(clr)   # clears previous lines before the game
now = datetime.now()
langload = False
print('Please choose the language\nCurrent options are: en (English)')
while langload == False:
    
    clang=input("> ")
    if clang == "en": 
        langload=True
        with open('./data/lang/en.json') as f: lang = json.load(f)
        if debug == True: print(lang['tags']['debug'], lang['debug']['langloaddone'])
    else: print('Please try again.\nCurrent options are: en (English)') 
if debug == True: print(lang["tags"]["debug"], lang["debug"]["systype"], os.name) #print systemtype for debug - Kana Inoue

if os.path.isfile('savedata.txt') == False: #check savedata file - Kana Inoue
    print(lang['tags']['info'], lang['info']['nosave'])
else: print(lang['tags']['info'], lang['info']['foundsave'])

game_data = open('savedata.txt', 'w')
game_data.write(lang["gamedata"]["header"] + now.strftime("%d/%m/%Y %H:%M")+ ":\n\n")

def start_art():
    '''
    this outputs the start art:

    "Welcome to John's quest"
    '''
    print('''
     ----------------------------------------------------------------------------------
    |   __      __       .__                                        __                 |
    |  /  \    /  \ ____ |  |   ____  ____   _____   ____         _/  |_  ____         |
    |  \   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \        \   __\/  _ \        |
    |   \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/         |  | (  <_> )       |
    |    \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >        |__|  \____/        |
    |         \/       \/          \/            \/     \/                             |
    |                                                                                  |
    |       ____.      .__         /\                                            __    |
    |      |    | ____ |  |__   ___)/  ______      ________ __   ____   ______ _/  |_  |
    |      |    |/  _ \|  |  \ /    \ /  ___/     / ____/  |  \_/ __ \ /  ___/ \   __\ |
    |  /\__|    (  <_> )   Y  \   |  \\\\___ \     < <_|  |  |  /\  ___/ \___ \   |  |   |
    |  \________|\____/|___|  /___|  //____ >     \__   |____/  \___/  /____/   |__|   |
    |                       \/     \/      \/        |__|                              |
    |                                                                                  |
     ----------------------------------------------------------------------------------
     ''')

def John():
    'this outputs John'
    print('''
       ___
      |   |
     _|   |_   <--- John
    |_______|
    /       \\
   |  0   0  |
   |         |
   |  \___.  |
    \_______/
        |
 /‾‾‾‾‾‾‾‾‾‾‾‾‾\\
/ /|         |\\ \\
|| |         | ||
|| |         | ||
() |         | ()
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
[NARRATOR] This is John. You are John.
    ''')

 # You insert 'start' to start John's Quest

start_art()
print(lang["start"]["enterusername"])      # enter your username
username = input(lang["tags"]["you"])

game_data.write(lang["gamedata"]["username"])
game_data.write(username)


print(lang["start"]["playfsm"])  # to either skip the narrator's guidence or not

start_reply = input(lang["tags"]["you"])
while str.lower(start_reply) != 'yes' and str.lower(start_reply) != 'no':
    system(clr)
    start_art()
    print(lang["start"]["playfsm"])
    start_reply = input(lang["tags"]["you"])

game_data.write(lang["gamedata"]["fsm"] + start_reply)

print(lang["start"]["gamestart"])
start = input(lang["tags"]["you"])

money = 0

while str.lower(start) != "start":      # Start of the game
    system(clr)
    start_art()
    start = input(lang["start"]["startagain"])

system(clr)

John()                      # shows John

sleep(3)
system(clr)

# actual John reveal        # INTRODUCTION
print(f'''
       ___
      |   |
     _|   |_   <--- John
    |_______|
    /       \\
   |  0   0  |      <HELLO, {username}!>
   |         |
   |  \___.  |
    \_______/
        |
 /‾‾‾‾‾‾‾‾‾‾‾‾‾\\
/ /|         |\\ \\
|| |         | ||
|| |         | ||
() |         | ()
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
''')
print(lang['tags']['narrator'], lang['start']['thisjohn'])
sleep(2)

system(clr)
print(f'''
       ___
      |   |
     _|   |_   <--- John
    |_______|
    /       \\
   |  0   0  |      <HELLO, {username}!>
   |         |      <NICE TO MEET YOU!>
   |  \___.  |
    \_______/
        |
 /‾‾‾‾‾‾‾‾‾‾‾‾‾\\
/ /|         |\\ \\
|| |         | ||
|| |         | ||
() |         | ()
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
''')
print(lang['tags']['narrator'], lang['start']['thisjohn'], "\n")
sleep(2)

print(lang['tags']['narrator'], lang['prestory']['hungrynow'])
sleep(3)
print(lang['tags']['narrator'], lang['prestory']['20dollar'])
sleep(2)
print(lang['tags']['narrator'], lang['prestory']['spendwisely'])
sleep(3)

money = 20     # the narrator was so generous he gave you $20, congrats
health_points = 10

def food_shelf():
    '''
    this outputs a shelf with 4 products:
    banana, cookie, candy, toast
    '''
    print('''
     ----------------------------------------------------------------------------------------------------
    |   _                                  Banana: $1 |                @@@@@@@@@@@@@@@@@   Cookie: $1.50 |
    |  //\\                                            |             @@@@@@@@@   @@@@@@@@@@@              |
    |  V  \\                                           |           @@@@@@@@@@@@@@@@@@@   @@@@@@           |
    |   \  \_                                         |          @@   @@@@@@@@@@@@@@@@@@@@@@@@@@         |
    |    \,'.`-.                                      |         @@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@       |
    |     |\ `. `.                                    |        @@@@@@@@@@   @@@@@@@@       @@@@@@@@      |
    |     ( \  `. `-.                        _,.-:\\   |       @@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@       |
    |      \ \   `.  `-._             __..--' ,-';/   |        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       |
    |       \ `.   `-.   `-..___..---'   _.--' ,'/    |         @@@@@@@@@@@@@@   @@@@@@@@@@@@   @        |
    |        `. `.    `-._        __..--'    ,' /     |          @@@@   @@@@@     @@@@@@@@@@@@@          |
    |          `. `-_     ``--..''       _.-' ,'      |            @@@   @@@@@@@@@@@@@@@@@@@@@           |
    |            `-_ `-.___        __,--'   ,'        |              @@@@@@@@@@@@@@   @@@@@@             |
    |               `-.__  `----"""    __.-'          |                 @@@@@@@@@@@@@@@@@                |
    |                    `--..____..--'               |                                                  |
    |-------------------------------------------------|--------------------------------------------------|
    |                                    Candy: $0.75 |              ___        ___         Toast: $0.75 |
    |          ___      .-""-.      ___               |             (   )______(   )                     |
    |          \  "-.  /      \  .-"  /               |             |  ----------  |                     |
    |           > -=.\/        \/.=- <                |             | |          | |                     |
    |           > -='/\        /\\'=- <                |             | |          | |                     |
    |          /__.-'  \      /  '-.__\\               |             | |          | |                     |
    |                   '-..-'                        |             |  ----------  |                     |
    |                                                 |             ----------------                     |
     ----------------------------------------------------------------------------------------------------
    (_______)                                     (_______)                                      (_______)
    ''')

system(clr)
food_shelf()

print(lang['tags']['narrator'], lang['prestory']['buychoice'])      # It's time to buy something to eat!
product = input(lang["tags"]["you"])

system(clr)

game_data.write('\n' + lang["gamedata"]["selprod"])

if str.lower(product) == 'banana':    # A banana for $1
    money -= 1
    health_points += 10
    print(lang['tags']['narrator'], lang['prestory']['choicebanana'])
    game_data.write(lang["gamedata"]["banana"])
    sleep(3)
elif str.lower(product) == 'cookie':    # A cookie for $1.50
    money -= 1.50
    health_points += 7
    print(lang['tags']['narrator'], lang['prestory']['choicecookie'])
    game_data.write('cookie')
    sleep(3)
elif str.lower(product) == 'candy':    # A candy for $0.75
    money -= 0.75
    health_points += 3
    print(lang['tags']['narrator'], lang['prestory']['choicecandy'])
    game_data.write('candy')
    sleep(3)
elif str.lower(product) == 'toast':    # A toast for $0.75
    money -= 0.75
    health_points += 5
    print(lang['tags']['narrator'], lang['prestory']['choicebread'])
    game_data.write('toast')
    sleep(3)
else:
    print(lang['tags']['narrator'], lang['prestory']['choicenone'])
    game_data.write('-NONE-')
    sleep(3)
    # WILL HAVE A MAJOR FIX

# The dialogue begins : FULL STORY MODE
if str.lower(start_reply) == 'yes':
    print(f'\n[NARRATOR] Anyways, you now have ${money:.2f}. Be sure to save it for later too :)')
    sleep(5)
    print("\n[NARRATOR] Secret..")
    sleep(2)
    print("[NARRATOR] Your amount of health actually depends on what you eat.")
    sleep(5)
    print(f"[NARRATOR] So your health is currently {health_points}/20 HP")
    sleep(4)
    print("\n[YOU] But sir, why do I need those health points for?")
    sleep(5)
    print("\n[NARRATOR] You see my friend..")
    sleep(2)
    print("[NARRATOR] You are on a quest..")
    sleep(2)
    print("[NARRATOR] And your main goal is to defeat BOB!!!")
    sleep(5)
    print("\n[YOU] My evil stepbrother?")
    sleep(2)
    print("\n[NARRATOR] Yes..")
    sleep(2)
    print("[NARRATOR] If you fail to defeat him, the world will have the same fate as you'll have..")
    sleep(5)
    print("\n[YOU] Since when has my stepbrother been like this?")
    sleep(4)
    print("[YOU] Nevermind, probably forever..")
    sleep(4)
    print("[YOU] I guess I have no choice then.")
    sleep(3)
else:
    print(f'\n[NARRATOR] Anyways, you now have ${money}. Be sure to save it for later too :)')
    sleep(5)
    print("\n[NARRATOR] Secret..")
    sleep(2)
    print("[NARRATOR] Your amount of health actually depends on what you eat.")
    sleep(5)
    print(f"[NARRATOR] So your health is currently {health_points}/20 HP")
    sleep(4)
    print('\n[NARRATOR] Good luck beating the boss!')
    sleep(3)

system(clr)   # The part where you get into action

def boss_start_art():
    'this shows "START" for bossfight in the game'
    print('''
       _____________________________________
      /   _________ __                 __   \\
     /   /   _____//  |______ ________/  |_  \\
    /    \_____  \\\   __\__  \\\_  __ \   __\  \\
    \    /        \|  |  / __ \|  | \/|  |    /
     \  /_______  /|__| (____  /__|   |__|   /
      \         \/           \/             / 
       ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    ''')

def show_sad_ending():
    print('''
    __      __  ______   _    _          __        __   ______   __
    \\ \\    / / |      | | |  | |        |  ‾‾‾_   |  | |      | |  ‾‾‾_
     \\ \\  / /  | |‾‾| | | |  | |        | |‾‾\\ \\   ‾‾  | |‾‾‾‾  | |‾‾\\ \\
      \\ \\/ /   | |  | | | |  | |        | |   | | |‾‾| | |____  | |   | |
       \\  /    | |  | | | |  | |        | |   | | |  | |      | | |   | |
        ||     | |  | | | |  | |        | |   | | |  | | |‾‾‾‾  | |   | |
        ||     | |__| | | |__| |        | |___| | |  | | |____  | |___| |
        ||     |      | |      |        |       | |  | |      | |       |
        ‾‾      ‾‾‾‾‾‾   ‾‾‾‾‾‾          ‾‾‾‾‾‾‾   ‾‾   ‾‾‾‾‾‾   ‾‾‾‾‾‾‾ 
    ''')

system(clr)
boss_start_art()
print('\n<TO START FIGHTING BOB, ENTER "START">')
boss_start = input('[YOU] ')

while str.lower(boss_start) != 'start':
    print('<ENTER "START" AGAIN>')
    boss_start = input('[YOU] ')

strength_points = 2         # you give BOB -2 HP
BOB_HP = 30                 # BOB has 30 HP
BOB_strength_points = 4     # BOB gives -4 HP to you

def boss_stage():
    'this outputs the boss stage with John and BOB in'
    print(f'''
     ___________________________________________________________________________________________________
    |        Money: {money:.2f}/20 dollars                                                                     |
    |        HP: {health_points:2d}/20                                          HP: {BOB_HP:2d}/30                               |
    |           ___                                                                                     |
    |          |   |                                                                                    |
    |         _|   |_   <--- John                                _______                                |
    |        |_______|                                          /\\   /  \\    <--- BOB                   |
    |        /  \\   /\\                                         | 0\\ /0   |                              |
    |       |   0\\ /0 |                                        |         |                              |
    |       |         |                                        |   ___.  |                              |
    |       |  .____  |                                         \_______/                               |
    |        \_______/                                              |                                   |
    |            |                                          /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\\                          |
    |     /‾‾‾‾‾‾‾‾‾‾‾‾‾\\                                  /  /|          |\\  \\                         |
    |    / /|         |\\ \\                                /  / |          | \\  \\                        |
    |    || |         | ||                                | |  |          |  | |                        |
    |    || |         | ||                                | |  |          |  | |                        |
    |    () |         | ()                               (___) |          | (___)                       |
    |===================================================================================================|
    | Name: John                                    | Name: BOB                                         |
    | {health_points:2d}/20 HP                                      | {BOB_HP:2d}/30 HP                                          |
    |                                               |                                                   |
    | Strength:                                     | Strength:                                         |
    | {strength_points} per damage                                  | {BOB_strength_points} per damage                                      |
    |                                               |                                                   |
     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        Type <A> to attack!        Type <B> to buy random armor!          Type <N> to block attack!
                                            (for $7.00)
    ''')

system(clr)
boss_stage()

game_data.write('\n\nALL PLAYER BOSSFIGHT COMBOS:\n')

def A_choice():
    'ATTACK BOB!!'
    global BOB_HP  # for access to the variable in and out the function
    global health_points

    BOB_HP -= strength_points
    health_points -= BOB_strength_points
    print('\nYou attacked BOB!! His HP dropped by', strength_points)
    sleep(1.5)
    print('BOB attacked you back!! Your HP dropped by', BOB_strength_points)
    sleep(1.5)
    system(clr)
    boss_stage()

def B_choice():
    'BUY ARMOR AND BOOST YOUR STRENGTH POINTS!!'
    global money
    global strength_points
    global BOB_strength_points
    global health_points

    if money >= 7:
        strength_points += 2
        money -= 7
        BOB_strength_points -= 1
        health_points -= BOB_strength_points
        print(f'\nYou bought a piece of armor!')
        sleep(1.5)
        print(F'BOB gives you -{BOB_strength_points} damage')
        sleep(2)
    else:
        health_points -= BOB_strength_points
        print("\nYou don't have enough money left.")
        print('BOB attacked you! Your HP dropped by', BOB_strength_points)
        sleep(4)
        
    system(clr)
    boss_stage()

def N_choice():
    "BLOCK BOB'S ATTACKS!!!!"
    global strength_points
    global health_points

    if strength_points > 0:
        strength_points -= 1
        print("\nYou blocked BOB's attack!")
        sleep(1.5)
        print('But you became weaker after his hit..')
        sleep(1.5)
        print('Your strength points has gone down by', 1)
        sleep(1.5)
    else:
        health_points -= BOB_strength_points
        print("\nYou don't have enough strength left.")
        print('BOB attacked you! Your HP dropped by', BOB_strength_points)
        sleep(4)
    
    system(clr)
    boss_stage()

while BOB_HP > 0:       # while BOB is alive, you choose between 3 of them
    choice = input('<CHOOSE AN ACTION> ')
    if str.upper(choice) == 'A':
        A_choice()
        game_data.write('A   ')
    if str.upper(choice) == 'B':
        B_choice()
        game_data.write('B   ')
    if str.upper(choice) == 'N':
        N_choice()
        game_data.write('N   ')
    
    # Sad ending..
    if health_points <= 0:

        game_data.write('\n\nRECEIVED: a sad ending')

        system(clr)
        show_sad_ending()
        skip = input('\n\n<PRESS "ENTER" TO CONTINUE> ')
        system(clr)
        break           # allows me to exit the loop

    # VICTORY!!!!!!!!!!!!!!!!!!!!!!!!!
    elif BOB_HP <= 0:

        game_data.write('\n\nRECEIVED: a good ending')

        system(clr)
        print('''
      ___
     |   |
    _|   |_
   |_______|
   /       \\
  |  0   0  |      <YOU WIN!!!!!>
  |         |
  |  \___.  |
   \_______/
       |
 /‾‾‾‾‾‾‾‾‾‾‾‾‾\\
/ /|         |\\ \\
|| |         | ||
|| |         | ||
() |         | ()
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        ''')
        sleep(4)
        system(clr)

        print(f'''
      ___
     |   |
    _|   |_
   |_______|
   /       \\
  |  0   0  |      <YOU WIN!!!!!>
  |         |      <THANK YOU SO MUCH FOR PLAYING MY GAME, {username}!>
  |  \___.  |
   \_______/
       |
 /‾‾‾‾‾‾‾‾‾‾‾‾‾\\
/ /|         |\\ \\
|| |         | ||
|| |         | ||
() |         | ()
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        ''')
        sleep(4)
        end_enter = input('<PRESS "ENTER" TO CONTINUE> ')
        system(clr)

game_data.close()   # stops and closes the text file