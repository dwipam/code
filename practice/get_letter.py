s = "abcd"
t = "abcde"
t = list(t)
visit = [False for i in t]
for i in range(len(t)):
    if s.find(t[i]) >= 0 and visit[i] == False:
        visit[i] = True
    print t[visit.index(False)]
