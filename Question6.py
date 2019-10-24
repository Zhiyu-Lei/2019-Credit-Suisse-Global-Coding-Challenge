def question06(portfolio):
    """
    Find the stock with maximum value which has the starting and ending same as the first stock in the portfolio
    :param portfolio: a string representing the list of stocks in "['stock_1, 'stock_2', ..., 'stock_n']" format
    :return: the index of highest valued stock found
    """
    portfolio = portfolio[1:-1]  # get rid of square brackets
    portfolio_cleaned = [item[1:-1] for item in portfolio.split(', ')]  # clean portfolio into a list of strings
    start = portfolio_cleaned[0][0]  # start substring
    end = portfolio_cleaned[0][-1]  # end substring
    index = len(portfolio_cleaned) - 1  # traverse the portfolio backwards
    while index >= 0:
        stock = portfolio_cleaned[index]
        if stock[0] == start and stock[-1] == end:
            return index
        index -= 1
