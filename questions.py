import rna
from feedforward import Feedforward
from xlrd import open_workbook
import numpy as np
from random import uniform
import matplotlib.pyplot as plt

def l2p2b():
    network = Feedforward(inputs_size=1, hidden_sizes=[3], outputs_size=1)

    network.set_weigths(weights=[3.38888, 0.962803], layer_index=1, neuron_index=1)
    network.set_weigths(weights=[11.0847, 1.88752], layer_index=1, neuron_index=2)
    network.set_weigths(weights=[1.55095, 2.51054], layer_index=1, neuron_index=3)
    network.output_layer.set_weights(weights=[-0.4186, -1.9956, 1.625224, 0.88538], neuron_index=1)

    network.set_activation(activation=rna.tan_hiperbolic, layer_index=1)
    
    network.output_layer.set_activation(activation=rna.linear)

    xlsx_file = open_workbook('RNA_Aproximação_Universal_PPB.xls')
    values_x1 = [i.value for i in xlsx_file.sheet_by_index(0).col(0)[1:]]
    y = [network.get_outputs([i])[0] for i in values_x1]
    plt.plot(values_x1, y)
    plt.xlabel('x1')
    plt.ylabel('y')

    plt.title("L2P2B")
    plt.savefig('./plots/l2p2b.png')

def l2p2a():
    wts= [[0,0,0],[0.5, 1, 1], [0.25, 0.5, 1], [-0.5,-0.5,1], [-1,-1,-1]] #Settings of weights and thresholds
    N = 20 #número
    inputs = [i for i in np.linspace(0,20, endpoint=True)]
    network = Feedforward(inputs_size=2, outputs_size=1, activation=rna.logistic, beta=1)

    for wt in wts:
        #network.output_layer.set_weights(wt, 1)
        y = [ network.get_outputs([inp, inp])[0] for inp in inputs]
        fig, ax = plt.subplots()
        ax.plot(inputs, y, label="Thresholds and weights: {0}".format(network.get_weights()))
        plt.xlabel('x1, x2')
        plt.ylabel('y')
        plt.title("L2P2A1")
        plt.legend()
        plt.savefig('./plots/l2p2a1-{0}.png'.format(wt))

    network = Feedforward(inputs_size=2, outputs_size=1, activation=rna.tan_hiperbolic, beta=1)

    for wt in wts:
        #network.output_layer.set_weights(wt, 1)
        y = [ network.get_outputs([inp, inp])[0] for inp in inputs]
        fig, ax = plt.subplots()
        ax.plot(inputs, y, label="Thresholds and weights: {0}".format(wt))
        plt.xlabel('x1, x2')
        plt.ylabel('y')
        plt.title("L2P2A2")
        plt.legend()
        plt.savefig('./plots/l2p2a2-{0}.png'.format(wt))
    
    network = Feedforward(inputs_size=2, hidden_sizes=[10], outputs_size=1, activation=rna.logistic, beta=1)

    for wt in wts:
        #network.output_layer.set_weights(wt, 1)
        y = [ network.get_outputs([inp, inp])[0] for inp in inputs]
        fig, ax = plt.subplots()
        ax.plot(inputs, y, label="Thresholds and weights: {0}".format(wt))
        plt.xlabel('x1, x2')
        plt.ylabel('y')
        plt.title("L2P2A3")
        plt.legend()
        plt.savefig('./plots/l2p2a3-{0}.png'.format(wt))
    



def l3p2a():
    pass

def l3p2b():
    pass

def l5p2():
    pass

if __name__ == "__main__":
    l2p2a()