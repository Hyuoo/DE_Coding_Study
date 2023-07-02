from collections import defaultdict 
import sys
sys.stdin = open("input.txt", "r")

n = int(input())
options = [input() for _ in range(n)] 
result = []
keys = defaultdict(int)

for option in options:
    words = option.split()  
    for i, word in enumerate(words):   # 1번
        if keys[word[0].upper()] == 0:
            keys[word[0].upper()] += 1
            words[i] = '['+word[0]+']'+word[1:]
            result.append(' '.join(words))
            break
    else:       # 2번
        flag = False
        for i, word in enumerate(words):
            for j, alph in enumerate(word):   
                if keys[alph.upper()] == 0:
                    keys[alph.upper()] += 1
                    l = list(word) 
                    l[j] = '['+alph+']' 
                    word = ''.join(l)
                    words[i] = word
                    result.append(' '.join(words))
                    flag = True
                    break
            if flag:
                break
        else:
            result.append(option) # 3번

for r in result:
    print(r)
