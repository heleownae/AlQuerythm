def solution(park, routes):
    start=''
    fence=[]
    limit_a=len(park[0])
    limit_b=len(park)

    for row,parks in enumerate(park):
        for col,word in enumerate(parks):
            if word == 'S':
                start=[row,col]
            elif word == 'X':
                fence.append([row,col])

    for a in routes:
        route, num = a.split()
        if route == 'E':
            tmp=start.copy()
            for b in range(int(num)):
                start[1]+=1
                if (start in fence) or (start[1]>=limit_a) or (start[1]<0):
                    start=tmp
                    break
        elif route == 'S':
            tmp=start.copy()
            for b in range(int(num)):
                start[0]+=1
                if (start in fence) or (start[0]>=limit_b) or (start[0]<0):
                    start=tmp
                    break
        elif route == 'W':
            tmp=start.copy()
            for b in range(int(num)):
                start[1]-=1
                if (start in fence) or (start[1]>=limit_a) or (start[1]<0):
                    start=tmp
                    break

    return start
