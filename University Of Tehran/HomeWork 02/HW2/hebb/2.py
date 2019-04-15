import numpy as np

# X = (hours sleeping, hours studying), y = score on test
X = np.array(([-1, -1], [-1, 1], [1,-1], [1,1]), dtype=float)
y = np.array(([-1,-1,-1, 1]), dtype=float)

# scale units
# X = X/np.amax(X, axis=0) # maximum of X array
# y = y/100 # max test score is 100

class Neural_Network(object):
  def __init__(self):
    #parameters
    self.inputSize = 2
    self.outputSize = 1
    self.hiddenSize = 0

    #weights
    self.W = np.random.randn(self.inputSize, self.outputSize) # (64x7) weight matrix from input to hidden layer


  def forward(self, X):
    #forward propagation through our network
    self.z = np.dot(X, self.W) # dot product of X (input) and first set of 3x2 weights
    return self.sigmoid(self.z) # activation function



  def sigmoid(self, s):
    # activation function
    return s #1/(1+np.exp(-s))


NN = Neural_Network()

#defining our output
o = NN.forward(X)

print ("Predicted Output: \n" + str(o))
print ("Actual Output: \n" + str(y))
