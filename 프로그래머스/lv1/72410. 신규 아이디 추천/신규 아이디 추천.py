def solution(new_id):
    answer = ''
    cnt = True
    f = ''
    new_id = new_id.lower()
    for s in new_id:
        if s in '-_.' or s.isdigit() or s.isalpha():
            f += s
    for s in f:
        if cnt:
            if s =='.':
                answer += s
                cnt = False
            else:
                answer +=s
        else:
            if s !='.':
                answer += s
                cnt = True
    if answer and answer[0] =='.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    if not answer:
        answer += 'a'
    if len(answer)>=16:
        answer = answer[:15]
    if answer and answer[-1] =='.':
        answer = answer[:-1]
    while len(answer)<=2:
        answer += answer[-1]
    return answer