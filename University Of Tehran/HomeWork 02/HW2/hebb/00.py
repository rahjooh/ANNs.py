import glob,numpy as np

def read_files(path) :
    Train_files = glob.glob(path)
    Y = [] ; x = [] ;
    for file in Train_files :
        y = []
        if file[-6:-5]=='A' : y.append(1) ;
        else : y.append(-1) ;
        if file[-6:-5]=='B' : y.append(1) ;
        else : y.append(-1) ;
        if file[-6:-5]=='C' : y.append(1) ;
        else : y.append(-1) ;
        if file[-6:-5]=='D' : y.append(1) ;
        else : y.append(-1) ;
        if file[-6:-5]=='E' : y.append(1) ;
        else : y.append(-1) ;
        if file[-6:-5]=='J' : y.append(1) ;
        else : y.append(-1) ;
        if file[-6:-5]=='K' : y.append(1) ;
        else : y.append(-1) ;
        Y.append(y)
        f =list(open(file,'r').read().replace('\n', ''))
        res = [x.replace('.','-1').replace('#','1') for x in f]
        res = [0 if x!='1' and x!='-1' else x for x in res]
        res = list(map(int, res))
        x.append(res)
    return np.array(x),np.array(Y)

def train(X,Y):
    bias = np.ones((X.shape[0], 1))
    input = np.append(X, bias, axis=1)

def train_np(X,Y):
    bias =  np.ones((X.shape[0],1))
    input = np.append(X,bias,axis=1)
    w = np.random.rand(input.shape[1],Y.shape[1])
    print(X.shape, bias.shape, input.shape, w.shape, Y.shape)
    for i in range(input.shape[0]):
        w += input[i].T.dot(Y[i])

    print(X.shape, bias.shape, input.shape, w.shape, Y.shape)
    return w

X_train ,Y_train = read_files("../TrainSetHW1/*.txt")
X_test ,Y_test = read_files("../TestSetHW1/*.txt")
W = train(X_train,Y_train)
print(W)
exit()
def test(X,W):
    bias = np.ones((X.shape[0], 1))
    input = np.append(X, bias, axis=1)
    print(input.shape,W.shape)
    y = input.dot(W)
    print(y.shape)




test(X_test,W)



