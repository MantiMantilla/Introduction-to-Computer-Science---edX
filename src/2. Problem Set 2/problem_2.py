# balance = 3329
# annualInterestRate = 0.2

monthlyRate = annualInterestRate / 12


def f(payment):
    global balance
    tracked_balance = balance
    for _ in range(1, 13):
        tracked_balance -= payment
        tracked_balance *= 1 + monthlyRate
    return tracked_balance


payment = 0

while True:
    if f(payment) <= 0:
        break
    payment += 10

print("Lowest Payment:", payment)
