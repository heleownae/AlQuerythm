fee = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
           "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

dict={}
for i in records:
    tmp = list(map(str, i.split()))
    if tmp[1] not in dict:
        dict[tmp[1]] = [tmp[0], tmp[2]]
    # else:
    #     dict[tmp[1]] = [tmp[0], tmp[2]] 아직 덜 풀었음.
