# balance = 42
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

monthlyRate = annualInterestRate / 12


def f(monthlyPaymentRate):
    global balance
    tracked_balance = balance
    payment = tracked_balance * monthlyPaymentRate
    for _ in range(1, 13):
        tracked_balance -= payment
        tracked_balance *= 1 + monthlyRate
        payment = tracked_balance * monthlyPaymentRate
    return tracked_balance


result = f(monthlyPaymentRate)

print("Remaining balance:", "{:.2f}".format(result))
