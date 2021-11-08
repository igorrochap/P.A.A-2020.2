def smallest_sum(triangle):
    minimum = []
    n = len(triangle) - 1

    for i in range (len(triangle[n])):
        minimum.append(triangle[n][i])

    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            minimum[j] = triangle[i][j] + min(minimum[j], minimum[j + 1])

    return minimum[0]


triangle = [[2],
            [5, 4],
            [3, 4, 7],
            [1, 6, 9, 6]        
]

print(smallest_sum(triangle))