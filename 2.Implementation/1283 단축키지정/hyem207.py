"""
주어진 그대로 구현하면 됨
처음에 생각 못한 반례:
'''
2
A
AB B
'''
"""
import sys
input = sys.stdin.readline
n = int(input())
short_keys = []

for i in range(n):
    short_key = False
    s = input().rstrip('\n')
    words = s.split()
    # 1. 단어의 첫글자 
    for j, word in enumerate(words):
        if word[0].lower() not in short_keys:
            short_key = word[0]
            short_keys.append(word[0].lower())
            # answer 출력
            answer = ''
            for k in range(len(words)):
                if k != j :
                    answer += words[k] + ' '
                else:
                    answer += '[' + words[k][0] + ']' + words[k][1:] +' ' 
            print(answer.rstrip())
            break
    # 2. 안 쓰인 글자
    if short_key == False:
        for c in s:
            if c == ' ':
                continue
            if c.lower() not in short_keys:
                short_keys.append(c.lower())
                short_key = c
                # answer 출력
                s =list(s)
                idx = s.index(short_key)
                s.insert(idx+1,']')
                s.insert(idx,'[')
                print(''.join(s))
                break
    
    # 3. 단축키 없는 경우
    if short_key == False:
        print(s)
