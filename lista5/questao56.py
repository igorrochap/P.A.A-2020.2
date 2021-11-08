def minimum_cost(string_length, cuts):
    costs = []
    for i in range(len(cuts)):
        costs += [[0] * (len(cuts))]

    for i in range(2, len(cuts)):
        for j in range(0, (len(cuts)) - i):
            j + i
            costs[j][j + i] = 1e1
            for k in range(j + 1, j + i):
                costs[j][j + i] = min(costs[j][j + i], costs[
                                        j][k] + costs[k][j + i])

            costs[j][j + i] += cuts[j + i] - cuts[j]

    return costs[0][(len(cuts)) - 1]

string_length = 20
cuts = [3, 10]
cuts = [-1] + cuts + [string_length - 1]
print('The optimal cost of the cut is:', int(minimum_cost(string_length, cuts)))