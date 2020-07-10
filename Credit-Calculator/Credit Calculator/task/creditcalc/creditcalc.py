import math
import argparse
import sys


# todo: #2) A capacity to calculate the same values as in the previous stage for annuity payment (principal, count of
#  periods and value of the payment). A user specifies all known parameters with command-line arguments, while a
#  single parameter will be unknown. This is the value the user wants to calculate.


class Calculator:
    def __init__(self):
        self.option = 0
        self.credit = 0
        self.period = 0
        self.interest = 0
        self.m_pay = 0

    def diff_payment(self):
        i = self.interest / 1200
        n = int(self.period)
        p = self.credit
        counter = 0
        print(f'principal: {p}, periods: {n}, interest: {i}')
        for m in range(1, n + 1):
            diff = (p / n) + (i * (p - ((p * (m - 1)) / n)))
            print(f'Month {m}: paid out {math.ceil(diff)}')
            counter += math.ceil(diff)
        overpayment = counter - p
        print(f'\nOverpayment = {math.ceil(overpayment)}')

    def count_of_periods(self):
        p = self.credit
        a = self.m_pay
        i = self.interest / 1200
        n = math.ceil(math.log(a / (a - i * p), 1 + i))
        overpayment = math.ceil(a) * n - p
        x = n // 12
        y = n % 12
        if y == 0:
            if x == 1:
                print(f'You need 1 year to repay this credit!')
            else:
                print(f'You need {x} years to repay this credit!')
        elif x == 0:
            if y == 1:
                print(f'You need 1 month to repay this credit!')
            else:
                print(f'You need {y} months to repay this credit!')
        else:
            print(f'You need {x} years and {y} months to repay this credit!')
        print(f'Overpayment = {math.ceil(overpayment)}')

    def value_of_payment(self):
        p = self.credit
        n = self.period
        i = self.interest / 1200
        a = p * ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1))
        overpayment = math.ceil(a) * n - p
        print(f'Your annuity payment = {math.ceil(a)}!')
        print(f'Overpayment = {math.ceil(overpayment)}')

    def principal(self):
        n = self.period
        a = self.m_pay
        i = self.interest / (12 * 100)
        p = a / ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1))
        overpayment = math.ceil(a) * n - p
        print(f'Your credit principal = {round(p)}!')
        print(f'Overpayment = {math.ceil(overpayment)}')

    @staticmethod
    def check_positive(value):
        i_value = float(value)
        if (i_value * -1) > 0:
            print('Incorrect parameters')
        return i_value

    def options(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--type', type=str, choices=['annuity', 'diff'])
        parser.add_argument('--payment', type=self.check_positive)
        parser.add_argument('--principal', type=self.check_positive)
        parser.add_argument('--periods', type=self.check_positive)
        parser.add_argument('--interest', type=self.check_positive)
        args = parser.parse_args()
        param_count = len(sys.argv) - 1
        self.credit = args.principal
        self.period = args.periods
        self.interest = args.interest
        self.m_pay = args.payment
        if param_count < 4:
            print('Incorrect parameters')
        elif args.type == 'annuity':
            if args.interest is not None:
                if args.principal is None:
                    self.principal()
                elif args.periods is None:
                    self.count_of_periods()
                elif args.payment is None:
                    self.value_of_payment()
                else:
                    print('Incorrect parameters my friend!')
            else:
                print('Incorrect parameters')
        elif args.type == 'diff':
            if args.payment is None and (args.principal, args.periods, args.interest) is not None:
                self.diff_payment()
            else:
                print('Incorrect parameters')
        else:
            print('Incorrect parameters')


if __name__ == '__main__':
    Calculator().options()
