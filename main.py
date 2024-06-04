import time

id_1 = 'name here' # your name or whatever
id_2 = '00110101' # e.g christmas 12252024

# Identification 1 Check
while True:
    print("Identification 1 !!! Please type your full name !!!")
    identity_check_1 = input().upper()
    if identity_check_1 == id_1:
        print("== Identification 1 Complete == ", "Welcome ", identity_check_1)
    else:
        print("== Identification 1 Failed, please try again: ")
        continue

# Identification 2 Check
    print("Identification 2 !!! Please input MM/DD/YYYY no slashes !!!")
    identity_check_2 = input()
    if identity_check_2 == id_2:
        print("== Identification 2 Complete ==")
        time.sleep(1)
        print("Welcome back my creator", id_1, "!! This is your Personal Username & Password Manager Project !!")
        break
    else:
        print("== Identification 2 Failed == please try again")

# Picking which accounts to pull-up
list_of_accounts = [
    "ACCOUNT 1",
    "ACCOUNT 2",
    "ACCOUNT 3",
    "ACCOUNT 4",
    "ACCOUNT 5",
]

for account in list_of_accounts:
    print(f"* {account}")

# List of account details NOTE: capitilize the ACCOUNT 1, ACCOUNT 2 you know what I mean.
account_details = {
    "ACCOUNT 1": "Username: admin | Password 123",
    "ACCOUNT 2": "Username: admin | Password 123",
    "ACCOUNT 3": "Username: admin | Password 123",
    "ACCOUNT 4": "Username: admin | Password 123",
    "ACCOUNT 5": "Username: admin | Password 123"
}

def choose_account():
    while True:
        print("Creator, which account would you like to bring up?")
        account_chosen = input().upper()
        if account_chosen in account_details:
            print(account_details[account_chosen])
            while True:
                print("Creator, would you like me to bring up a different account? Y/N")
                yes_or_no = input().strip().upper()
                if yes_or_no in ['Y', 'YES']:
                    break
                elif yes_or_no in ['N', 'NO']:
                    print("Good bye Creator... Closing Application")
                    time.sleep(3)
                    return
                else:
                    print("Please type (Y or N) or (Yes or No)")
        else:
            print("Creator, unfortunately the account you have entered is not in our database")

choose_account()


