import locale
from collections import namedtuple

locale.setlocale(locale.LC_ALL, 'en_US')

MonthlyPayment = namedtuple('MonthlyPayment',
    'payment_number, payment, principal, interest, total_interest, balance')


def make_row(row_num, *data):
    """Return a MonthlyPayment with numbers rounded up to two decimal places."""
    return MonthlyPayment(row_num, *tuple(round(x, 2) for x in data))


class MortgageCalculator:

    def __init__(self, principal, term, interest_rate, extra=0):
        """
        :param principal: (P) The amount borrowed ($200,000)
        :param term: (N) Number of payments in years (15, 20, 30, ect)
        :param interest_rate: (r) Fixed interest rate percentage (4.5%, 6.875%)
        :param extra: Fixed amout of extra principal to pay each month.
        """
        self.principal = principal
        self.term = term * 12
        self.interest_rate = interest_rate / 100 / 12
        self.balance = principal
        self.extra_principal = extra
        self.total_interest = 0
        self.payment_count = 0
        self.principal_paid = 0

    def get_payments(self):
        """A generator that returns one month's payment at a time, until the
        debt is paid.
        """
        while True:
            payment = self.get_payment()
            interest_payment = self.balance * self.interest_rate
            principal_payment = payment - interest_payment

            self.balance = self.balance - self.extra_principal - principal_payment
            self.total_interest += interest_payment
            self.payment_count += 1

            yield make_row(
                self.payment_count,
                payment,
                principal_payment,
                interest_payment,
                self.total_interest,
                self.balance)

            if principal_payment >= self.balance:
                # Paid off!
                return


    def get_payment(self):
        """Calculate the month payment based on the standard US mortgage
        formula.
        """
        dividend = self.interest_rate * self.principal
        divisor = 1 - (1 + self.interest_rate) ** (-self.term)
        return dividend / divisor
