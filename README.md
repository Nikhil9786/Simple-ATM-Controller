# Simple-ATM-Controller

This project can be cloned using git clone https://github.com/Nikhil9786/Simple-ATM-Controller.git

Aim of the project was to build a simple ATM controller which can perform basic functions of an ATM like check balaance, deposit and withdraw money from both saving and checking accounts.

**Python version - 3.7.2**

**Code Details**

There is only one file Simple-ATM-Controller.py
It consists of two classes and a main function
* Class Bank
  * contains bank generator
  * cards and pin can be added with add_entry functions
  * update_account is used to update balances
  * check_pin checks the if the pin is corrct or not

* Class ATM_Controller
  * containst a function which constructs bank obj and cash bin
  * swipe method used ot insert card
  * account sleect gives option to select between checking and savings
  * account_actions defines basic functions of an ATM like see balance, withdraw and deposit money
  * call function is defined to check the functionality of the controller which is very useful for testing
  * for call function user input is required.
 
* Main Function
  * This functions generated a simple controller where if your run the code it will follow the flow as explained below in flow part of the read me file
  * After the controller functions are defined, some test cases are also defined
  * Different bank and controller for it can be created by invoking their constructor
  * actions in the list should bein tuple to succesfuuly run the code

**Running the program**

python3 Simple-ATM-Controller.py

**Flow of the program**

1. Please inser your card - here you will enter the account number i.e. 123456789
2. pin - 1234
3. Chose between the account checking or savings
4. Chose your action - LEave/See Balance/Withdraw/Deposit (these ara case sensitive)
5. After you leave it will show if the test cases passed or failed
