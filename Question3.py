from collections import Counter


def question03(scores, alice):
    """
    The participant with the highest score is ranked number 1 on the leader board
    Participants who have equal scores receive the same ranking number
    The next participants(s) receive the immediately following ranking number
    :param scores: a lsit of scores of all the other participants
    :param alice: a list of alice's scores
    :return: alice's modal ranking
    """
    set_scores = set(scores)  # use set to eliminate equal scores
    ranks = []  # initialize list of ranks
    for alice_score in alice:  # test every score of alice
        new_scores = sorted(list(set_scores | {alice_score}), reverse=True)  # sort the new list of scores with alice's
        for i, score in enumerate(new_scores, start=1):
            if score == alice_score:
                ranks.append(i)  # get the rank
                break
    counter_ranks = Counter(ranks)  # count the frequencies of ranks
    sorted_ranks = sorted(counter_ranks.items(), key=lambda item: item[1], reverse=True)  # sort ranks by frequencies
    highest_frequency = sorted_ranks[0][1]
    highest_rank = 0
    for rank, count in sorted_ranks:
        if count == highest_frequency:
            if rank > highest_rank:
                highest_rank = rank
        else:
            break
    return highest_rank
