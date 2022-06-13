import sys
def minStepstoEnd(start_pos, end_pos):
    ind = {}
    cnt = 0
    for i in range(8):
        for j in range(8):
            ind[cnt] = [i, j]
            cnt += 1
    start_pos = ind[start_pos]
    end_pos = ind[end_pos]
    queue = [start_pos]
    minSteps = [[-1 for i in range(8)] for j in range(8)]
 
    nextp = [
        (1, 2),
        (2, 1),
        (2, -1),
        (1, -2),
        (-1, -2),
        (-2, -1),
        (-2, 1),
        (-1, 2),
    ]
    minSteps[start_pos[0]][start_pos[1]] = 0
 
    while queue != []:
        current_pos = queue.pop(0)
        steps = minSteps[current_pos[0]][current_pos[1]]
 
        if current_pos == end_pos:
            return steps;
 
        for nextpos in nextp:
            if 0 <= current_pos[0] + nextpos[0] <=7 and 0 <= current_pos[1] + nextpos[1] <= 7:
                nextPosition = [current_pos[0] + nextpos[0], current_pos[1] + nextpos[1]]
                if minSteps[nextPosition[0]][nextPosition[1]] == -1:
                    minSteps[nextPosition[0]][nextPosition[1]] = steps + 1
                    queue.append(nextPosition)
                    
    return -1
