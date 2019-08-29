from collections import defaultdict
from random import random
x = [-1, 4, 9, 7, 7, 2, 7, 3, 0, 9, 6, 5, 7, 8, 9]
dic = defaultdict(int)
for i in x:
    dic[i]+=1
max_key = max(dic.iterkeys(),key = lambda x : dic[x])
cnt = 0
t = round(random() % dic[max_key] + 1)
j = 0
for i in x:
    if i == max_key:
        cnt+=1
    if cnt == t:
        print j
        break
    j+=1


