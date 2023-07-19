def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


annualInterestRate = 0.18
balance = 999999


monthlyRate = annualInterestRate / 12


def f(payment):
    global balance
    tracked_balance = balance
    for _ in range(1, 13):
        tracked_balance -= payment
        tracked_balance *= 1 + monthlyRate
    return tracked_balance


a = balance / 12
b = (balance * ((1 + monthlyRate) ** 12)) / 12

tol = 1 / 100

n = 0
N = 100

payment = None


while n <= N:
    c = (a + b) / 2
    n += 1
    if f(c) == 0 or (b - a) / 2 < tol:
        payment = c
        break
    if sign(f(c)) == sign(f(a)):
        a = c
    else:
        b = c

print(payment)
