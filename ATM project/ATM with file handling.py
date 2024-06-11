import ast
def Register(a):

    RED = "\033[31m";RESET = "\033[0m"

    def Account_no():
        while True:
            Ac_no = int(input("Enter the account number: "))
            if a and Ac_no in a.keys():
                print(f"{RED}Name already registered !\nEnter another name...{RESET}")
            else:break
        return Ac_no
    key=Account_no()
    a[key] = {"Name":input("Enter u r name : "),
            "Password":input("Enter your password : "),
            "Pin":int(input("Enter your Pin : ")),
            "Balance":0}
    print("Registerd successfully")
    return a

def read():
    with open('spam.txt', 'r') as f:
        a = ast.literal_eval(f.read())
        return a
def write(data):
    with open('spam.txt','w') as file:
        file.write(str(data))

class ATM:
    def __init__(self):

        self.choose()
        self.count = 0

    def choose(self):
        self.a = read()
        print("------------------ATM PROJECT-----------------")
        print("\n1. Login\n2. Register\n")
        n=int(input("Enter u r choise : "))
        if n == 1:
            self.account_no = int(input("Enter your AC no : "))
            if self.account_no in self.a:
                self.current = self.a[self.account_no]
                self.Username = self.current['Name']
                self.Password = self.current['Password']
                self.Pin = self.current['Pin']
                self.balance = self.current['Balance']
                self.Login()
            else:
                print("Invalid Account")
                self.choose()
        elif n==2:
            temp=Register(self.a)
            write(temp)
            self.choose()



    def withdraw(self):
        withdraw_ampunt=int(input("Enter amount to withdraw : "))
        pin=int(input("Enter Your Pin Number : "))
        if pin==self.Pin:
            if self.balance>=withdraw_ampunt:
                print("Your Previous Balance : ",self.balance)
                self.balance-=withdraw_ampunt
                print("Your Balance is ",self.balance)
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Pin Number")
        self.Option()

    def Deposit(self):
        deposit_amount=int(input("Enter Amount to Deposit : "))
        pin=int(input("Enter Your Pin Number : "))
        if pin==self.Pin:
            self.balance+=deposit_amount
            print("Successfully Deposited...")
        else:
            print("PIN is not valid")
        self.Option()

    def Balance(self):
        pin=int(input("Enter Your Pin Number : "))
        if pin==self.Pin:
            print("Your Balance is ",self.balance)
        else:
            print("PIN is not valid")
        self.Option()

    def Change_password(self):
        pin=int(input("Enter Your Pin Number : "))
        if pin==self.Pin:
            current_password=input("Enter your Current Password : ")
            if current_password==self.Password:
                while True:
                    new_password=input("Enter your New Password : ")
                    re_new_password=input("Re-Enter Your New Password : ")
                    if new_password==re_new_password:
                        self.Password=new_password
                        print("Password Changed Successfully")
                        break
                    else:
                        print("Password not matched Re enter again")
            else:
                print("invalid Password")
        else:
            print("invalid PIN")
        self.Option()


    def default(self):
        print("Invalid Option")
        print("Please Reenter Valid option")
        self.Option()
    def Exit(self):
        self.current['Password']=self.Password
        self.current['Balance']=self.balance
        self.a[self.account_no]=self.current
        write(self.a)
        print("THANK YOU")
    def Option(self):
        print("\n")
        print("1    --> Withdraw\n2    --> Deposit\n3    --> Balance\n4    --> Change Password\n5    --> Exit\n")
        self.option = int(input("Enter your Option : "))

        switch_dict = {
            1: self.withdraw,
            2: self.Deposit,
            3: self.Balance,
            4: self.Change_password,
            5: self.Exit
        }
        a = switch_dict.get(self.option, self.default)
        a()


    def Login(self):
        self.U_name = input("Enter your Username : ")

        if self.U_name == self.Username:
            while True:
                self.U_password = input("Enter your Password : ")

                if self.U_password == self.Password:
                    self.Option()
                    break
                elif self.count <= 2:
                    self.count += 1
                    print(f"{self.count} Attempt Done\nOnly   {3 - self.count}  Attempts are availabe")
                if self.count == 3:
                    print("Account blocked..")
                    break



start=ATM()