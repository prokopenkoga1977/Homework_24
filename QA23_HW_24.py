# 1) Register:
# - email , login , password

# Email : 
# - must contain “@” and “.”

# Password : 
# - more than 6 symbols 
# - must contain upper and lower -case letters
# - must contain number , or symbols as : “@” , “!” , etc.

# Name : 
# - more or equal to 2 symbols 
# - first letter must be in uppercase 

register_data=[]
is_running = True
is_valid = None
while is_running:
    user_email=input("Enter your email: ")
    user_password=input("Enter your password: ")
    user_name=input("Enter your name: ")
    
    def email_special_symbol_validation():
        global user_email
        if "@" in user_email:
            return True
        else:
            print("Error! email isn't correct")
    
    def email_symbol_validaition():
        global user_email
        if "." in user_email:
            return True
        else:
            print("Error! email isn't correct")

    def password_len_validation():
        global user_password
        if len(user_password)>6:
            return True
        else:
            print("Error! Password isn't incorrect. Password must be more than 6 symbols")

    def password_alphabet_upper_validation():
        global user_password
        if user_password.isupper():
            return False
            print("Error! Password must contain upper letters")
        else:
            return True

    def password_alphabet_lower_validation():
        global user_password
        if user_password.islower():
            return False
            print("Error! Password must contain lower letters")
        else:
            return True
    
    def password_number_special_symbol_validation():
        global user_password
        if user_password.find("0, 1, 2, 3, 4, 5, 6, 7, 8, 9, @, $, %, ?. !"):
            return True
        else:
            print("Error! Password must contain at least one number and a special symbol")

    def name_len_validation():
        global user_name
        if len(user_name)>=2:
            return True
        else:
            print("Error! Name must be more or equel to 2 symbols")

    def name_first_latter_validation():
        global user_name
        if user_name.istitle():
            return True
        else:
            print("Error! First letter must be uppercase")

    def registration(user_email, user_password, user_name, register_data):
        global is_valid
        global is_running

        is_valid_email_special_symbol=email_special_symbol_validation()
        is_valid_email_symbol=email_symbol_validaition()
        is_valid_password_len=password_len_validation()
        is_valid_password_alphabet_upper=password_alphabet_upper_validation()
        is_valid_password_alphabet_lower=password_alphabet_lower_validation()
        is_valid_password_number_special_symbol=password_number_special_symbol_validation()
        is_valid_name_len=name_len_validation()
        is_valid_name_first_latter=name_first_latter_validation()

        if is_valid_email_special_symbol and  is_valid_email_symbol and is_valid_password_len and is_valid_password_alphabet_upper and  is_valid_password_alphabet_lower and is_valid_password_number_special_symbol and is_valid_name_len and is_valid_name_first_latter:
            is_valid = True
            register_data.append({
                "Email" : user_email,
                "Password" : user_password,
                "Name" : user_name
            })
            is_valid = False

    registration(user_email, user_password, user_name, register_data)
    user_choose = int(input("1) Exit 2) Continue  "))
    if user_choose == 1:
        is_running = False
print(register_data)

# 2) Practice with me -> Look at last lesson (04.03.2023)


# 1) Context menu : a) All products b) Buy product c) Registration d) Auth e) Balance q) Quit
#  product - manufacturer , label , price , date
# Dict -> object
# {
#    "key" : "value"
# }
# a)  All products - print all products into the console
# []
# b) cart -> history of user shopping
# user = { "login" , "password" , "money" , "money_transfer"}
# c)  - register / auth
# q)  - quit
# buy car
# money_transfer
# e) Balance
# b)  Buy product -> if money enough -> buy car -> - money
from datetime import date
def is_exit():
    result = input("Do you wanna quit ? y/n : ")
    return result.lower()
def registration (login , password , balance = 0):
    return {
        "login" : login,
        "password" : password,
        "balance": balance
    }
def show_products (list_of_products):
    for product in list_of_products:
        print("\n")
        print("***********************" + product['label'] + "***********************\n")
        for key , value in product.items() :
            if key == "date":
                print(key + " ====> " + str(value))
                continue
            print(key + " ====> " + value)
def auth (login, password, array_of_users) :
    for users in array_of_users :
        if login == user['login'] :
            password = input("Enter your account's password: ")
            
            if password == user['password'] :
                return [users , True]
            else :
                print("Incorrect password")
        else:
            print("Incorrect login")

def get_balance (account) :
    print("[USER_BALANCE]", current_user['balance'], "Y.E.")



def money_transfer (account) :
    card_number = input("Enter your card number : ")
    card_date = input("Enter your card date : ")
    card_cvv = input("Enter your card cvv : ")
    
    if len(card_number) == 19 and "/" in card_date and len(card_cvv) == 3:
        money = input("How much money do you want to send? : ")
        account['balance'] = int(account['balance']) + int(money)
        print(f"Congratulations now your balance is : {str(account['balance'])} Y.E.")
    else:
        print("Error! Enter correct card details")
    

def buy_car (target , list_of_products) :
    for product in list_of_products:
        if target.lower() == product['label'].lower():
            sliced_price = product['price'].find("y")
            current_user['balance'] = current_user['balance'] - int(product['price'][:sliced_price - 1])
    print(f"After you bought the car there is left {str(current_user['balance'])} on your balance")
    

products = [
    {
        "manufacturer" : "Czech Republic",
        "label" : "Skoda",
        "price" : "30000 y.e",
        "date" : date(2023,11,1),
        "category" : "sedan"
    },
    {
        "manufacturer": "Italy",
        "label": "Fiat",
        "price": "20000 y.e",
        "date": date(2021, 6, 1),
        "category" : "sedan"
    },
    {
        "manufacturer": "Germany",
        "label": "BMW",
        "price": "10000 y.e",
        "date": date(2002, 8, 1),
        "category" : "crossover"
    },
    {
        "manufacturer": "Germany",
        "label": "MB",
        "price": "20000 y.e",
        "date": date(2012, 12, 2),
        "category" : "sedan"
    },
    {
        "manufacturer": "Germany",
        "label": "VW",
        "price": "10000 y.e",
        "date": date(2011, 12, 2),
        "category" : "truck"
    },
    {
        "manufacturer": "Italy",
        "label": "Alfa Romeo",
        "price": "10000 y.e",
        "date": date(2021, 6, 12),
        "category" : "crossover"
    },
]
is_running = True
is_registred = False
users = [
    {
        "login" : "admin",
        "password" : "admin",
        "balance" : "1200"
    }
]
current_user = {}
while is_running :
    user_choose = input("""
        a) Show products 
        b) Buy product 
        c) Register
        d) Auth
        e) Balance
        q) Quit
        
    Answer : """).lower()
    if user_choose == "a" :
        show_products(products)
    elif user_choose == "b":
        show_products(products)
        prefer_car = input("Choose car that you want buy: ")
        buy_car(prefer_car ,products)
    elif user_choose == "c":
        login = input("Enter login that you want to use continuously : ")
        password = input("Enter your password : ")
        user = registration(login ,password)
        users.append(user)
        print(users)
    elif user_choose == "d":
        login = input("Enter your account's login : ")
        result = auth(login, password, users)
        current_user , is_registred = result
        print(current_user)
        print(is_registred)
    elif user_choose == "e":
        if not is_registred :
            print("Error!")
            continue
        user_choose = input("""
            1) Look at bill
            2) Transfer by card 
        """)
        if user_choose == "1" :
            if is_registred == True :
                get_balance(current_user)
            else :
                print("You should to have an account to look at balance")
        elif  user_choose == "2":
            money_transfer(current_user)
    elif user_choose == "q":
        result = is_exit()
        if result == "y" :
            is_running = False