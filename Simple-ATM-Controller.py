# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:32:17 2020

@author: Nikhil Arora
email - nikhilar@buffalo.edu
github - https://github.com/Nikhil9786
linkedin - linkedin.com/in/arora-nikhil/
"""

import sys

class Bank:
    '''
    
    This class consists of functions defining
    different basics of an ATM.
    
    '''
    
    def __init__(self):
        self.bank_data = {}

    def add_entry(self, card_num, pin, account, amt):
        self.bank_data[card_num] = {"pin":pin, "account":{account:amt}}

    def add_account(self, card_num, account, amt):
        if card_num in self.bank_data:
            self.bank_data[card_num]["account"][account] = amt

    def check_pin(self, card_num, entered_pin):
        if card_num in self.bank_data and self.bank_data[card_num]["pin"] == entered_pin:
            return self.bank_data[card_num]["account"]
        else:
            return None

    def update_account(self, card_num, account, amt):
        if self.bank_data[card_num]["account"][account] in self.bank_data[card_num]["account"]:
            self.bank_data[card_num]["account"][account] = amt
            return True
        else:
            return False
    
    def data(self, data):
        data = {}
        data = self.bank_data
        return data


class ATM_Controller:
    '''
    
    Function defines basic functionss of an ATM and
    a __call__ function to check the functionality of the controller
    
    '''
    def __init__(self, bank, cash):
        self.Bank = bank
        self.accounts = None
        self.cash_bin = cash

    def insert_card(self, card_num, pin):
        self.accounts = self.Bank.check_pin(card_num, pin)
        if self.accounts is None:
            return 0, "Invalid Card or Incorrect Pin!"
        else:
            return 1, "Welcome!"

    def account_select(self, acc):
        if acc in self.accounts:
            return True
        else:
            return False

    def account_actions(self, card_num, acc, action, amt=0):
        if action == "See Balance":
            return self.accounts[acc], 1
        elif action == "Withdraw":
            if self.accounts[acc] >= amt and self.cash_bin >= amt:
                new_balance = self.accounts[acc] - amt
                self.accounts[acc] = new_balance
                self.Bank.update_account(card_num, acc, new_balance)
                return self.accounts[acc], 1
            else:
                return self.accounts[acc], 0
        elif action == "Deposit":
            new_balance = self.accounts[acc] + amt
            self.cash_bin += amt
            self.accounts[acc] = new_balance
            self.Bank.update_account(card_num, acc, new_balance)
            return self.accounts[acc], 1
        else:
            return self.accounts[acc], 2
            
    def __call__(self, card_num, pin, acc, action_list):
        leave = False
        while leave is not True:
            v, m = self.insert_card(card_num, pin)
            if v == 0:
                return "Invalid Card or Incorrect Pin!"
            check = self.account_select(acc)
            if check is False:
                return "Invalid Account!"
            for action in action_list:
                if action[0] == "Leave":
                    return "Gracefully departed"
                balance, bit = self.account_actions(card_num, acc, action[0], action[1])
                if bit == 0:
                    continue
                elif bit == 2:
                    return "Invalid action"
                else:
                    continue
            return "Actions completed"

    def cash_info(self):
        print("\ncash in your wallet : ",self.cash_bin, "\n")

if __name__ == "__main__":
    
    '''
    
    Main function coonsisting of basic controls of ATM
    like See Balance, Withdraw and Deposit mone. And 
    this function consists of different test cases.
    
    '''
    if sys.version_info < (3, 7, 2):
        sys.exit("Python version incompatible, Please use Python 3.7.2")

    empty_bank = Bank()
    
    # Generating a simple bank
    card_number1 = 123456789
    pin1 = 1234
    test_bank = Bank()
    test_bank2 = Bank()
    
    test_bank.add_entry(123456789, 1234, "checking", 1000)
    test_bank.add_account(123456789, "savings", 1000)
    
    test_bank2.add_entry(123456789, 1234, "checking", 1000)
    test_bank2.add_account(123456789, "savings", 1000)
    test_bank2.add_entry(987654321, 7321, "checking", 5000)
    test_atm2 = ATM_Controller(test_bank2, 10000)
    
    cash_bin_over_action = [("See Balance", 0), ("Withdraw", 30000)]
    test_atm = ATM_Controller(test_bank, 10000)
    action_list1 = [("See Balance",0), ("Withdraw", 40), ("Withdraw", 1000), ("Deposit", 100)]

    data = {}
    data = test_bank.data(data)

    atm1 = ATM_Controller(test_bank, 10000)
    atm1.cash_info()
    
    #start ATM controller
    print("please insert your card\n")
    r = 0
    while True:
        input_card_num = int(input("card_num : "))
        input_pin = int(input("pin : "))
        print("")
        r = atm1.insert_card(input_card_num, input_pin)[0]
        if r == 0:
            print(atm1.insert_card(input_card_num, input_pin)[1])
            print("please try again")   
            continue
        else:
            print(atm1.insert_card(input_card_num, input_pin)[1])
            print("")
            break
    
    print("account list : \n")
    print(data[card_number1]['account'])
    
    while True:
        acc = input("account : ")
        check = atm1.account_select(acc)
        if check is False:
            print("Invalid Account!")
            print("please try again (checking or savings)")
        else:
            print("\nEntering your", acc, "account now !")
            break
        
    while True:
        amount = 0
        action = input("choose your action : Leave, See Balance, Withdraw, Deposit : ")
        if action == "Leave":
            print("Successfully departed")
            break
        
        elif action == "See Balance" :
            amount = 0
            print("\nBalance : ", atm1.account_actions(input_card_num, acc, action, amount)[0])
            atm1.cash_info()
            
        elif action == "Withdraw":
            input_amount_w = int(input("amount : "))
            atm1.account_actions(input_card_num, acc, action, input_amount_w)
            print("\nBalance : ", atm1.account_actions(input_card_num, acc, action, amount)[0])
            atm1.cash_info()
        elif action == "Deposit":
            input_amount_d = int(input("amount : "))
            atm1.account_actions(input_card_num, acc, action, input_amount_d)
            print("\nBalance : ", atm1.account_actions(input_card_num, acc, action, amount)[0])
            atm1.cash_info()
        else:
            print("\ntry again")
            continue

    '''
    
    Test Cases to check basic functions of an ATM
    
    '''
    
    empty_atm = ATM_Controller(empty_bank, 0)
    valid, message = empty_atm.insert_card(0, 0)
    if valid == 0:
        print("Test Invalid Message on Empty ATM -- PASS")
    else:
        print("Test Invalid Message on Empty ATM -- FAIL")
        
    if test_atm(123456789, 1234, "checking", action_list1) == "Actions completed":
        print("Test Success on Valid ATM -- PASS")
    else:
        print("Test Success on Valid ATM -- FAIL")

    # Test case for whether ATM handles overdraft attempt without crashing
    if test_atm(123456789, 1234, "checking", action_list1) == "Actions completed":
        print("Test Overdraft handling -- PASS")
    else:
        print("Test Overdraft handling -- FAIL")

    # Test case for incorrect PIN number
    if test_atm(987654321, 1234, "checking", action_list1) == "Invalid Card or Incorrect Pin!":
        print("Test Incorrect Pin Number -- PASS")
    else:
        print("Test Incorrect Pin Number -- FAIL")

    # Test case for incorrect Account number
    if test_atm(876504321, 1234, "checking", action_list1) == "Invalid Card or Incorrect Pin!":
        print("Test Incorrect Acc Number -- PASS")
    else:
        print("Test Incorrect Acc Number -- FAIL")

    # Test case for cash bin excess handling on account balance
    if test_atm(123456789, 1234, "checking", cash_bin_over_action) == "Actions completed":
        print("Test cash bin excess handling -- PASS")
    else:
        print("Test cash bin excess handling -- Fail")
    
    # Test case for exit command
    exit_action = [("See Balance", 0), ("Leave", 0)]
    if test_atm(123456789, 1234, "checking", exit_action) == "Successfully departed":
        print("Test exiting -- PASS")
    else:
        print("Test exiting -- Fail")