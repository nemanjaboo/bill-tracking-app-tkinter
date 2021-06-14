from db_functions import *
import datetime

dt = datetime.datetime.now()
class Bill:
    def __init__(self, month, name, cost, status):
        self.month = month
        self.name = name
        self.cost = cost
        self.status = status

    def __str__(self):
        return 'MONTH : {}, NAME {}\nCOST: {} ----- {}'.format(self.month, self.name, self.cost, self.status)

    @staticmethod
    def get_month():
        m = str(dt.strftime('%B'))
        y = str(dt.year)
        return m+'-'+y

    @staticmethod
    def add_bill(name, cost, status):
        new_bill = Bill(Bill.get_month(), name, cost, status)
        return insert_bill_to_table(new_bill)
    


class Bills:
    def __init__(self, bills_list=None):
        if bills_list is None:
            bills_list = []
        self.bills_list = bills_list



