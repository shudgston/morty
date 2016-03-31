from prettytable import PrettyTable

# Standard mortgage payment formula
# M = P [ i(1 + i)n ] / [ (1 + i)n - 1]

P = 125000.00
YEARS = 30
INTEREST_RATE = 0.04875
I = INTEREST_RATE / 12.0
n = YEARS * 12
nn = (1 + I) ** n
M = round(P * ( (I * nn) / (nn - 1) ), 2)

BALANCE = P
MONTHLY_INTEREST = I
PAYMENT = M
EXTRA_PAYMENT = 0

tbl = PrettyTable(['Payment #', 'Payment', 'Interest', 'Principal', 'Balance'])
tbl.border = False
tbl.header_style = 'upper'
tbl.align = 'r'

i = 0
total_interest = 0.0

while (BALANCE >= PAYMENT):
    i += 1
    interest_payment = BALANCE * MONTHLY_INTEREST
    total_interest += interest_payment
    principal_payment = PAYMENT - interest_payment
    BALANCE -= principal_payment + EXTRA_PAYMENT
    row = [
        i,
        PAYMENT,
        '%.2f' % round(interest_payment, 2),
        '%.2f' % round(principal_payment, 2),
        '%.2f' % round(BALANCE, 2)
    ]
    tbl.add_row(row)

print tbl
print "Total interest paid: $%.2f" % total_interest
