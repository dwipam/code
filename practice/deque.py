def _():
    x = [5,7,9,6,3,1,2,4,8,10]
    import pdb;pdb.set_trace()
    t = [0]*len(x)
    for i in range(len(t)):
        t[x[i]-1] = i
    deq = [1]
    vec = ["pushBack"]
    counter = 2
    for i in range(len(x)):
        val = x[i]
        while True:
            if len(deq)!=0:
                if val == deq[len(deq)-1]:
                    deq.pop()
                    vec.append("popBack")
                    break
                elif counter > len(x):
                    print "impossible"
                    return
            if counter < val:
                if(t[counter-2] < t[counter-1] and len(deq)!=0):
                    deq.insert(0,counter)
                    vec.append("pushFront")
                else:
                    deq.append(counter)
                    vec.append("pushBack")
                counter+=1
            else:
                x.append(counter)
                x.pop()
                counter+=1
                vec.append("pushBack")
                vec.append("popBack")
                break
    print ','.join(vec)
    y = []
    counter = 1
    for i in vec:
        if i == 'pushBack':
            y.append(counter)
            counter+=1
        if i == 'popBack':
            print y.pop()
        if i == 'pushFront':
            y.insert(0,counter)
            counter+=1     
    print y
    print vec 
_()
            
