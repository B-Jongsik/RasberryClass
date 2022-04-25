from itertools import permutations

def data(n,r):
    dataset = []
    for i in range(n):
        dataset.append(i)
    res = list(permutations(dataset, r))
    print("n's value : ",n)
    print("r's value : ", r)
    print(f"Result of Permutation : {len(res)}") 
    return res

n,r = map(int, input().split())
data(n,r)