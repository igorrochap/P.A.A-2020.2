def subset_sum(set, n, sum):
    subset = [[False for i in range(sum + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        subset[i][0] = True
    for i in range(1, sum + 1):
        subset[0][i] = False
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j >= set[i - 1]:
                subset[i][j] = (subset[i - 1][j - set[i - 1]] or subset[i - 1][j])
            if j < set[i - 1]:
                subset[i][j] = subset[i - 1][j]
    return subset[n][sum]

set = [3, 2, 6, 3, 10, 15]
sum = 25
if (subset_sum(set, len(set), sum) == True):
    print('There is a subset with the sum')
else:
    print("There isn't a subset with the sum")