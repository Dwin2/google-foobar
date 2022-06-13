def bfs(g, w, l):
    nxtpos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = {(0, 0) : 1}
    q = [(0, 0)]
    while (len(q)):
        x, y = q.pop(0)
        steps = d[(x, y)]
        if (x == l-1 and y == w-1): return steps
       
        for n in nxtpos:
            nx, ny = n[0], n[1]
            if 0 <= nx+x <= l-1 and 0 <= ny + y <= w-1:
                nxtPos = (nx+x, ny+y)
                if nxtPos not in d and g[nx+x][ny+y] != 1:
                    q.append(nxtPos)
                    d[nxtPos] = steps+1
   
    return 9999999999999
 
def solution(grid):
    ans = 9999999999
    l = len(grid)
    w = len(grid[0])
    ans = min(ans, bfs(grid, w, l))
    for i in range(l):
        for j in range(w):
            if grid[i][j] == 1:
                grid[i][j] = 0
                ans = min(ans, bfs(grid, w, l))
                grid[i][j] = 1
   
    return ans
