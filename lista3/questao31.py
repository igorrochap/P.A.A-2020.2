def turn_pancakes(pancakes, i):
    start = 0
    while start < i:
        aux = pancakes[start]
        pancakes[start] = pancakes[i]
        pancakes[i] = aux
        start = start + 1
        i = i - 1

def bigger_pancake(pancakes, n):
    bigger = 0
    for i in range(0, n):
        if(pancakes[i] > pancakes[bigger]):
            bigger = i
    return bigger


def arrange_pancakes(pancakes, n):
    while(n > 1):
        bigger = bigger_pancake(pancakes, n)
        if bigger != (n - 1):
            turn_pancakes(pancakes, bigger)
            turn_pancakes(pancakes, n - 1)
        n = n - 1

pancakes_sizes = [15, 2, 18, 53, 21, 8, 10, 32]
arrange_pancakes(pancakes_sizes, len(pancakes_sizes))
print(pancakes_sizes)
