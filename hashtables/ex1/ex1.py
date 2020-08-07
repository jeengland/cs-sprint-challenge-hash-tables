def get_indices_of_item_weights(weights, length, limit):
    if length < 2:
        return None
    diffs = {}
    for i in range(len(weights)):
        if limit - weights[i] not in diffs.keys():
            diffs[limit - weights[i]] = [[i, weights[i]]]
        else:
            diffs[limit - weights[i]] += [[i, weights[i]]]
    for diff in diffs:
        if diffs[diff][0][1] in diffs.keys():
            if diff != limit - diff:
                return sorted([diffs[diff][0][0], diffs[limit - diff][0][0]], reverse=True)
            else:
                return sorted([diffs[diff][0][0], diffs[diff][1][0]], reverse=True)
    return None
