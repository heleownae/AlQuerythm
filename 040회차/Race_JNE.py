def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)}
    
    for calling in callings:
        current_rank = rank[calling]
        
        if current_rank > 0:
            front_player = players[current_rank - 1]
            
            players[current_rank], players[current_rank - 1] = players[current_rank - 1], players[current_rank]
            
            rank[calling] -= 1
            rank[front_player] += 1
            
    return players
