def solution(l):
   n = len(l)
   ans = 0
   for i in range(n):
       cnt = cnt1 = 0
       for j in range(i+1, n):
           if (l[j] % l[i] == 0):cnt += 1
       for k in range(i):
           if (l[i] % l[k] == 0): cnt1 += 1
       ans += cnt*cnt1
   return ans
