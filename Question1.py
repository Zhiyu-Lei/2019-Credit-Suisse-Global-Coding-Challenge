def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    """
    Calculate the total estimated cost of a "Simply Buy" mortgage with a fixed 10% deposit
    :param initialLevelOfDebt: the initial debt
    :param interestPercentage: a percentage of the current debt
    :param repaymentPercentage: a fixed percentage of the initial debt
    :return: the total cost of the mortgage
    """
    debt = initialLevelOfDebt  # initialize current debt
    repayment = initialLevelOfDebt * repaymentPercentage / 100
    n_repay = 0
    interest_rate = 1 + interestPercentage / 100
    while debt > repayment:
        debt = debt * interest_rate - repayment  # Add interest and make repayment
        n_repay += 1
    cost = initialLevelOfDebt * 10 / 100 + n_repay * repayment + debt
    return round(cost)
