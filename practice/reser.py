import random

def sample(x,k):
    window = x[:k]
    for i in range(len(x))[k+1:]:
        t = random.randrange(i)
        if t<k:
            window[t] = x[i]
    print window

sample([random.randrange(100) for i in range(100)],5)
            

