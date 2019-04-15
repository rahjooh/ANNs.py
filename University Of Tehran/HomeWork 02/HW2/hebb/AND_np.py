import numpy as np

X = np.array(([-1, -1], [-1, 1], [1,-1], [1,1]), dtype=float)
y = np.array(([-1,-1,-1, 1]), dtype=float)


# X = np.array(([-1, 1], [-2, 2], [-3,3], [-4,4]), dtype=float)
w = np.array(([0,0,0]), dtype=float)
bias =  np.ones((4,1))

input = np.append(X,bias,axis=1)

print(np.dot(input[0], w))

# for i in range(input.shape[0]-1,-1,-1):
for i in range(input.shape[0]):
    print('i:', i, '  input:', input[i], '  y:',y[i],'  w:', w, '  dot:', np.dot(input[i], y[i]), '  w:', end='')
    w += np.dot(input[i], y[i])
    print(w)
