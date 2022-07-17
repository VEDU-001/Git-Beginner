
class Customer:
    def __init__(self, customer_name, bill_amount):
        self.customer_name = customer_name
        self.bill_amount = bill_amount
        self.amount = self.bill_amount - (self.bill_amount / 20)
    
    def pays_bill(self,amount):
        print(self.customer_name," pays bill amount of Rs.",amount)

obj1 = Customer(input("Enter Customer name = "),int(input("Enter bill amount = ")))
amount = obj1.amount
obj1.pays_bill(amount)