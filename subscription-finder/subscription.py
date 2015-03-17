import sys
import csv
import datetime
from collections import defaultdict

# "Date","Description","Original Description","Amount","Transaction Type","Category","Account Name","Labels","Notes"
DATE = 0
DESCRIPTION = 1
ORIG_DESCRIPTION = 2
AMOUNT = 3
TRANS_TYPE = 4
CATEGORY = 5

class Transaction:
    def __init__ (self, date, description, orig_description, amount):
        self.date = datetime.datetime.strptime(date, '%m/%d/%Y')
        self.description = description
        self.orig_description = orig_description
        self.amount = amount
    def __str__(self):
        return "%s - %s - %s" % (self.date, self.description, self.amount)

def find_subscriptions (filename):
    with open(filename, 'r') as f:
        # map from description to array of transactions
        transactions = defaultdict(list)
        next(f)
        r = csv.reader(f, delimiter=',', quotechar='"')
        for t in r:
            transactions[t[DESCRIPTION] + t[AMOUNT]].append(Transaction(t[DATE], t[DESCRIPTION], \
                                                                        t[ORIG_DESCRIPTION], t[AMOUNT]))
    
    for group in transactions:
        subscription = transactions[group]
        if len(subscription) > 1:
           amount = subscription[0].amount
           for payment in subscription:
               if payment.amount != amount:
                   break
           else:
               print "---"
               print group
               for payment in subscription:
                   print payment

               print "---"
def main ():
    find_subscriptions (sys.argv[1])

if __name__ == "__main__":
    main()
