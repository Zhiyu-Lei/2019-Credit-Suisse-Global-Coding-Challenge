def question02(risk, bonus, trader):
    """
    Calculate the maximum profit for a team of traders with a series of trades
    Only traders with skill levels at or above the difficulty of a trade can complete that trade
    :param risk: a list of the difficulties of the trades
    :param bonus: a list of the bonuses from completion of the trades
    :param trader: a list of the skill levels of the traders
    :return: the maximum profit that can be made from the trading strategy
    """
    max_profit = 0  # initialize the total maximum profit
    for td in trader:
        profit = 0  # initialize the potential profit a single trader can make
        for r, b in zip(risk, bonus):
            if td >= r:  # the trader can complete the trade
                if b > profit:
                    profit = b  # update the potential profit with a higher value
        max_profit += profit  # update the total maximum profit
    return max_profit
