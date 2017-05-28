x = [3,1,2,4]
y = 6

z = []
def _():
    for i in x:
        if i in z:
            return True
        else:
            z.append(abs(y-i))
    print z
    return False
print _()
