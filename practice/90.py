x = [['*','*','*,','^','*','*','*,'],\
    ['*','*','*,','|','*','*','*,'],\
    ['*','*','*,','|','*','*','*,'],\
    ['*','*','*,','_','*','*','*,']]
y = [['*','*','*','*'] for i in range(len(x[0]))]
for i in range(len(x)):
    for j in range(len(x[i])):
        import pdb;pdb.set_trace()
        y[j][len(x)-i-1] = x[i][j]
print y 
