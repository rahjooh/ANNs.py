import glob,numpy as np

def read_files(path,TrainOrTest = 'train') :
    Train_files = glob.glob(path)
    Y = [] ; x = [] ; T = []
    for file in Train_files :
        y = []
        T.append(file[-6:-5])
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
    return np.array(x),np.array(Y),np.array(T)



def train(X,Y):
    bias = np.ones((X.shape[0], 1))
    input = np.append(X, bias, axis=1)
    w = np.random.rand(Y.shape[1],input.shape[1])
    # w = np.zeros(shape=(Y.shape[1],input.shape[1]))
    # print(X.shape, bias.shape, input.shape, w.shape, Y.shape)
    for i in range(input.shape[0]): # 0 - 20
        for j in range(Y.shape[1]):  # 0 - 7
            w[j] += input[i].T.dot(Y[i][j])
    return w

def test(X,W):
    bias = np.ones((X.shape[0], 1))
    input = np.append(X, bias, axis=1)
    y = input.dot(W.T)
    pred =[]
    switcher = { 1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"J", 7:"K" }
    for i in range(y.shape[0]):
        pred.append( switcher.get(np.unravel_index(y[i].argmax() , y[i].shape)[0]+1,"Unknown"))
    return pred,y


X_train ,Y_train , Target  = read_files("../TrainSetHW1/*.txt")
X_test ,Y_test ,Target = read_files("../TestSetHW1/*.txt")
# print('X_train : \n',X_train , X_train.shape)
# print('Y_train : \n',Y_train , Y_train.shape)

W = train(X_train,Y_train)
predictedVector,WightOfPredicts =test(X_test,W)
print(Target)
print(predictedVector)
print(WightOfPredicts)