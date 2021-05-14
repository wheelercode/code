from collections import defaultdict   

def digit_freq(a, b):
    D = defaultdict(int)
    for n in range(a, b+1):
        for char in str(n):
            D[char] += 1
    return D

D = digit_freq(1, 500000)
for d in sorted(D.items(), key=lambda x: x[0]):
    print(f'{d[0]}: {d[1]:,}')
