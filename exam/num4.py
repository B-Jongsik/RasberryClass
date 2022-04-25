from itertools import permutations

def data(n,r):
    dataset = []
    for i in range(n):
        dataset.append(i)
    res = list(permutations(dataset, r))
    # print(f"모든 경우: {res}") # [('A'
    print(f"모든 경우의 수: {len(res)}") 
    return res

n,r = map(int, input().split())
data(n,r)