def solution(players, callings):
    dict={}

    for i,e in enumerate(players):
        dict[i+1]=e

    for run in callings:
        for hit in dict.items():
            if hit[1]==run:
                word=dict.get(hit[0]-1)
                dict[hit[0]-1]=run
                dict[hit[0]]=word

    return list(dict.values())
