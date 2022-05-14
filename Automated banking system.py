# This is the code written by Parash for the automated new ATM system which can create accounts load the money withdraw money and delete the account itself
def date_time():
    import datetime

    return datetime.datetime.now()


class ATM:
    def __init__(self, lst):
        self.lst = lst
        self.atm_name = "parash ATM"
        self.atm_money = 10000000

    def withdraw(self):
        a = 1
        while a == 1:
            user = input("Enter your name :\n")
            pw = input("Enter your four digit password :\n")
            if user in self.lst and pw in str(self.lst[user]["password"]):
                a = self.lst[user]["balance"]
                c = 1
                while c == 1:
                    print(f"your total balance is {a}$ ")
                    while True:
                        try:
                            amt = int(input("enter the amount you want to withdraw\n"))
                            break
                        except ValueError:
                            print("ENTER THE AMOUNT OF MONEY IN NUMBER:")

                    if a >= amt:
                        balance = a - amt
                        self.atm_money = self.atm_money - amt
                        del self.lst[user]
                        self.lst.update({user: {"balance": balance, "password": pw}})
                        with open(user, "a") as p:
                            p.write(f"You have withdrawn {amt}$ at {date_time()} \n")
                        with open("atm.txt", "a") as a:
                            a.write(f"{user} has withdrawn {amt}$ at {date_time()}\n")
                        print(
                            f"Your remaining balance is {balance}$\nThank you for using our service"
                        )

                        break

                    else:
                        print(f"Sorry insufficient balance:\nYour total balance is {a}")
                        while True:
                            try:
                                a = int(
                                    input("Do you want to try again?\n1.Yes\n2.No\n")
                                )
                                break
                            except ValueError:
                                print("Please enter 1 for yes and 2 for no")
            else:

                print("Either your password or username is wrong :")
                while True:
                    try:
                        c = int(input("Do you want to try again?\n1.Yes\n2.No\n"))
                        break
                    except ValueError:
                        print("Please enter 1 for yes and 2 for no")

    def load_money(self):
        a = 1
        while a == 1:
            user = input("Enter your name :\n")
            pw = input("Enter your four digit password :\n")
            if user in self.lst and pw in str(self.lst[user]["password"]):
                a = self.lst[user]["balance"]
                c = 1
                while c == 1:
                    print(f"your total balance is {a}$ ")
                    while True:
                        try:
                            amt = int(
                                input(
                                    "enter the amount you want to Load in the account\n"
                                )
                            )
                            break
                        except ValueError:
                            print("ENTER THE AMOUNT OF MONEY IN NUMBER:")
                    balance = a + amt
                    self.atm_money = self.atm_money + amt
                    del self.lst[user]
                    self.lst.update({user: {"balance": balance, "password": pw}})
                    with open(user, "a") as p:
                        p.write(f"You have withdrawn {amt}$ at {date_time()} \n")
                    with open("atm.txt", "a") as a:
                        a.write(f"{user} has withdrawn {amt}$ at {date_time()}\n")
                    print(
                        f"Your new balance is {balance}$\nThank you for using our service"
                    )
                    break

                else:
                    print(f"Sorry insufficient balance:\nYour total balance is {a}")
                    while True:
                        try:
                            c = int(
                                input(
                                    "Do you want to try again to withdraw?\n1.Yes\n2.No\n"
                                )
                            )
                            break
                        except ValueError:
                            print("Please enter 1 for yes and 2 for no")
            else:
                print("Either your password or username is wrong :")
                while True:
                    try:
                        a = int(input("Do you want to try again?\n1.Yes\n2.No\n"))
                        break
                    except ValueError:
                        print("Please enter 1 for yes and 2 for no")

    def log_activity(self):
        a = 1
        while a == 1:
            user = input("Enter your name :\n")
            pw = input("Enter your four digit password :\n")
            if user in self.lst and pw in str(self.lst[user]["password"]):
                with open(user, "r") as p:
                    a = p.readlines()
                    for index, item in enumerate(a):
                        print(f"{index}:{item3}")
                break
            else:
                print("Either your password or username is wrong :")
                while True:
                    try:
                        a = int(input("Do you want to try again?\n1.Yes\n2.No\n"))
                        break
                    except ValueError:
                        print("Please enter 1 for yes and 2 for no")

    def private_activity(self):
        a = 1
        while a == 1:
            user = input("Enter private name :\n")
            pw = input("Enter the four digit password :\n")
            if user == "private" and pw == "1234":
                print(f"The remaining amount in atm is {self.atm_money}")
                with open("atm.txt", "r") as p:
                    a = p.readlines()
                    for index, item in enumerate(a):
                        print(f"{index}:{item}")
                break
            else:
                print("Either your password or username is wrong :")
                while True:
                    try:
                        a = int(input("Do you want to try again?\n1.Yes\n2.No\n"))
                        break
                    except ValueError:
                        print("Please enter 1 for yes and 2 for no")

    def pwchanger(self):
        a = 1
        while a == 1:
            user = input("Enter your name :\n")
            pw = input("Enter your four digit password :\n")
            if user in self.lst and pw in str(self.lst[user]["password"]):
                while True:
                    try:
                        newpw = int(input("Enter your new four digit pin\n"))
                        while len(str(newpw)) != 4:
                            newpw = int(
                                input("YOu must enter only a four digit pin:\n")
                            )
                            break
                        break
                    except ValueError:
                        print("Please enter the number only for your password:")

                balance = self.lst[user]["balance"]
                del self.lst[user]
                self.lst.update({user: {"balance": balance, "password": newpw}})
                with open(user, "a") as p:
                    p.write(
                        f"You have successfully changed your password from {pw} to {newpw} at {date_time()} \n"
                    )
                with open("atm.txt", "a") as a:
                    a.write(
                        f"{user} has successfully changed  password from {pw} to {newpw} at {date_time()}\n"
                    )
                print(
                    f"You have successfully changed your password from {pw} to {newpw}"
                )

            else:
                print("Either your password or username is wrong :")
                while True:
                    try:
                        a = int(input("Do you want to try again?\n1.Yes\n2.No\n"))
                        break
                    except ValueError:
                        print("Please enter 1 for yes and 2 for no")

    def account_creater(self):
        import smtplib
        import random
        import string
        import time

        a = "".join(random.sample(string.digits, 4))
        user = input("Enter the name from which you wanna create your account\n")
        while True:
            try:
                newpw = int(input("Enter your new four digit pin\n"))
                while len(str(newpw)) != 4:
                    newpw = int(input("YOu must enter only a four digit pin:\n"))
                    break
                break
            except ValueError:
                print("Please enter the number only for your password:")
        email = input("Enter your email for verification\n")

        # please enter your gmail and pw here from which you want to send email to users
        Gmail_Id = "dummy@gmail.com"
        Gmail_pw = "dummy16"
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(Gmail_Id, Gmail_pw)
        s.sendmail(
            Gmail_Id,
            email,
            f'subject:"Verification code from ATM"\n\n{a}',
        )
        s.quit()
        print(
            f"the verification code is sent to {email} email id.\n Please double check if you have entered right email address or the code is sent to another email account:"
        )
        code = input(
            "Please enter the verification code below to create your account successfully:\n"
        )
        while code != "q":
            if code == a:
                self.lst.update({user: {"balance": 0, "password": pw}})
                print(
                    f"{user} has created a atm account successfully with balance 0 and your pin is {pw}"
                )
                print(
                    "thank you for creating account in our atm if you want to lodge money you can now easily load money frooption on the home menu:"
                )
                break
            else:
                print("sorry your pin is wrong ")
            code = input("enter code again for creating account or q for quiting it:\n")

    def account_deleter(self):
        a = 1
        while a == 1:
            user = input("Enter your username:\n ")
            pw = input("Enter your four digit pin:\n")
            if user in self.lst and pw in str(self.lst[user]["password"]):
                print(
                    "you have accessed your account successfully :\nWE suggest to check your balance in your account once your account is deleted you cannont access your remaining money anymore :)"
                )
                a = input(
                    "Enter confirm to deleter your account or random words to cancel the confirmation :\n"
                )
                if a.lower == "confirm":
                    del self.lst[user]
                    print("your account is deleted successfully:\n Have a great day :")
                else:
                    print(
                        f"Your account is not deleted because You have entered {a} \nThank you!!!!! "
                    )
            else:
                print("Either your password or username is wrong :")
                while True:
                    try:
                        a = int(input("Do you want to try again?\n1.Yes\n2.No\n"))
                        break
                    except ValueError:
                        print("Please enter 1 for yes and 2 for no")


lst = ATM(
    {
        "shyam": {"balance": 1000, "password": 4545},
        "ram": {"balance": 3000, "password": 5687},
        "parash": {"balance": 5000000, "password": 2345},
        "hari": {"balance": 20000, "password": 2734},
    }
)
if __name__ == "__main__":
    c = "2"
    while c == "2":
        while True:
            try:
                what = int(
                    input(
                        "what do you wanna do :\n1.witdraw money\n2.Load money\n3.wanna se your log activity\n4.private use\n5.change password\n6.create an account\n7.Delete your existing accoung\n8.press 8 to quit\n"
                    )
                )
                break
            except ValueError:
                print("Please enter the numbers Only:")
        if what == 1:
            lst.withdraw()

        elif what == 2:
            lst.load_money()
        elif what == 3:
            lst.log_activity()
        elif what == 4:
            lst.private_activity()
        elif what == 5:
            lst.pwchanger()
        elif what == 6:
            lst.account_creater()
        elif what == 7:
            lst.account_deleter()
        else:
            exit()

        c = input("Do you wanna Quit from the ATM?\n1.yes\n2.No\n")
    print("Thank you for choosing us :")
