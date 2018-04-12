def getBestMorning(dic):
    best = (-1,-1)
    for i in range(0,13,2):
        if(i not in dic):
            continue
        cur = (dic[i],i)
        if(cur>best):
            best = cur
    return best

def getBestEvening(dic):
    best = (-1,-1)
    for i in range(12,23,2):
        if(i not in dic):
            continue
        cur = (dic[i],i)
        if(cur>best):
            best = cur
    return best
