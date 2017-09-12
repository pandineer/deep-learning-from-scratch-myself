class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None # Loss
        self.y = None    # output of softmax
        self.t = None    # training data(one-hot vector)

    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)

        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size

        return dx
