def question04(v, c, mc):
    """
    Calculate the maximum value of trades can be executed, given the complexity constraint
    :param v: a list of trade values
    :param c: a list of complexities
    :param mc: the maximum complexity
    :return: the maximum value
    """
    return calculate_max_value(v, c, mc, 0, 0, 0, 0)


def calculate_max_value(v, c, mc, index_trade, current_value, current_complexity, max_value):
    """
    Recursively calculate the maximum value by considering a new trade each time
    :param v: a list of trade values
    :param c: a list of complexities
    :param mc: the maximum complexity
    :param index_trade: the index of the current trade considered
    :param current_value: the total value before considering current trade
    :param current_complexity: the total complexity before considering current trade
    :param max_value: the current maximum value
    :return: the maximum value
    """
    if index_trade == len(v):
        return max_value
    if current_complexity + sum(c[index_trade:]) <= mc:  # all trades after can be chosen
        total_values_after = sum(v[index_trade:])
        if current_value + total_values_after > max_value:
            max_value = current_value + total_values_after
        return max_value
    # consider choosing current trade
    if current_complexity + c[index_trade] <= mc:  # current trade can be chosen
        if current_value + v[index_trade] > max_value:
            max_value = current_value + v[index_trade]  # update max_value
        max_value = calculate_max_value(v, c, mc, index_trade + 1, current_value + v[index_trade],
                                        current_complexity + c[index_trade], max_value)  # next trade
    # consider not choosing current trade
    max_value = calculate_max_value(v, c, mc, index_trade + 1, current_value, current_complexity, max_value)  # next td
    return max_value
