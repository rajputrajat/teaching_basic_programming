# Exercise 12: Calculate income tax for the given income
# by adhering to the below rules
# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
# Expected Output:

# For example, suppose that the taxable income is $45000
# the income tax payable is

# $10000*0% + $10000*10%  + $25000*20% = $6000.

def calculate_income_tax() -> float:
    pass

assert(6000 == calculate_income_tax(45000))

print('passed')