class ATM:
    def __init__(self):

        self.Username = ['priya', 'ramya', 'adhithi', 'niyaz']
        self.Password = ['priya@123', 'ramya@456', 'adhithi@789', 'niyaz@111']
        self.Pin = [1234, 2345, 3456, 8999]
        self.count = 0
        self.U_password = ''
        self.option = 0
        self.current_index = 0
        self.balance = 2000
        self.Login()

    def withdraw(self):
        withdraw_ampunt = int(input("Enter amount to withdraw : "))
        pin = int(input("Enter Your Pin Number : "))
        if pin == self.Pin[self.current_index]:
            if self.balance > withdraw_ampunt:
                print("Your Previous Balance : ", self.balance)
                self.balance -= withdraw_ampunt
                print("Your Balance is ", self.balance)
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Pin Number")
        self.Option()

    def Deposit(self):
        deposit_amount = int(input("Enter Amount to Deposit : "))
        pin = int(input("Enter Your Pin Number : "))
        if pin == self.Pin[self.current_index]:
            self.balance += deposit_amount
            print("Successfully Deposited...")
        else:
            print("PIN is not valid")
        self.Option()

    def Balance(self):
        pin = int(input("Enter Your Pin Number : "))
        if pin == self.Pin[self.current_index]:
            print("Your Balance is ", self.balance)
        else:
            print("PIN is not valid")
        self.Option()

    def Change_password(self):
        pin = int(input("Enter Your Pin Number :"))
        if pin == self.Pin[self.current_index]:
            current_password = input("Enter your Current Password : ")
            if current_password == self.Password[self.current_index]:
                while True:
                    new_password = input("Enter your New Password : ")
                    re_new_password = input("Re-Enter Your New Password : ")
                    if new_password == re_new_password:
                        self.Password[self.current_index] = new_password
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

    def UsernameCheck(self, current):
        self.U_password = input("Enter your Password : ")
        self.current_index = current
        if self.U_password == self.Password[current]:
            self.Option()

        elif self.count < 2:
            self.count += 1
            print(f"{self.count} Attempt Done\nOnly   {3 - self.count}  Attempts are availabe")
            self.UsernameCheck(current)
        elif self.count == 2:
            print("Account blocked..")

    def Login(self):
        self.U_name = input("Enter your Username : ")

        if self.U_name not in self.Username:
            print("Invalid Username")
        else:
            for i, value in enumerate(self.Username):
                if value == self.U_name:
                    current_user = i
                    break

            self.UsernameCheck(current_user)


start=ATM()




