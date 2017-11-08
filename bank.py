class Bank(object):
    def __init__(self, BankId, Bankname, Location):
        self.BankId = BankId
        self.Bankname = Bankname
        self.Location = Location


class Customer(Bank):
    def __init__(self,BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo):
        super(Customer, self).__init__(BankId, Bankname, Location)
        self.accounts = {}
        self.CustomerId = CustomerId
        self.AcctNo = AccountNo
        self.Name = Name
        self.Address = Address
        self.PhoneNo = PhoneNo

    def GeneralInquiry(self):
        try:
            x= self.accounts[self.CustomerId]['CustomerId']
            y = self.accounts[self.CustomerId]['Name']
            z = self.accounts[self.CustomerId]['Address']
            p = self.accounts[self.CustomerId]['PhoneNo']
            r = self.accounts[self.CustomerId][self.AcctNo]['accountNumber']
            n = self.accounts[self.CustomerId][self.AcctNo]['AccountBalance']
            print('Bank ID:%s\nBank Name: %s\nBank Location: %s\n' % (self.BankId, self.Bankname, self.Location))
            print('CustomerId: %s\nCustomer_Name: %s\nAddress: %s\nPhoneNo.: %s \n' % (x, y, z, p))
            print('AccountNo: %s\nAccountBalance: %s\n' % (r, n))
            try:
                v = self.accounts[self.CustomerId]['loan']['loanbalance']
                f = self.accounts[self.CustomerId]['loan']['loanType']
                print('Active_Loan: %s\n' % v)
                print('loan Type: %s\n' % f)
            except:
                print('Loan not activated for this Account')
        except:
            print('Account does not exist!')

    def DepositMoney(self, Amount):
        self.Amount = Amount
        if self.Amount > 0:
            self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'] += self.Amount

    def WithdrawMoney(self, amount):
        self.amount = amount
        if 0 < self.amount < self.accounts[self.CustomerId][self.AcctNo]['AccountBalance']:
            self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'] -= self.amount
        else:
            print('Insufficient balance')

    def OpenAccount(self):
        self.accounts[self.CustomerId] = {}
        self.accounts[self.CustomerId]['Name'] = self.Name
        self.accounts[self.CustomerId]['CustomerId'] = self.CustomerId
        self.accounts[self.CustomerId]['Address'] = self.Address
        self.accounts[self.CustomerId]['PhoneNo'] = self.PhoneNo
        self.accounts[self.CustomerId][self.AcctNo] = {}
        self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] = self.AcctNo
        self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'] = 0
        return self.accounts

    def CloseAccount(self):
        del self.accounts[self.CustomerId]

    def ApplyForLoan(self, loanAmount):
        self.loanAmount = loanAmount
        try:
            self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] = self.AcctNo
        except:
            print('Your are not eligible for a loan')
        if self.loanAmount > (1.5 * (self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'])):
            print('Your not eligible')
        else:
            print('Request Successful')

    def RequestCard(self):
        try:
            self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] = self.AcctNo
        except:
            print('Your are not eligible for Card please create an account first!')


class Teller(Customer, Bank):
    def __init__(self, TellerName, TellerId, BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo):
        super(Teller, self).__init__(BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo)
        self.TellerName = TellerName
        self.TellerId = TellerId
        self.BankId = BankId
        self.Bankname = Bankname
        self.Location = Location
        self.AccountNo = AccountNo
        self.Name = Name
        self.Address = Address
        self.PhoneNo = PhoneNo


    def CollectMoney(self,Amount):
        self.Amount = Amount
        if self.Amount > 0:

            self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'] += self.Amount
            print('you have deposited',self.Amount)
        else:
            print('INPUT AMOUNT GREATER THAN ZERO')

    def LoanRequest(self, loanId ,Type,loanAmount):
        self.loanType = Type
        self.loanId = loanId
        self.loanAmount =loanAmount
        try:
            self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] = self.AcctNo
        except:
            print('Your are not eligible for a loan')
        if self.loanAmount > (1.5*(self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'])):
            print('Your not eligible')
        else:
            self.accounts[self.CustomerId]['loan'] = {}
            self.accounts[self.CustomerId]['loan']['loanId'] = self.loanId
            self.accounts[self.CustomerId]['loan']['loanType'] = self.loanType
            self.accounts[self.CustomerId]['loan']['loanbalance'] = -self.loanAmount
            print('loan account has been created!')

    def ProvideInfo(self):
        print('Bank ID:%s\nBank Name: %s\nBank Location: %s\n' % (self.BankId, self.Bankname, self.Location))
        print('Teller Id: %s\nTeller Name: %s\n' % (self.TellerId, self.TellerName))

    def IssueCard(self):
        if self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] == self.AcctNo:
            print('Your request  for card was received and your Card is ready')
        else:
            print('Not eligible for card issuing')


class Account(Customer):
    pass


class Loan(Customer):
    def __init__(self, LoanId, Type, AccountId, BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo):
        super(Loan, self).__init__(BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo)
        self.LoanId = LoanId
        self.Type = Type
        self.AcctNo = AccountId


a1 = Customer('2', 'DFCU', 'KAMPALA', '200', '00200001', 'KALUMBA JONATHAN', 'Entebbe', '0703750666')
a1.OpenAccount()
a1.DepositMoney(30000)
a1.WithdrawMoney(10000)
a1.GeneralInquiry()
a1.ApplyForLoan(5000)

b1 = Customer('2', 'DFCU', 'KAMPALA', '202', '00200002', 'MBAREBAKI ADONIA', 'MAKERERE', '07872111223')
b1.OpenAccount()
b1.DepositMoney(40000)
b1.WithdrawMoney(20000)
b1.GeneralInquiry()
b1.ApplyForLoan(10000)

c1 = Customer('2', 'DFCU', 'KAMPALA', '203', '00200003', 'MALIAN UMTONI', 'MAKERERE', '0733334444')
c1.OpenAccount()
c1.DepositMoney(60000)
c1.WithdrawMoney(15000)
c1.GeneralInquiry()

d1 = Customer('2', 'DFCU', 'KAMPALA', '203', '00200004', 'ODONGO PATRICK ', 'MAKERERE', '0704444555')
d1.OpenAccount()
d1.DepositMoney(60000)
d1.WithdrawMoney(17000)
d1.GeneralInquiry()

e1 = Customer('2', 'DFCU', 'KAMPALA', '204', '00200005', 'IHIRWE LILIAN', 'KIKONI', '0706666777')
e1.OpenAccount()
e1.DepositMoney(30000)
e1.WithdrawMoney(5000)
e1.GeneralInquiry()
e1.ApplyForLoan(50000)

f1 = Customer('2', 'DFCU', 'KAMPALA', '205', '00200006', 'AMAU ', 'KIKUMU KIKUMI', '0737777880')
f1.OpenAccount()
f1.DepositMoney(40000)
f1.WithdrawMoney(5500)
f1.GeneralInquiry()

g1 = Customer('1', 'DFCU', 'KAMPALA', '206', '00200007', 'SILVAN ', 'BWAISE', '0778888999')
g1.OpenAccount()
g1.DepositMoney(60000)
g1.WithdrawMoney(10000)
g1.GeneralInquiry()


h1 = Customer('2', 'DFCU', 'KAMPALA', '207', '00200008', 'CLEVER', 'KIKONI', '0789999111')
h1.OpenAccount()
h1.DepositMoney(60000)
h1.WithdrawMoney(12000)
h1.GeneralInquiry()

i1 = Customer('2', 'DFCU', 'KAMPALA', '208', '00200009', 'PETER', 'WANDEGEYA', '077555606')
i1.OpenAccount()
i1.DepositMoney(60000)
i1.WithdrawMoney(10000)
i1.GeneralInquiry()

j1 = Customer('2', 'DFCU', 'KAMPALA', '209', '00200010', 'ASIIMWE CHRISPUS', 'KIKONI','0706278557')
j1.OpenAccount()
j1.DepositMoney(60000)
j1.WithdrawMoney(13000)
j1.GeneralInquiry()

a = Customer('1', 'DFCU', 'GULU', '123', '00100001', 'emma', 'kamp', '0703750666')
a.OpenAccount()
a.DepositMoney(30000)
a.WithdrawMoney(10000)
a.GeneralInquiry()

b = Customer('1', 'DFCU', 'GULU', '124', '001000022', 'NASASIRA THEONEST', 'NIMURA', '0706663750')
b.OpenAccount()
b.DepositMoney(40000)
b.WithdrawMoney(20000)
b.GeneralInquiry()

c = Customer('1', 'DFCU', 'GULU', '125', '00100003', 'RUNDANA SYLUS', 'PUMAKA', '0705037666')
c.OpenAccount()
c.DepositMoney(60000)
c.WithdrawMoney(15000)
c.GeneralInquiry()

d = Customer('1', 'DFCU', 'GULU', '126', '00100004', 'ASIIMIRE ISAACAKIZZA', 'NIKIDO', '0706375066')
d.OpenAccount()
d.DepositMoney(60000)
d.WithdrawMoney(17000)
d.GeneralInquiry()

e = Customer('1', 'DFCU', 'GULU', '127', '00100005', 'KWESIGA ASAPH', 'PUDAMA', '0700663756')
e.OpenAccount()
e.DepositMoney(30000)
e.WithdrawMoney(5000)
e.GeneralInquiry()

f = Customer('1', 'DFCU', 'GULU', '128', '00100006', 'WALUGEMBE JOHN', 'DUKANA', '0700636756')
f.OpenAccount()
f.DepositMoney(40000)
f.WithdrawMoney(5500)
f.GeneralInquiry()

g = Customer('1', 'DFCU', 'GULU', '129', '00100007', 'ATUHAIRWE LORNA', 'PUDAMA', '0703751555')
g.OpenAccount()
g.DepositMoney(60000)
g.WithdrawMoney(10000)
g.GeneralInquiry()

h = Customer('1', 'DFCU', 'GULU', '130', '00100008', 'NALUWOZA SHARIFAH', 'DUKANA', '0701555375')
h.OpenAccount()
h.DepositMoney(60000)
h.WithdrawMoney(12000)
h.GeneralInquiry()

i = Customer('1', 'DFCU', 'kampala', '131', '00100009', 'TUMUHAIRWE RONAH', 'KUMINA', '0703155575')
i.OpenAccount()
i.DepositMoney(60000)
i.WithdrawMoney(10000)
i.GeneralInquiry()

j = Customer('1', 'DFCU', 'kampala', '132', '00100010', 'NYEHANGANE DARIUS', 'BUKADI', '0701555655')
j.OpenAccount()
j.DepositMoney(60000)
j.WithdrawMoney(13000)
j.GeneralInquiry()
#this is the driver code for the teller
bank1= Bank('1','DFCU','kampala')
bank1.t1= Teller('NABASA SARAH', '011','2','DFCU','KAMPALA','200','00200001','KALUMBA JONATHAN','Entebbe', '0703750666')
#t1.CollectMoney(5000)

