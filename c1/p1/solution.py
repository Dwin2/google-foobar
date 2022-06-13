import math, sys
def solution(n):
    maxn = 50000
    primes = [True]*maxn
    for i in range(2, int(math.sqrt(maxn))+1):
        for j in range(i*i, maxn, i):
            primes[j] = False
 
    s = ""
    for i in range(2, maxn):
        if primes[i]:
            s = s + str(i)
    for i in range(n, n+5):
        sys.stdout.write(s[i])
    sys.stdout.write("\n")
