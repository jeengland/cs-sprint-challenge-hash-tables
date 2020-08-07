def intersection(arrays):
    goal = len(arrays)
    digits = {}
    result = []
    for array in arrays:
        for digit in array:
            if digit not in digits:
                digits[digit] = 1
            else:
                digits[digit] += 1
                if digits[digit] == goal:
                    result.append(digit)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
