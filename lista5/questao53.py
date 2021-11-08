def add_edge(adjacencies, u, v):
    adjacencies[u].append(v)

def dfs(node, adjacencies, dp, visited_nodes):
    visited_nodes[node] = True
    
    for i in range(0, len(adjacencies[node])):
        if not visited_nodes[adjacencies[node][i]]:
            dfs(adjacencies[node][i], adjacencies, dp, visited_nodes)
        dp[node] = max(dp[node], dp[adjacencies[node][i]] + 1)


def longest_path(adjacencies, n):
    length = 0
    dp = [0] * (n + 1)
    visited_nodes = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited_nodes[i]:
            dfs(i, adjacencies, dp, visited_nodes)
    for i in range(1, n + 1):
        length = max(length, dp[i])

    return length
            


n = 5
adjacencies = [[] for i in range(n + 1)]

add_edge(adjacencies, 1, 2)
add_edge(adjacencies, 1, 3)
add_edge(adjacencies, 3, 2)
add_edge(adjacencies, 2, 4)
add_edge(adjacencies, 3, 4)

print('The length of the longest path is:', longest_path(adjacencies, n))