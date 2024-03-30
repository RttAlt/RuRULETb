import keyboard
import random
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

life = True
score = 0
pat = 0

youl = 3
dell = 3

diedcode = 0

dealerm = 0

q = True
w = True

def out_red(text):
    print("\033[31m {}" .format(text))
def out_yellow(text):
    print("\033[33m {}" .format(text))
def out_blue(text):
    print("\033[34m {}" .format(text))

print("RUSSIAN ROULETTE. THE CONSOLE GAME")
print("----------------------------------")
print("Welcome! This is game created in python.")
print("In this game you will have to PLAY FOR LIFE AND DEATH. No mercy! Just you, the text, and despair.")
print("Attention: If he does not write that someone was hit by a cartridge, then it means a blank.")
print("GOOD LUCK.")
input()
print("Welcome. What's your name?")
name = input("> ")

print("Hi,", name, "you are ready?")
print("Press Y to say 'Yes' ")
print("Press N to say 'No' ")
while True:
    if keyboard.read_key() == 'y':
        print("Good. We ready to start.")
        break
    elif keyboard.is_pressed('n'):
        out_red("You are serious? Ok...")
        life = False
        diedcode = 2
        break

while life == True:
    pat = random.randint(0, 10)
    out_yellow("Gun reloaded.")
    print("Your move!")
    print("Score:", score, "; Dealer - ", dell, " lifes,", name, " - ", youl, " lifes.")
    print()
    print("Q - Shot you")
    print("W - Shot Dealer")
    while q == True:
        if keyboard.read_key() == 'q':
            pat = random.randint(0, 10)
            print("You decided to shoot yourself.")
            if pat == random.randint(0, 10):
                youl = youl - 1
                print("The gun went off. You shot yourself, but you survived.")
            q = False
        elif keyboard.is_pressed('w'):
            print("You decided to shoot dealer.")
            if pat == random.randint(0, 10):
                dell = dell - 1
                print("You fired... A real patron! But the dealer survived.")
                break
            q = False

    q = True
    score = score + 1
    if youl <= 0:
        life = False
        diedcode = 1
    out_blue("Continue...")
    print("--------------------------------")
    pat = random.randint(0, 10)
    print("Dealer's move!")
    print("The dealer is thinking about who to shoot...")
    dealerm = random.randint(0, 1)
    if dealerm == 1:
        print("The dealer decided that he would shoot at you.")
        if pat == random.randint(0, 10):
            print("Shot! But... You survived.")
            youl = youl - 1
    elif dealerm == 0:
        print("The dealer decided to take a chance: he shoots himself.")
        if pat == random.randint(0, 10):
            print("Shot! But... he survived.")
            dell = dell - 1
    print("Blank. Press enter to continue.")
    input()
    out_yellow("Continue...")
    print("--------------------------------")
    if dell <= 0:
        print("He doesn't get up. It seems you've won!")
        input()
        quit()

if life == False:
    out_red("The gun went off. You died.")
    if diedcode == 1:
        print("It was fun playing with you. Bye.")
    elif diedcode == 2:
        print("You're very strange. We haven't even started the game...")
    input()
    quit()