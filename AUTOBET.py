import time
import pyautogui
import os 
from colorama import init, Fore
import random

init()


print(Fore.RED + '''

░█████╗░░██████╗░██████╗░███████╗███████╗███╗░░░███╗███████╗███╗░░██╗████████╗
██╔══██╗██╔════╝░██╔══██╗██╔════╝██╔════╝████╗░████║██╔════╝████╗░██║╚══██╔══╝
███████║██║░░██╗░██████╔╝█████╗░░█████╗░░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░
██╔══██║██║░░╚██╗██╔══██╗██╔══╝░░██╔══╝░░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░
██║░░██║╚██████╔╝██║░░██║███████╗███████╗██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░
''')


print(Fore.RED + '''

Created by zZ#4630
Version 1.0.0



                                    Disclaimer!

                      By using this program, you agree to the below:
                 This program cannot be redistributed without permission.
              This program cannot be modified or changed without permission.

                            All Rights Reserved To zZ#4630.
                            

''')

agreement = input("Type I Agree To Continue.(with capitals)")

if agreement == "I Agree":
    os.system('cls' if os.name == 'nt' else 'clear')

    # prompt user to press enter
    print(Fore.RED + '''
    ██████╗░██╗░░░░░░█████╗░██╗░░██╗███████╗██╗░░░░░██╗██████╗░
    ██╔══██╗██║░░░░░██╔══██╗╚██╗██╔╝██╔════╝██║░░░░░██║██╔══██╗
    ██████╦╝██║░░░░░██║░░██║░╚███╔╝░█████╗░░██║░░░░░██║██████╔╝
    ██╔══██╗██║░░░░░██║░░██║░██╔██╗░██╔══╝░░██║░░░░░██║██╔═══╝░
    ██████╦╝███████╗╚█████╔╝██╔╝╚██╗██║░░░░░███████╗██║██║░░░░░
    ╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝╚═╝░░░░░

    ░█████╗░██╗░░░██╗████████╗░█████╗░██████╗░███████╗████████╗
    ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
    ███████║██║░░░██║░░░██║░░░██║░░██║██████╦╝█████╗░░░░░██║░░░
    ██╔══██║██║░░░██║░░░██║░░░██║░░██║██╔══██╗██╔══╝░░░░░██║░░░
    ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██████╦╝███████╗░░░██║░░░
    ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░╚══════╝░░░╚═╝░░░
    ''')

    print("[PRESS ENTER]")
    input()

    # prompt user for bet amount
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
    ██████╗░██╗░░░░░░█████╗░██╗░░██╗███████╗██╗░░░░░██╗██████╗░
    ██╔══██╗██║░░░░░██╔══██╗╚██╗██╔╝██╔════╝██║░░░░░██║██╔══██╗
    ██████╦╝██║░░░░░██║░░██║░╚███╔╝░█████╗░░██║░░░░░██║██████╔╝
    ██╔══██╗██║░░░░░██║░░██║░██╔██╗░██╔══╝░░██║░░░░░██║██╔═══╝░
    ██████╦╝███████╗╚█████╔╝██╔╝╚██╗██║░░░░░███████╗██║██║░░░░░
    ╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝╚═╝░░░░░

    ░█████╗░██╗░░░██╗████████╗░█████╗░██████╗░███████╗████████╗
    ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
    ███████║██║░░░██║░░░██║░░░██║░░██║██████╦╝█████╗░░░░░██║░░░
    ██╔══██║██║░░░██║░░░██║░░░██║░░██║██╔══██╗██╔══╝░░░░░██║░░░
    ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██████╦╝███████╗░░░██║░░░
    ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░╚══════╝░░░╚═╝░░░
    ''')

    more_then_one = input("Would you like to use multiple bet/auto cashout numbers? y/n (if you answer yes, You must seperate the bet/auto cashout numbers using spaces, ex: 1 2 3 4 dont put a comma or period on the last one. or else the code will break. also, dont put any extra spaces. only put it like this. (1 2 3) not like this ( 2 3 4 ))")
    os.system('cls' if os.name == 'nt' else 'clear')
    if more_then_one == "y":
        bet_amount = input("BET AMOUNT: ").split()  
        auto_cashout = input("AUTO CASHOUT NUMB: ").split()
        numbers = [int(n) for n in bet_amount]
        numbers2 = [int(n) for n in auto_cashout]    
        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(2)
        print('''
        ██████╗░██╗░░░░░░█████╗░██╗░░██╗███████╗██╗░░░░░██╗██████╗░
        ██╔══██╗██║░░░░░██╔══██╗╚██╗██╔╝██╔════╝██║░░░░░██║██╔══██╗
        ██████╦╝██║░░░░░██║░░██║░╚███╔╝░█████╗░░██║░░░░░██║██████╔╝
        ██╔══██╗██║░░░░░██║░░██║░██╔██╗░██╔══╝░░██║░░░░░██║██╔═══╝░
        ██████╦╝███████╗╚█████╔╝██╔╝╚██╗██║░░░░░███████╗██║██║░░░░░
        ╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝╚═╝░░░░░

        ░█████╗░██╗░░░██╗████████╗░█████╗░██████╗░███████╗████████╗
        ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
        ███████║██║░░░██║░░░██║░░░██║░░██║██████╦╝█████╗░░░░░██║░░░
        ██╔══██║██║░░░██║░░░██║░░░██║░░██║██╔══██╗██╔══╝░░░░░██║░░░
        ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██████╦╝███████╗░░░██║░░░
        ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░╚══════╝░░░╚═╝░░░
        ''')

        print('Starting.....')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
        ██████╗░██╗░░░░░░█████╗░██╗░░██╗███████╗██╗░░░░░██╗██████╗░
        ██╔══██╗██║░░░░░██╔══██╗╚██╗██╔╝██╔════╝██║░░░░░██║██╔══██╗
        ██████╦╝██║░░░░░██║░░██║░╚███╔╝░█████╗░░██║░░░░░██║██████╔╝
        ██╔══██╗██║░░░░░██║░░██║░██╔██╗░██╔══╝░░██║░░░░░██║██╔═══╝░
        ██████╦╝███████╗╚█████╔╝██╔╝╚██╗██║░░░░░███████╗██║██║░░░░░
        ╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝╚═╝░░░░░

        ░█████╗░██╗░░░██╗████████╗░█████╗░██████╗░███████╗████████╗
        ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
        ███████║██║░░░██║░░░██║░░░██║░░██║██████╦╝█████╗░░░░░██║░░░
        ██╔══██║██║░░░██║░░░██║░░░██║░░██║██╔══██╗██╔══╝░░░░░██║░░░
        ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██████╦╝███████╗░░░██║░░░
        ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░╚══════╝░░░╚═╝░░░
        ''')






        time.sleep(2)
        # Open Google Chrome
        pyautogui.hotkey('winleft', 'r')
        pyautogui.typewrite('chrome')
        pyautogui.press('enter')
        time.sleep(2)




        # Get a list of all open window titles
        titles = pyautogui.getAllTitles()

        # Search for the Chrome window title
        chrome_title = None
        for title in titles:
            if "Chrome" in title:
                chrome_title = title
                break

        # Maximize the Chrome window
        if chrome_title:
            chrome_window = pyautogui.getWindowsWithTitle(chrome_title)[0]
            chrome_window.maximize()
            time.sleep(2)





        # Go to bloxflip
        pyautogui.typewrite('https://bloxflip.com/crash')
        pyautogui.press('enter')
        time.sleep(2)

        # put in bet amount
        pyautogui.click(379, 383)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.typewrite(str(random.choice(numbers)))  # pass the random number directly as an argument
        pyautogui.press('enter')
        time.sleep(2)

        # set up auto cashout  
        pyautogui.click(364, 489)
        pyautogui.typewrite(str(random.choice(numbers2)))  # pass the random number directly as an argument
        pyautogui.press('enter') 

        # the actual bet
        counter = 0
        while True: 
            pyautogui.click(475, 557)
            time.sleep(10)
            counter += 1
            if counter == 3:
                time.sleep(1)
                pyautogui.click(379, 383)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.typewrite(str(random.choice(numbers)))  # pass the random number directly as an argument
                time.sleep(1)
                pyautogui.click(364, 489)
                pyautogui.typewrite(str(random.choice(numbers2)))  # pass the random number directly as an argument
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.press('enter')
                counter = 0
    elif more_then_one == "n":
        bet_amount = input("BET AMOUNT: ")
        auto_cashout = input("AUTO CASHOUT NUMB: ")


        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(2)
        print('''
        ██████╗░██╗░░░░░░█████╗░██╗░░██╗███████╗██╗░░░░░██╗██████╗░
        ██╔══██╗██║░░░░░██╔══██╗╚██╗██╔╝██╔════╝██║░░░░░██║██╔══██╗
        ██████╦╝██║░░░░░██║░░██║░╚███╔╝░█████╗░░██║░░░░░██║██████╔╝
        ██╔══██╗██║░░░░░██║░░██║░██╔██╗░██╔══╝░░██║░░░░░██║██╔═══╝░
        ██████╦╝███████╗╚█████╔╝██╔╝╚██╗██║░░░░░███████╗██║██║░░░░░
        ╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝╚═╝░░░░░

        ░█████╗░██╗░░░██╗████████╗░█████╗░██████╗░███████╗████████╗
        ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
        ███████║██║░░░██║░░░██║░░░██║░░██║██████╦╝█████╗░░░░░██║░░░
        ██╔══██║██║░░░██║░░░██║░░░██║░░██║██╔══██╗██╔══╝░░░░░██║░░░
        ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██████╦╝███████╗░░░██║░░░
        ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░╚══════╝░░░╚═╝░░░
        ''')

        print('Starting.....')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
        ██████╗░██╗░░░░░░█████╗░██╗░░██╗███████╗██╗░░░░░██╗██████╗░
        ██╔══██╗██║░░░░░██╔══██╗╚██╗██╔╝██╔════╝██║░░░░░██║██╔══██╗
        ██████╦╝██║░░░░░██║░░██║░╚███╔╝░█████╗░░██║░░░░░██║██████╔╝
        ██╔══██╗██║░░░░░██║░░██║░██╔██╗░██╔══╝░░██║░░░░░██║██╔═══╝░
        ██████╦╝███████╗╚█████╔╝██╔╝╚██╗██║░░░░░███████╗██║██║░░░░░
        ╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝╚═╝░░░░░

        ░█████╗░██╗░░░██╗████████╗░█████╗░██████╗░███████╗████████╗
        ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
        ███████║██║░░░██║░░░██║░░░██║░░██║██████╦╝█████╗░░░░░██║░░░
        ██╔══██║██║░░░██║░░░██║░░░██║░░██║██╔══██╗██╔══╝░░░░░██║░░░
        ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██████╦╝███████╗░░░██║░░░
        ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░╚══════╝░░░╚═╝░░░
        ''')






        time.sleep(2)
        # Open Google Chrome
        pyautogui.hotkey('winleft', 'r')
        pyautogui.typewrite('chrome')
        pyautogui.press('enter')
        time.sleep(2)




        # Get a list of all open window titles
        titles = pyautogui.getAllTitles()

        # Search for the Chrome window title
        chrome_title = None
        for title in titles:
            if "Chrome" in title:
                chrome_title = title
                break

        # Maximize the Chrome window
        if chrome_title:
            chrome_window = pyautogui.getWindowsWithTitle(chrome_title)[0]
            chrome_window.maximize()
            time.sleep(2)





        # Go to bloxflip
        pyautogui.typewrite('https://bloxflip.com/crash')
        pyautogui.press('enter')
        time.sleep(2)

        # put in bet amount
        pyautogui.click(379, 383)
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.typewrite(bet_amount)
        pyautogui.press('enter')
        time.sleep(2)

        # set up auto cashout  
        pyautogui.click(364, 489)
        pyautogui.typewrite(auto_cashout)
        pyautogui.press('enter')

        # the actual bet
        while True: 
            pyautogui.click(475, 557)
            time.sleep(10)
            time.sleep(1)
            pyautogui.click(379, 383)
else:
    print('Alright, Exitng App.....')
    time.sleep(1.5)
    exit()