import time
import os
import colorama
import webbrowser as wb
import random

white = "\u001b[0m"
red = "\u001b[31m"
green = "\u001b[32m"
yellow = "\u001b[33m"
blue = "\u001b[34m"
purple = "\u001b[35m"
cyan = "\u001b[36m"

def cprint(string):
    print(yellow + "[:] " + white + string)
# ---------------------------------------------
def scprint(string):
    print(yellow + "    [:] " + white + string)
# ---------------------------------------------
def cerror(string):
    print(red + "[#] " + white + string)
# ---------------------------------------------
def scerror(string):
    print(red + "    [#] " + white + string)
# ---------------------------------------------
def cinfo(string):
    print(blue + "[?] " + white + string)
# ---------------------------------------------
def scinfo(string):
    print(blue + "    [?] " + white + string)
# ---------------------------------------------
def cnotice(string):
    print(green + "[!] " + white + string)
# ---------------------------------------------
def scnotice(string):
    print(green + "    [!] " + white + string)
# ---------------------------------------------
def wprint(string):
    time.sleep(.02)
    print(yellow + "" + white + string)
# ---------------------------------------------
def swprint(string):
    time.sleep(.02)
    print(yellow + "    [:] " + white + string)
# ---------------------------------------------
def cls():
    os.system("cls")
# ---------------------------------------------
def wait(string): # lol just in case i get mixed up with lua
    time.sleep(string)


cls()
random_messages = ["ram-tester 300", "are you gay?", "christian said brb and died", "can like u not", "1v1 brawlhalla"]
cmds = ["cmds", "ram"]
print(red + """                           
█▀█ ▄▀█ █▀▄▀█ ▀█▀ █▀▀ █▀ ▀█▀
█▀▄ █▀█ █░▀░█ ░█░ ██▄ ▄█ ░█░
""")
print(white + f"say {red}[cmds]{white} to display commands.")
print(white + f"{random.choices(random_messages)}")

def ramtest():
    cmd = input(red + ">" + white)
    if cmd.lower() == cmds[0]:
        cls()
        print(red + """                           
        █▀█ ▄▀█ █▀▄▀█ ▀█▀ █▀▀ █▀ ▀█▀
        █▀▄ █▀█ █░▀░█ ░█░ ██▄ ▄█ ░█░
        """)
        print(white + f"{random.choices(random_messages)}")
        print("")
        print("")
        print(f"""
        {red}0: {cmds[0]} {white} - displays cmds
        {red}1: {cmds[1]} {white} - test your ram
        """)
        ramtest()
    elif cmd.lower() == cmds[1]:
        cls()
        print(red + """                           
        █▀█ ▄▀█ █▀▄▀█ ▀█▀ █▀▀ █▀ ▀█▀
        █▀▄ █▀█ █░▀░█ ░█░ ██▄ ▄█ ░█░
        """)
        print(white + f"{random.choices(random_messages)}")
        print("")
        print("")
        cinfo("Enter the amount of webpages you wish to open")
        scerror("MUST BE IN NUMERAL FORM")
        amount = int(input(f"{red}> {white}"))
        scinfo("opening in (5)seconds, exit if you want")
        wait(5)
        for x in range(amount):
            wb.open("google.com")

        ramtest()

ramtest()