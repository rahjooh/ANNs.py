X_binary = [[0, 0], [0, 1], [1,0], [1,1]]
X_bipolar = [[-1, -1], [-1, 1], [1,-1], [1,1]]
Y_binary = [0,0,0, 1]
Y_bipolar = [-1,-1,-1, 1]
b = [1, 1, 1, 1]


print(' Binary Input - Binary Output')
w = [0,0,0]
for  i in range(3,-1,-1):
    w[0] = w[0]+ X_binary[i][0]*Y_binary[i]
    w[1] = w[1]+ X_binary[i][1]*Y_binary[i]
    w[2] = w[2]+ b[i]*Y_binary[i]

    print(' I:',i,end=' ')
    print(' X:',X_binary[i],end=' ')
    print(' B:', b[i], end=' ')
    print(' W:', w, end=' ')
    print(' Y:',Y_binary[i],end=' ')
    print()

print('\n Binary Input - Bipolar Output')
w = [0,0,0]
for  i in range(3,-1,-1):
    w[0] = w[0]+ X_binary[i][0]*Y_bipolar[i]
    w[1] = w[1]+ X_binary[i][1]*Y_bipolar[i]
    w[2] = w[2]+ b[i]*Y_bipolar[i]

    print(' I:',i,end=' ')
    print(' X:',X_binary[i],end=' ')
    print(' B:', b[i], end=' ')
    print(' W:', w, end=' ')
    print(' Y:',Y_bipolar[i],end=' ')
    print()

print('\n Bipolar Input - Bipolar Output')
w = [0,0,0]
for  i in range(3,-1,-1):
    w[0] = w[0]+ X_bipolar[i][0]*Y_bipolar[i]
    w[1] = w[1]+ X_bipolar[i][1]*Y_bipolar[i]
    w[2] = w[2]+ b[i]*Y_bipolar[i]

    print(' I:',i,end=' ')
    print(' X:',X_bipolar[i],end=' ')
    print(' B:', b[i], end=' ')
    print(' W:', w, end=' ')
    print(' Y:',Y_bipolar[i],end=' ')
    print()



