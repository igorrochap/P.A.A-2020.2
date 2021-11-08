import sys

def having_change_possibility(coins, v):
    t = [0] * (v + 1)
    
    for i in range(1, v + 1):
        t[i] = sys.maxsize
        for current in range(len(coins)):
            change = t[i - coins[current]]
            if change != sys.maxsize:
                t[i] = min(change + 1, t[i])

    return t[v]

coins = [5, 10]
k = 6
v = 55
if(having_change_possibility(coins, v) <= k):
    print("It's possible to give change")
else:
    print("It's not possible to give change")
    