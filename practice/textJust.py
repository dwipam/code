words = ["This", "is", "an", "example", "of", "text","lubricate","is"]
L = 16
temp = []
i=0
while i<(len(words)):
    j=i+1
    while(len(' '.join(words[i:j+1]))<=L and j<len(words)):
        j+=1
    sol = []
    import pdb;pdb.set_trace()
    #spacRequired = (L-len(''.join(words[i:j])))/len(words[i:j])
    spacRequired = (L-len(''.join(words[i:j])))/(len(words[i:j])-1 if len(words[i:j])>1 else len(words[i:j]))
    z = len(words[i:j])
    x = [spacRequired for x in range(z-1 if z>1 else z)]
    x[0] =x[0]+ (L-len(''.join(words[i:j])))-sum(x)
    x.append(0)
    for k in range(len(words[i:j])):
        sol.append(words[i:j][k]);sol.append(' '*x[k])
    temp.append(''.join(sol))
    i=j
print temp
print map(lambda x: len(x),temp)

