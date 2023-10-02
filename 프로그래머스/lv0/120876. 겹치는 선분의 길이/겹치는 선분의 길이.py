def solution(lines):
    line_list = []
    for i in lines:
        line_list += i
    mn = min(line_list)
    mx = max(line_list)
    
    answer = 0
    x, y, z = lines
    for j in range(mn, mx+1):
        point_answer = 0
        
        if x[0] <= j < x[1]:
            point_answer += 1
        if y[0] <= j < y[1]:
            point_answer += 1
        if z[0] <= j < z[1]:
            point_answer += 1
        
        if point_answer >= 2:
            answer += 1
    
    return answer