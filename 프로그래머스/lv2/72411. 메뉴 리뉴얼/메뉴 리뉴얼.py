from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        hash = {}  
        for s in orders:
            if len(s)>=i:
                for ord in combinations(s,i):
                    d = ''
                    ord =sorted(ord)
                    for ss in ord:
                        d += ss
                    
                    try :hash[d] +=1
                    except :
                        hash[d] = 1
        m = [(0,None)]
        for k,v in hash.items():
            if v <2:
                continue
            if v== m[0][0]:
                m.append((v,k))
            elif v> m[0][0]:
                m = [(v,k)]
        for li in m:
            if li[1]:
                answer.append(li[1])
    return sorted(answer)