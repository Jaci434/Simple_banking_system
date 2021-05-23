import sqlite3

CREATE_CARDS_TABLE = 'CREATE TABLE IF NOT EXISTS card(id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);'

INSERT_CARD = "INSERT INTO card(number, pin, balance) VALUES(?, ?, ?);"

GET_ALL_CARDS = "SELECT * FROM card;"
NUMBER_IN_DATABASE = "SELECT id FROM card WHERE number = ?;"
GET_PIN_BY_NUMBER = "SELECT pin FROM card WHERE number = ?;"
GET_BALANCE_BY_NUMBER = "SELECT balance FROM card WHERE number = ?;"
UPDATE_BALANCE = "UPDATE card SET balance = ? WHERE number = ?;"
DELETE_CARD = "DELETE FROM card WHERE number = ?;"

def connect():
    #create database
    return sqlite3.connect("card.s3db")

def create_tables(connection):
    #when we run our quiry it ensures it will be save to the file
    with connection:
        #creating table
        connection.execute(CREATE_CARDS_TABLE)

#adding new card to database
def add_card(connection, number, pin, balance):
    with connection:
        connection.execute(INSERT_CARD, (number, pin, balance))

#get all cards in database
def get_all_cards(connection):
    with connection:
        return connection.execute(GET_ALL_CARDS).fetchall()

#checking if card number is in the table
def check_number_in_table(connection, number):
    with connection:
        return connection.execute(NUMBER_IN_DATABASE, (number,)).fetchone()

#getting pin of card number from database
def get_pin_by_number(connection, number):
    with connection:
        return connection.execute(GET_PIN_BY_NUMBER, (number,)).fetchone()

#getting balance of card number from database
def get_balance_by_number(connection, number):
    with connection:
        return connection.execute(GET_BALANCE_BY_NUMBER, (number,)).fetchone()

#updating the balance after change was made
def update_balance(connection, number, balance):
    with connection:
        connection.execute(UPDATE_BALANCE, (balance, number,))

#deleting account
def delete_card(connection, number):
    with connection:
        connection.execute(DELETE_CARD, (number,))