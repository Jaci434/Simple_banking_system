from random import randint
import SBS_database

connection = SBS_database.connect()

SBS_database.create_tables(connection)


class CreditCard:
    IIN = 400000
    card_informations = []

    def __init__(self):
        self.costumer_number = None
        self.checksum = None
        self.card_number = None
        self.pin_number = None
        self.balance = 0
        
     #Luhn algorthem to check if the card number is valid
    def luhn_algorithem(self, number_card):
        put_to_list = list(map(int, number_card))
        num = 0
        luhn_check = []
        position = 1
        for num in put_to_list:
            if position % 2 != 0:
                num *= 2
                luhn_check.append(num)
                position += 1
            else:
                num = num
                luhn_check.append(num)
                position += 1 
        luhn_check2 = [num1 - 9 if num1 > 9 else num1 for num1 in luhn_check ]

        #calulation of check number(last number of credit card number)
        luhn_sum = 0
        for num2 in luhn_check2:
            luhn_sum += num2 
        roun_num = luhn_sum % 10
        checksum = 10 - roun_num
        return checksum 

    #creating accout(credit card number and pin)
    def creating_account(self):
        
        #credit card number
        self.costumer_number = ''.join([str(randint(0, 9)) for number in range(9)])

        card_number_ = str(CreditCard.IIN) + self.costumer_number
            
        self.checksum = self.luhn_algorithem(card_number_)

        self.card_number = str(CreditCard.IIN) + self.costumer_number + str(self.checksum)
            
        #creating pin number
        self.pin_number = ''.join([str(randint(0, 9)) for number in range(4)])

        #checking if number and pin are right lenght
        if (len(self.card_number) == 16) and (len(self.pin_number) == 4):
            print(f'Your card has been created\nYour card number:\n{self.card_number}\nYour card PIN:\n{self.pin_number}')
        else:
            print("Choose Create an account again.")

        SBS_database.add_card(connection,self.card_number,self.pin_number, self.balance)

    
    #logging into account
    def log_in(self, card_number, pin_number):

        #checking if account exist
        id_card = SBS_database.check_number_in_table(connection, card_number)
        
        if id_card is not None:
            pin = SBS_database.get_pin_by_number(connection, card_number)[0]
            
            #checking if typed pin is same as in database
            if input_pin == pin:
                print("You have successfully logged in!")
                #costumer choose if they want to check balance, enter income, transfer money, delete account, log out or exit the application
                while True: 
                    print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
                    logging_input = int(input()) 
                    #get balance from database
                    self.balance = SBS_database.get_balance_by_number(connection, card_number)[0]

                    #checking the balance of account
                    if logging_input == 1:
                        print(f'Balance: {self.balance}')
                        continue
                        
                    #put money on your account and updating the account balance
                    elif logging_input == 2:
                        income_input = int(input("Enter income: "))
                        self.balance += income_input
                        SBS_database.update_balance(connection, card_number, self.balance)
                        print("Income was added!")

                    #transfering money from your account to other
                    elif logging_input == 3:
                        print("Transfer")
                        transfer_to_card = input("Enter card number: ")
                        check_checksum = self.luhn_algorithem(transfer_to_card[:15])
                        check_id_card = SBS_database.check_number_in_table(connection, transfer_to_card)
                        
                        #checking if card comply with Luhn algorithem
                        if check_checksum != int(transfer_to_card[15]):
                            print("Probably you made a mistake in the card number. Please try again!")
                            continue

                        #checking if input card exist
                        elif check_id_card is None:
                            print("Such a card does not exist.")
                            continue

                        #checking if input card is not same as costumers
                        elif transfer_to_card == card_number:
                            print("You can't transfer money to the same account!")
                            continue
                        
                        #trensfering money to account and updating balance of both accounts
                        else:
                            transfered_amount = int(input("Enter how much money you want to transfer:"))
                            if (self.balance - transfered_amount) > 0:
                                print("Success!")
                                #update costumer account
                                self.balance -= transfered_amount
                                SBS_database.update_balance(connection, card_number, self.balance)

                                #update account where money was transfered
                                transfer_to_card_balance = SBS_database.get_balance_by_number(connection, transfer_to_card)[0]
                                new_transfer_balance = transfer_to_card_balance + transfered_amount
                                SBS_database.update_balance(connection, transfer_to_card, new_transfer_balance)
                                continue
                            else:
                                print("Not enough money!")
                                continue
                    #deleting the account 
                    elif logging_input == 4:
                        SBS_database.delete_card(connection, card_number)
                        print("The account has been closed!")
                        break
                    
                    #logging out
                    elif logging_input == 5:
                        print("You have successfully logged out!")
                        break
                    
                    #leaving the application
                    elif logging_input == 0:
                        print("Bye!")
                        exit()
                    else:
                        print("Invalid option")

            #if pin is wrong           
            else:
                print("Wrong card number or PIN!")
        else:
                print("Wrong card number or PIN!")





while True:

    print("1. Create an account \n2. Log into account \n0. Exit")
    costumer_choice = int(input())

    card = CreditCard()
    #if pressed 1(create an account) it goes to class method creating_account
    if costumer_choice == 1:
        card.creating_account()

    #if pressed 2(Log into account) it goes to class method log_in
    elif costumer_choice == 2:
        input_costumer_number = input("Enter your card number:")
        input_pin = input("Enter your PIN:")
        card.log_in(input_costumer_number,input_pin)

    #if pressed 0(exit from application)
    elif costumer_choice == 0:
        print("Bye!")
        exit()
    else:
        print("Invalid option!")

