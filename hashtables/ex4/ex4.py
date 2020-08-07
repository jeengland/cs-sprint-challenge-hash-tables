def has_negatives(a):
    totals = {}
    result = []
    for integer in a:
        if abs(integer) not in totals.keys():
            totals[abs(integer)] = 1
        else:
            result.append(abs(integer))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
