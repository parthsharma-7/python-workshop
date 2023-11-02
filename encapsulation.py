class Bankaccount:
 def __init__(self,acc_no,balance):
  self._acc_no=acc_no
  self.__balance=balance

 def get_balance(self):
  return self.__balance
acc1=Bankaccount("2342323",100)
print(acc1._acc_no)
print(acc1.get_balance())