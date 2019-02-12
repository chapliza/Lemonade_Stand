#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 12:56:00 2018

@author: Liza


"""

"""
DocString:
    
You decided to earn some pocket money and you are opening your own business!
Lemonade stand!!!
Your Mom gives you $100 as a startup capital and supplies you with water and sugar. 

To produce lemonade you still need:
1. Lemons ($3 per lemon)
2. Cups ($1 per cup)
You can buy these supplies in the store.

After buying the supplies you will need and set up your lemonade price. 
Note that the higher the price, the less lemonades you will be able to sell.

Goal: to earn as much money as you can to pay your Mom's investment back and, probably,
to buy a bike for $150 afterwards. Good luck!
 
To start playing run this file (F5) and then run game_start() in the console

"""

#from sys import exit
my_answer = input('Would you like to play? (YES/NO)\nYour answer: ').lower()
if 'yes' in my_answer:
    game_start()
else:
    print(f'\nThank you for your interest! Have a nice day!')

def game_start() :
    
    global player_name

    print('\nWelcome to your future \n')
    #ANSI Shadow
    print('██╗     ███████╗███╗   ███╗ ██████╗ ███╗   ██╗ █████╗ ██████╗ ███████╗\n'+
          '██║     ██╔════╝████╗ ████║██╔═══██╗████╗  ██║██╔══██╗██╔══██╗██╔════╝\n'+
          '██║     █████╗  ██╔████╔██║██║   ██║██╔██╗ ██║███████║██║  ██║█████╗  \n'+
          '██║     ██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║██╔══██║██║  ██║██╔══╝  \n'+
          '███████╗███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║  ██║██████╔╝███████╗\n'+
          '╚══════╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚══════╝\n\t\t\t\t\t'+

'███████╗████████╗ █████╗ ███╗   ██╗██████╗\n\t\t\t\t\t'+ 
'██╔════╝╚══██╔══╝██╔══██╗████╗  ██║██╔══██╗\n\t\t\t\t\t'+
'███████╗   ██║   ███████║██╔██╗ ██║██║  ██║\n\t\t\t\t\t'+
'╚════██║   ██║   ██╔══██║██║╚██╗██║██║  ██║\n\t\t\t\t\t'+
'███████║   ██║   ██║  ██║██║ ╚████║██████╔╝\n\t\t\t\t\t'+
'╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ \n')
    
  
    player_name = input("What is your name? \n> ")
    
    investment = 100
    
    print('<----------------------------------------------------------------------------->\n'+
            f'Ok, {player_name}, you have just received a ${investment} investment from\n'+
          'your Mom to open a lemonade stand.\n'+
          'Go to the store to buy the necessary supplies.\n'+
          '<----------------------------------------------------------------------------->\n') 
    at_the_store(investment,0,0)
    
def at_the_store(balance, cup_number, lemon_number):
 
#Check if you have any money when entering the store    
    if balance == 0 and cup_number == 0 and lemon_number == 0 :
        print('<----------------------------------------------------------------------------->\n'+
              '\nYou have no cups or lemons left :(\n'
             'More upsetting is that you have $0 in your account.'+
             '<----------------------------------------------------------------------------->\n')
        input('<Press Enter to continue>\n')
        fail()
        
    input('<Press Enter to continue>\n')
    
# At_the_store: Buy lemons and cups at the store
# You entered the store with your investment and possible leftovers of cups or lemons
# from previous rounds
    
    in_the_store = True
    
    remaining_balance = balance
    cup_qty = cup_number
    lemon_qty = lemon_number
    
    print('<----------------------------------------------------------------------------->\n'
            +'You are in the store. To produce 1 lemonade you need 1 lemon and 1 cup.\n')
    print(f'Your current balance is ${balance}. Buy an optimal amount of cups and lemons\n'+
          'to produce as many lemonades as you can.\n'+
          '<----------------------------------------------------------------------------->\n') 

    input('\n<Press Enter to continue>\n')

# This loop allows you to shop desirable quantities of lemons and cups, to 
# to empty the cart and to check out

    while in_the_store == True :
        
        print('PRESS:\n\t' +
          '1 to buy cups (1$ each)\n\t' +
          '2 to buy lemons (3$ each)\n\t' +
          '3 to empty your cart and shop again\n\t' +
          '4 to spend all the money on your favorite sweets instead\n\t' +
          '5 to check out and open your lemonade stand')
        
        choice = input('> ')
    
        
        if choice == '1' :
           
            try:  
# Tracking purchases on cups: quantity, price, remaining balance
                cups_bought = int(input('Enter cup quantity: '))
                cup_qty = cup_qty + cups_bought
                cup_price = cups_bought * 1
                remaining_balance = remaining_balance - cup_price
                
# Check for the negative balance
                if remaining_balance < 0 :
                    
                     print(f'Your current balance is ${remaining_balance}!\n' +
                           'Not enought money in your account!\n' +
                          'Please empty your cart and shop again!')
                     
# Subtotal of the purchases            
                else :
                        print('_________________________' +
                                f'\nRemaining balance: ${remaining_balance}')
                        print(f'Cups: {cup_qty}\n' +
                              f'Lemons: {lemon_qty}' +
                              '\n_________________________')
                        input('<Press Enter to continue shopping>\n\n')
            except ValueError :
                print("Invalid entry. Please try again.\n")
                
            in_the_store == True
            
       
        elif choice == '2' :
           
    
            try:
# Tracking purchases on lemons: quantity, price, remaining balance              
                lemons_bought = int(input('Enter lemon quantity: '))
                lemon_qty = lemon_qty + lemons_bought
                lemon_price = lemons_bought * 3
                remaining_balance = remaining_balance - lemon_price

# Check for the negative balance
                if remaining_balance < 0 :
                     print(f'Your current balance is ${remaining_balance}!\n'+
                           'Not enought money in your account!\n'+
                          'Please empty your cart and shop again!')
                     
  # Subtotal of the purchases
                else :
                        print('_________________________'+
                                f'\nRemaining balance: ${remaining_balance}')
                        print(f'Cups: {cup_qty}\n'+
                              f'Lemons: {lemon_qty}'+
                              '\n_________________________')
                        input('<Press Enter to continue shopping>\n\n')
            except ValueError :
                print("\nInvalid entry. Please try again.\n")
                
            in_the_store == True
            
            
        elif choice == '3' :
           
            cup_qty = cup_number
            lemon_qty = lemon_number
            remaining_balance = balance
            in_the_store = True

       
        elif choice == '4' :
            
            in_the_store = False
            fail()
        
        
        elif choice == '5' :
            
            if remaining_balance < 0 :
                
                     print('Your card was declined at the counter. Look, you are tring\n'+
                           f'to overspend ${0-remaining_balance}.\n'+
                           'Maybe empty your cart and shop again?\n\n')
                     in_the_store = True
                     input('<Press Enter to continue shopping>\n')
            else:
                in_the_store = False
                round_2(balance,cup_qty,lemon_qty)
        
        else :
            print("\nInvalid entry. Please try again.\n")
            in_the_store == True
            
#Leave the store
            
########################################################          
#Bonus Dad's jokes: 
# - What does Batman have in his lemonade?
# - Just ice
############
# - What kind of scientist put bubbles in lemonade?
# - A FIZZicist
############
# - Where does the baseball keep its lemonade?
# - In the pitcher!
########################################################

#In round_2 you set the price 
def round_2(balance, cup_qty, lemon_qty) :
    
    remaining_balance = balance - cup_qty - (lemon_qty*3)
    
    if cup_qty > lemon_qty :
        lemonade_qty = lemon_qty
        cup_leftover = cup_qty - lemonade_qty
        lemon_leftover = 0
    else :
        lemonade_qty = cup_qty
        cup_leftover = 0
        lemon_leftover = lemon_qty - lemonade_qty
        
    print('<----------------------------------------------------------------------------->\n'+
            f'In the store you bought {cup_qty} cups and {lemon_qty} lemons.\n'+
          f'You can make {lemonade_qty} lemonades!\n')
    
    print(f'\nNow, you need to set the price. The unit cost was $4, right!?\n'+
          'So, you probably would like to pop it up a bit ;) \n\n'+
          'But note: the higher your price is, the less people would want to buy it.\n'+
          '<----------------------------------------------------------------------------->\n')  
    
    input('<Press Enter to continue>\n')
    
    revenue = sales(lemonade_qty, remaining_balance)
    while revenue == -1: 
        revenue = sales(lemonade_qty,remaining_balance)
    
    input('\n\nSelling ... <Press Enter to continue>\n\n')  
    print(f'Your current revenue: ${revenue}')
    input('<Press Enter to continue>\n') 

# Extra money from your Dad?    
    print('Would you like to earn some easy money? Your Dad just came by.\n'+
          'Finish your Dad\'s joke or give it a good laugh at least!')
    
    answer_1 = input('\nDad: - What does Batman have in his lemonade?\n\n'+
                     'Your answer: ').lower()
    if 'just ice' in answer_1 or 'justice' in answer_1 :
        print('Atta kid! You have just earned extra $100!!!\n')
        revenue = revenue + 100
        print(f'Revenue: ${revenue}\n')
    else :
        print('\n\nDad: - Just ice')
        
    answer_2 = input('\nYour answer *laugh*: ')
    if 'ha' in answer_2 or 'HA' in answer_2 or 'Ha' in answer_2 :
        print('\nYou have just earned extra $20!!!\n')
        revenue = revenue + 20
        print(f'Your current revenue: ${revenue}')
        
    input('<Press Enter to continue>\n')   

#If you did not earn enough and don't want to quit yet - here is the loop for you 
    while revenue <= 250 :
        answer_3 = input('<----------------------------------------------------------------------------->\n'+
                         'Great! Would you like to grow your business and come back to the store?(YES/NO)\n'+
                         '(Note: You will be able to use your cups or lemons leftovers from the previous shopping)\n\n'+
                         '<----------------------------------------------------------------------------->\n'+
                         'Your answer: ').lower()
        if 'yes' in answer_3:
            at_the_store(revenue,cup_leftover,lemon_leftover)
        else:
            break
    
    if revenue <= 250:
        fail()
    else:
        
        print(f'Congratulations! Your final revenue is ${revenue}!\n'+
              'And you are able to buy a bike now! What a kid!')
        repay = input('\nWould you be first willing to pay your Mom back?(YES/NO)\n'+
                              'Your answer: ')
        if 'yes' in repay :
           
            print(f'\nYour final profit is ${revenue-100}!\n'+
                         '\nYou know how to pay your investors back - you may expect a call from Warren Buffett soon ;)')
            answer = input('So, the game is over. Would you like to play again? (YES/NO)\nYour answer: ').lower()
            if "yes" in answer:
                game_start()
            else:
                print(f'\nThank you for playing, {player_name}!!! Have a nice day!')
              
        else:
            print(f'Your final profit is still ${revenue}!\n'+
                          'Not paying your investors back? - You may not expect a call from Warren Buffett any soon ;)')
            answer = input('So, the game is over. Would you like to play again? (YES/NO)\nYour answer: ').lower()
            if "yes" in answer:
                game_start()
                      
            else:
                print(f'\nThank you for playing, {player_name}!!! Have a nice day!')
               
 
# Sales(,) is a helping function that defines the ules of lemonade demand
    
def sales(lemonade_qty, remaining_balance) :

    try:
        lemonade_price = float(input('\nPlease enter your price here: $'))
                
        if lemonade_price >= 0 and lemonade_price < 6 :
            revenue = lemonade_qty*lemonade_price + remaining_balance
            
        elif lemonade_price >= 6 and lemonade_price < 10 :
            revenue = round(lemonade_qty * 0.8 * lemonade_price) + remaining_balance
            print('\n\tNice! Smart and cautious pricing!') 
            
        elif lemonade_price >= 10 and lemonade_price < 20 :
            revenue = round(lemonade_qty * 0.5 * lemonade_price) + remaining_balance
            print('\n\tOoooh, you\'re targetting hipsters!')
                
        elif lemonade_price >= 20 and lemonade_price < 30 :
            revenue = round(lemonade_qty * 0.2 * lemonade_price) + remaining_balance
            print('\n\tYou better be living in a rich neighborhood!')
                
        elif lemonade_price >= 30 and lemonade_price < 70 :
            revenue = lemonade_price + remaining_balance
            print('\n\tToo pricey! Maybe your Dad will buy a cup or two?!')
        
        elif lemonade_price < 0 :
            revenue = -1
            print("\nInvalid entry. Please try again.")
            
        else :
            revenue = remaining_balance
            print('\n\tReally??! You sold none, genious!')
    except ValueError :
            print("\nInvalid entry. Please try again.")
            revenue = -1 
            
    return revenue

#fail function
    
def fail() :
    print(
'███████╗ █████╗ ██╗██╗\n'+   
'██╔════╝██╔══██╗██║██║\n'+     
'█████╗  ███████║██║██║\n'+     
'██╔══╝  ██╔══██║██║██║\n'+     
'██║     ██║  ██║██║███████╗\n'+
'╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝\n')
    
    print('<----------------------------------------------------------------------------->\n'+
          f'Oh, {player_name}!! You don\'t have enough money to pay your investors\n'+
          'and to buy a bike. Your business did not succeed. Try to be more disruptive next time!\n'+
          'GAME OVER\n\n'
          'P.S. There is an exellent MIB (Master of International Business) program at Hult\n'+
          'Check it out to improve your business skills to win this game\n'+
          '<----------------------------------------------------------------------------->\n')
    
    answer = input('Would you like to play again? (YES/NO)\nYour answer: ').lower()
    if "yes" in answer:
        game_start()
    else:
        print(f'\nThank you for playing, {player_name}!!! Have a nice day!')

 
