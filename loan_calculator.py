import math
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--type', choices=['annuity', 'diff'], help='Indicates the type of payment.')
parser.add_argument('--principal', type=int, help='The loan principal int value.(--principal=1000000)')
parser.add_argument('--periods', type=int,
                    help='This is the number of months in which repayments will be made, int value.(--periods=10)')
parser.add_argument('--interest', type=float, help='Interest rate, float value.(--interest=12.5)')
parser.add_argument('--payment', type=int, help='Monthly payment, int value.(--payment=23000)')
args = parser.parse_args()

if args.type == 'annuity':
    if args.principal and args.payment and args.interest:
        nominal_interest = args.interest / (12 * 100)
        x = (args.payment / (args.payment - nominal_interest * args.principal))
        base = 1 + nominal_interest
        years = round(math.log(x, base)) // 12
        months = math.ceil(math.log(x, base)) % 12
        if months == 0:
            print(f"It will take {years} years to repay this loan!")
        elif years == 0:
            print(f"It will take {months} months to repay this loan!")
        else:
            print(f"It will take {years} years and {months} months to repay this loan!")
        overpayment = ((years * 12 + months) * args.payment) - args.principal
        print(f"Overpayment = {round(overpayment)}")
    elif args.principal and args.periods and args.interest:
        nominal_interest = args.interest / (12 * 100)
        formula_part = pow(1 + nominal_interest, args.periods)
        payment = args.principal * ((nominal_interest * formula_part) / (formula_part - 1))
        print(f"Your annuity payment = {math.ceil(payment)}!")
        overpayment = args.principal - (math.ceil(payment) * args.periods)
        print(f"Overpayment = {round(overpayment)}")
    elif args.payment and args.periods and args.interest:
        nominal_interest = args.interest / (12 * 100)
        formula_part = pow(1 + nominal_interest, args.periods)
        principal_loan = args.payment / ((nominal_interest * formula_part) / (formula_part - 1))
        print(f"Your loan principal = {math.floor(principal_loan)}!")
        overpayment = (args.payment * args.periods) - math.floor(principal_loan)
        print(f"Overpayment = {round(overpayment)}")
    else:
        print("Incorrect parameters")
elif args.type == 'diff':
    if args.principal and args.periods and args.interest:
        nominal_interest = args.interest / (12 * 100)
        m = 1
        sum_ = 0
        while m <= args.periods:
            formula_part = args.principal / args.periods
            formula_part_2 = args.principal - ((args.principal * (m - 1)) / args.periods)
            diff_payment = formula_part + nominal_interest * formula_part_2
            print(f"Month {m}: payment is {math.ceil(diff_payment)}")
            m += 1
            sum_ += math.ceil(diff_payment)
        overpayment = sum_ - args.principal
        print(" ", f"Overpayment = {overpayment}", sep='\n')
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
