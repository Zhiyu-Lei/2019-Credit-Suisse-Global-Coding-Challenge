def question05(input):
    """
    Calculate the minimum number of instances needed, to protect the safety of the organisation from security threats
    :param input: a list of integers with the first one representing the number of security threats posed,
                  followed by pairs of the time and frequency of the threats
    :return: the minimum number of instances
    """
    n_threat = input[0]  # number of threats
    threats = [(input[i * 2 + 1], input[i * 2 + 2]) for i in range(n_threat)]  # list of threats in (t, f) format
    threats.sort(key=lambda thr: thr[0])  # sort the list of threats by t
    instances = [{'t': threats[0][0], 'f': threats[0][1]}]  # initial list of instances in {'t': t, 'f': f} format
    for threat in threats:
        counter = False
        instances.sort(key=lambda inst: inst['t'], reverse=True)  # sort the list of instances by t in reverse order
        for instance in instances:
            if abs(instance['f'] - threat[1]) <= threat[0] - instance['t']:  # can counter
                counter = True
                instance['t'] = threat[0]  # update the instance's current t
                instance['f'] = threat[1]  # update the instance's current f
                break
        if not counter:  # cannot counter
            instances.append({'t': threat[0], 'f': threat[1]})  # add a new instance
    return len(instances)
