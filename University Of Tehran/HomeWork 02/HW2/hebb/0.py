import glob,numpy as np

def read_files(path) :
    Train_files = glob.glob(path)
    y = [] ; x = [] ;
    for file in Train_files :
        y.append(ord(file[-6:-5])-64)
        f =list(open(file,'r').read().replace('\n', ''))
        res = [x.replace('.','-1').replace('#','1') for x in f]
        res = [0 if x!='1' and x!='-1' else x for x in res]
        res = list(map(int, res))
        x.append(res)
    return np.array(x),np.array(y)


def train(X,Y):
    bias =  np.ones((X.shape[0],1))
    input = np.append(X,bias,axis=1)
    w = np.random.rand(input.shape[1])
    for i in range(input.shape[0]):
        w += np.dot(input[i], Y[i])
    print(X.shape,bias.shape,input.shape,Y.shape,w.shape)
    return w

X_train ,Y_train = read_files("../TrainSetHW1/*.txt")
X_test ,Y_test = read_files("../TestSetHW1/*.txt")
W = train(X_train,Y_train)
print(W)

def test(X,W):
    bias = np.ones((X.shape[0], 1))
    input = np.append(X, bias, axis=1)
    print(input.shape,W.shape)
    y = input.dot(W)
    print(y.shape)





test(X_test,W)



