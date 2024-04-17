card = list(input())
    
while card:
    del card[0]
    card.append(card[0])
    del card[0]
    if len(card) == 1:
        break
    
print(*card)
