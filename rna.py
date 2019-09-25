from random import uniform
import math 
import numpy as np

class Neuron:
    def __init__(self,  inputs_size, activation=None, beta=1):
        self.activation = activation
        self.beta = beta
        self.weights = np.array([uniform(0,1) for i in range(np.size(inputs_size + 1))])
    
    def get_output(self, inputs):
        
        _inputs = [-1]
        _inputs.extend(inputs)
        
        _inputs = np.array(_inputs)
        if np.size(_inputs) != np.size(self.weights):
            raise ValueError("Quantidade de entradas menor do que a de pesos")
        u = (_inputs * self.weights).sum()
        y = self.activation(u, self.beta)
        return y

def degree_bipolar(number, beta=None):
    if number >= 0:
        return 1
    else:
        return -1

def degree(number, beta=None):
    if number >= 0:
        return 1
    else:
        return 0

def tan_hiperbolic(number, beta):
    return (1-math.e**((-beta)*number))/(1+math.e**((-beta)*number))

def logistic(number, beta):
    return 1/(1+math.e**((-beta)*number))

def linear(number, beta):
    return number


class HiddenLayer:
    def __init__(self, inputs_size, size, activation=None, beta=1, *args, **kwargs):
        self.size = size
        self.neurons = [ Neuron(inputs_size, activation=activation, beta=beta) for i in range(size)]
        super().__init__(*args, **kwargs)
    
    def set_activation(self, activation, neuron_index=None):
        if neuron_index == None:
            for i in range(self.size):
                self.neurons[i].activation = activation
        else:
            self.neurons[neuron_index - 1].activation = activation
    
    def set_weights(self, weigths, neuron_index):
        self.neurons[neuron_index - 1].weights = weigths
    
    def set_threshold(self, threshold, neuron_index):
        self.neurons[neuron_index - 1].weights[0] = threshold
    
    def set_beta(self, beta, neuron_index):
        self.neurons[neuron_index - 1].beta = beta

    def get_output(self, inputs):
        return [neuron.get_output(inputs) for neuron in self.neurons]

class OutputLayer:
    def __init__(self,inputs_size, size, activation=None, beta=1):
        self.size = size
        self.neurons = [ Neuron(inputs_size, activation=activation, beta=beta) for i in range(size)]
    
    def set_activation(self, activation, neuron_index=None):
        if neuron_index == None:
            for i in range(self.size):
                self.neurons[i].activation = activation
        else:
            self.neurons[neuron_index - 1].activation = activation

    def set_weights(self, weights, neuron_index):
        self.neurons[neuron_index - 1].weights = weights
    
    def set_threshold(self, threshold, neuron_index):
        self.neurons[neuron_index - 1].weights[0] = threshold
    
    def set_beta(self, beta, neuron_index):
        self.neurons[neuron_index - 1].beta = beta
    
    def get_output(self, inputs):
        return [i.get_output(inputs) for i in self.neurons]

class InputLayer:
    def __init__(self, inputs, *args, **kwargs):
        self.inputs = inputs
        self.size = len(self.inputs)
        super().__init__(*args, **kwargs)
    
    def get_size(self):
        return self.size
    
    def get_inputs(self):
        return self.inputs