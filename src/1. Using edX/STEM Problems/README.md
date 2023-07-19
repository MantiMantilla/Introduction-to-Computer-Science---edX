We are searching for the smallest monthly payment such that we can pay off the entire balance of a loan within a year.

The following values might be useful when writing your solution

Monthly interest rate
    = (Annual interest rate) / 12
Monthly payment lower bound
    = Balance / 12
Monthly payment upper bound
    = (Balance x (1 + Monthly interest rate)12) / 12

The following variables contain values as described below:

balance
    - the outstanding balance on the credit card
annualInterestRate
    - annual interest rate as a decimal

Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent such that we can pay off the debt within a year.

Note that if you do not use bisection search, your code will not run - your code only has 30 seconds to run on our servers. If you get a message that states "Your submission could not be graded. Please recheck your submission and try again. If the problem persists, please notify the course staff.", check to be sure your code doesn't take too long to run.

The code you paste into the following box should not specify the values for the variables `balance` or `annualInterestRate` - our test code will define those values before testing your submission.
