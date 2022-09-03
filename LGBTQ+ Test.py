# Wagwan,
# Have you ever felt like the online sex tests aren't accurate, and you need something more accurate?
# If yes, then this is for you.

import os

from pystyle import *
from time import sleep as stfu
from console.utils import set_title

banner = """
██╗      ██████╗ ██████╗ ████████╗ ██████╗     ████████╗███████╗███████╗████████╗
██║     ██╔════╝ ██╔══██╗╚══██╔══╝██╔═══██╗    ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
██║     ██║  ███╗██████╔╝   ██║   ██║   ██║       ██║   █████╗  ███████╗   ██║   
██║     ██║   ██║██╔══██╗   ██║   ██║▄▄ ██║       ██║   ██╔══╝  ╚════██║   ██║   
███████╗╚██████╔╝██████╔╝   ██║   ╚██████╔╝       ██║   ███████╗███████║   ██║   
╚══════╝ ╚═════╝ ╚═════╝    ╚═╝    ╚══▀▀═╝        ╚═╝   ╚══════╝╚══════╝   ╚═╝v1.1
                                                                                  
A simple LGBTQ+ test to find out if you're Gay/Lesbian
Originally retardedly coded by github/shoppingmall69 in 8 lines, revamped by Bloody\n
"""

calculating = """
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗██╗███╗   ██╗ ██████╗          
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██║████╗  ██║██╔════╝          
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║██╔██╗ ██║██║  ███╗         
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║██║╚██╗██║██║   ██║         
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝██╗██╗██╗
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝                                                                                                 
"""

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    os.system('pause >nul')

def pius():
    cls()
    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))
    set_title("LGBTQ+ Test | By: shoppingmall69 | Revamped By: Bloody | Breh")
    Write.Print("Pius. You are the embodiment of gayness.", Colors.green_to_white, interval=0.008)
    pause()

def male():
    set_title("LGBTQ+ Test | By: shoppingmall69 | Revamped By: Bloody | Attraction")
    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))
    Write.Print("NOTE: Please put all answers in CAPS , it's case sensitive.\n", Colors.red_to_yellow, interval=0)
    male_attraction = Write.Input('Are you attracted to females? Write F for female or M for male: ', Colors.red_to_yellow, interval=0.008)
    cls()
    set_title("LGBTQ+ Test | By: shoppingmall69 | Revamped By: Bloody | Calculating")
    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(calculating)))
    stfu(3)

    if male_attraction == 'F':
        cls()
        set_title("LGBTQ+ Test | By: shoppingmall69 | Revamped By: Bloody | Done!")
        print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))
        Write.Print("Either you provided an incorrect answer or you're not Gay.", Colors.green_to_white, interval=0.008)
        pause()
    else:
        cls()
        set_title("LGBTQ+ Test | By: shoppingmall69 | Revamped By: Bloody | Done!")
        print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))
        Write.Print("Either you provided an incorrect answer or you're Gay.", Colors.green_to_white, interval=0.008)
        pause()

def female():
    set_title("LGBTQ+ Test | By: shoppingmall69 | Revamped By: Bloody | Atrraction")
    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))
    Write.Print("NOTE: Please put all answers in CAPS , it's case sensitive.\n", Colors.red_to_yellow, interval=0)
    female_attraction = Write.Input('Are you attracted to males? Write M for male or F for female: ', Colors.red_to_yellow, interval=0.008)
    cls()
    set_title("LGBTQ+ Test | By: shoppingmall69 | Revamped By: Bloody | Calculating")
    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(calculating)))
    stfu(3)

    if female_attraction == 'M':
        cls()
        set_title("LGBTQ+ Test | By: shoppingmall69 | Revamped By: Bloody | Done!")
        print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))
        Write.Print("Either you provided an incorrect answer or you're not Lesbian.", Colors.green_to_white, interval=0.008)
        pause()
    else:
        cls()
        set_title("LGBTQ+ Test | By: shoppingmall69 | Revamped By: Bloody | Done!")
        print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))
        Write.Print("Either you provided an incorrect answer or you're Lesbian.", Colors.green_to_white, interval=0.008)
        pause()

def ask_gender():
    cls()
    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))
    set_title("LGBTQ+ Test | By: shoppingmall69 | Revamped By: Bloody | Gender")
    Write.Print("NOTE: Please put all answers in CAPS , it's case sensitive.\n", Colors.red_to_yellow, interval=0)
    gender = Write.Input("What is your gender?. Write M for male or F for female: ", Colors.red_to_yellow, interval=0.008)
    cls()
    if gender == 'M':
        male()
    else:
        female()

cls()
set_title("LGBTQ+ Test | By: shoppingmall69 | Revamped By: Bloody | Name")
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))
ask_name = Write.Input("What is your name?: ", Colors.red_to_yellow, interval=0.008)



if ask_name == 'Pius':
    pius()
else:
    ask_gender()
