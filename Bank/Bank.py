import random
class Bank:
    def __init__(self, name: str, ifsc: str):
        self.name = name
        self.ifsc = ifsc
        self._user = []
        self.no_of_accounts = len(self._user)
    
    def addUser(self, account):
        self._user.append(account)
    
    

    def getUsers(self):
        count = 1
        for users in self._user:
            print(f"User {users._id}: {users.username}, Balance: {users.getBalance()}")
            count+=1

class BranchBank(Bank):
    def __init__(self, name: str, ifsc: str, branch_name: str):
        super().__init__(name, ifsc)
        self.branch_name = branch_name

class Account(Bank):

    def __init__(self, username: str, bank: Bank):
        self._id = random.randint(1, 100000)                 #create id automatically
        self.username = username
        self._balance = 0
        self.bank = bank
        self.bank.addUser(self)

    def setBalance(self, money: float):
        self._balance += money
    
    def getBalance(self):
        return self._balance
    
if __name__ == "__main__":
    bank =  Bank("ICICI", "ICICI0045")
    account1 = Account("Shreya", bank)
    account2 = Account("Shreyas", bank)
    account3 = Account("Shr", bank)
    account4 = Account("Sunit", bank)
    account1.setBalance(1000)
    newBank = Bank("IDFC", "IDFC10045")
    account2 = Account("Shampa", newBank)
    account2.setBalance(20000.33)


    bank.getUsers()




    branch_bank = BranchBank("SBI", "SBI00001", "Main Branch")
    account3 = Account("Ravi", branch_bank)
    account3.setBalance(5000)

    print("Users in SBI Main Branch:")
    branch_bank.getUsers()