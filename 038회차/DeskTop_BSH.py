def solution(wallpaper):
    dict=[]
    cont=[]
    first=0
    last=0
    flag=0

    for i,e in enumerate(wallpaper):
        dict.append([i,e.find("#"),e.rfind("#")])
        cont.append(e.find("#"))
        cont.append(e.rfind("#"))

    for i in dict:
        if i[1]>=0:
            if first==0 and flag==0:
                first=i[0]
                flag+=1
            if last<i[0]:
                last=i[0]

    cont = [i for i in cont if i>=0]

    return [first,min(cont),last+1,max(cont)+1]
