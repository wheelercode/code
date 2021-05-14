from collections import defaultdict  

def digit_freq(a, b):
    """ Count digit frequencies in a range of numbers. """ 
    D = defaultdict(int)           # store digit counts  (D[2] counts 2's, etc..)
    for n in range(a, b+1):        # for every number n, where a <= n <= b
        for char in str(n):        # count each digit in the number (convert it to string and loop through each character in the string)
            D[char] += 1           # everytime we see a digit, increase the dictionary counter by one (keyed by digit)
    return D                       # return the completed dictionary 

D = digit_freq(1, 500000)          # count digits for whatver range
for d in sorted(D.items()):        # sort the results
    print(f'{d[0]}: {d[1]:,}')     # print the results
