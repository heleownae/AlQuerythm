i = int(input())
df = [card for card in range(1, i+1)]

if len(df) == 1:
    print(*df)
else:
    while len(df) != 1:
        del df[0]
        df.append(df[0]) 
        del df[0]
        if len(df) == 1:
            print(*df)
