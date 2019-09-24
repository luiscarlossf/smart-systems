import random

class Neuron():
    def __init__(self, inputs, activation, beta=None, weights=None, *args, **kwargs):
        self.inputs = [-1].extend(inputs)
        self.activation = activation
        self.beta = beta
        if weights == None:
            self.weigths = [random.rand(0,1) for i in range(len(self.inputs))]
        else:
            self.weights = weights
        
        super().__init__(*args, **kwargs)
    
    def get_output():
        pass

def degree_bipolar(number, beta):
    if number >= 0:
        return 1
    else:
        return -1

def degree(number, beta):
    if number >= 0:
        return 1
    else:
        return 0

def tan_hiperbolic(number, beta):
    return (1-math.e**((-beta)*number))/(1+math.e**((-beta)*number))

def logarithmic(number, beta):
    return 1/(1+math.e**((-beta)*number))


class HiddenLayer:
    def __init__(self, size, activation, *args, **kwargs):
        super().__init__(*args, **kwargs)

class OutputLayer:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class InputLayer:
    def __init__(self, inputs, *args, **kwargs):
        self.inputs = inputs
        self.size = len(self.inputs)
        super().__init__(*args, **kwargs)
    
    def getSize():
        return self.size