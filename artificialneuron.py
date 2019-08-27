import math
import numpy as np
import matplotlib.pyplot as plt 

class Neuron():
    """
    Represents a artificial neuron.
    """
    def __init__(self, inputs=None, weights=None, threshold=None, activation_function=None):
        """
        Constructor of class

        :param inputs: list with values of inputs.
        :param weights: list of synaptic weights
        :param threshold: activation threshold
        :param activation_function: activation function
        """
        self.inputs = inputs
        self.weights = weights
        self.threshold = threshold
        self.activation_function = activation_function

    def get_potential(self):
        """
        Obtain the activation potential produced by the weighted sum of
        the inputs, by subtracting the activation threshold.

        :return u: activation potential
        """

        u = None
        sum = 0
        for index in range(0, len(self.inputs)):
            sum += self.inputs[index] * self.weights[index]
        
        u = sum - self.threshold

        return u
    
    def get_output(self, beta=None):
        """
        Generates outputs using activation function with
        activation potential as input.

        :return y: value of output
        """
        u = self.get_potential()
        if beta != None:
            y = self.activation_function(u, beta)
        else:
            y = self.activation_function(u)
        return y
    
def degree(number):
    if number >= 0:
        return 1
    else:
        return 0

def tan_hiperbolic(number, beta):
    return (1-math.e**((-beta)*number))/(1+math.e**((-beta)*number))

def logarithmic(number, beta):
    return 1/(1+math.e**((-beta)*number))

def question_2():
    arq = open('infos.txt', 'r')
    arq.readline()
    lines = arq.readlines()
    cont = 0
    letras = list("abcdefghijklmnopqrstuvwxyz")
    for line in lines:
        cont += 1
        letra = letras.pop(0)
        line = line.split(';')
        n_inputs = int(line[0])
        start = int(line[1].split(',')[0])
        stop = int(line[1].split(',')[1])
        num_points = int(line[2])
        weights = [float(i) for i in line[3].split(',')]
        threshold = float(line[4])
        beta = int(line[5])
        activation_function = logarithmic if int(line[6]) == 1 else tan_hiperbolic
        samples = np.linspace(start, stop, num_points)
        results = list()
        neuronio = Neuron()
        for inputs in samples:
            neuronio.inputs = n_inputs * [inputs]
            neuronio.weights = weights
            neuronio.threshold = threshold
            neuronio.activation_function = activation_function
            results.append(neuronio.get_output(beta))
        fig, ax = plt.subplots()
        ax.plot(samples, results)
        plt.xlabel('Sinais de entrada')
        plt.ylabel('Saída do neurônio')
        plt.title("Letra {0}) - Valores de saída de um neorônio artificial".format(letra))
        
        plt.savefig("./plots/plot-{0}.png".format(cont))

if __name__=='__main__':
    inputs = [1, 1]
    weights = [1.0, 1.0]
    threshold = 1.1
    neuronio = Neuron(inputs, weights, threshold, degree)
    print("Neuron Artificial\nInputs: {0}\nWeights: {1}\nThreshold: {2}\nOutput: {3}".format(\
           inputs, weights,threshold, neuronio.get_output()))
    question_2()

