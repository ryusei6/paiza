import itertools


def main():
    n, k = map(int, input().split())
    if n >= 10:
        print(0)
        return
    A = list(range(2*n))

    comb_list = list(itertools.combinations(A, n))
    ans = 0
    for comb in comb_list:
        s = 0
        comb2 = list(set(A) - set(comb))
        for i in range(n):
            s += abs(comb[i] - comb2[i])
        if s <= k:
            ans += 1
    print(ans)

    
if __name__ == '__main__':
    main()