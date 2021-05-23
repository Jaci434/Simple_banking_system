Simple banking system: 
	2 python scripts: Simple_banking_system.py and SBS_database (Sqlite functions and quieries)
			
Project using classes and objects, Sqlite3 for Python.

With starting the program, menu open:
1. Create account
2. Log in account
0. Exit

If pressed 1, class CreditCard is called and method creating_account is used. With it we create account with 
16-long card number and 4-long card pin. Account balance is 0 by default.

If pressed 2, class CreditCard is called and method log_in is used. User has to log in the account by type in card number and pin. 
If both is right, submenu is open:
1.Balance
2.Add income
3.Do transfer
4.Close account
5.Log out
0.Exit

	pressed 1: checking the balance on account
	pressed 2: add _ amount of money on the account. Balance in database in updated
	pressed 3: transfer _ amount of money to wished account. Accound card number is checked for complying with luhn algorith,
		if it exist in database, if the account card number is not tha same as user account number. If is al ok, the 
		the user type how much money he wants to transfere. It check if is enough money on user account, and do the transaction.
		Balance of both account are updated
	pressed 4: user want to delete the account. Account is deleted from database
	pressed 5: logging out from account and going in main menu
	pressed 0: exit the program/application

If pressed 0: exit the program/application


Jacinta Mihelcic, march 2021
