def solution(info, query):
    inf_dic = {}
    for lang in ['java','python','cpp','-']:
        for part in ['backend','frontend','-']:
            for job in ['junior','senior','-']:
                for food in ['chicken','pizza','-']:
                    inf_dic[lang+part+job+food]=[]
    for inf in info:
        inf = inf.split()
        for lang in [inf[0],'-']:
            for part in [inf[1],'-']:
                for job in [inf[2],'-']:
                    for food in [inf[3],'-']:
                        inf_dic[lang+part+job+food].append(int(inf[4]))
    n = len(query)
    answer = [0 for _ in range(n)]
    for key in inf_dic.keys():
        inf_dic[key].sort()
    for i in range(n):
        qu = query[i].split()
        score = int(qu[7])
        inf_li = inf_dic[qu[0]+qu[2]+qu[4]+qu[6]]
        l = len(inf_li)
        tmp = l

        low,high = 0,l-1

        while low<=high:
            mid = (low+high)//2

            if score<=inf_li[mid]:
                tmp = mid
                high = mid-1
            else:
                low = mid+1
        answer[i] = l-tmp
    return answer