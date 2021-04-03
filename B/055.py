def price(a, b, c, d, x):
    if x - a < 0:
        return b
    return b + ((x - a) // c + 1) * d


n, x = map(int, input().split())
P = []
for i in range(n):
    a, b, c, d = map(int, input().split())
    p = price(a, b, c, d, x)
    P.append(p)
print(min(P), max(P))