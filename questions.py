import rna
from feedforward import Feedforward
from xlrd import open_workbook
import numpy as np

def iib():
    network = Feedforward(inputs_size=1, hidden_sizes=[3], outputs_size=1)

    network.set_weigths(weights=[3.38888, 0.962803], layer_index=1, neuron_index=1)
    network.set_weigths(weights=[11.0847, 1.88752], layer_index=1, neuron_index=2)
    network.set_weigths(weights=[1.55095, 2.51054], layer_index=1, neuron_index=3)
    network.output_layer.set_weights(weights=[-0.4186, -1.9956, 1.625224, 0.88538], neuron_index=1)

    network.set_activation(activation=rna.tan_hiperbolic, layer_index=1)
    
    network.output_layer.set_activation(activation=rna.linear)

    xlsx_file = open_workbook('RNA_Aproximação_Universal_PPB.xls')
    values_x1 = [i.value for i in xlsx_file.sheet_by_index(0).col(0)[1:]]
    print([network.get_outputs([i]) for i in values_x1])

def iia():
    wt= [[0,0,0],[0.5, 1, 1], [0.25, 0.5, 1], [-0.5,-0.5,1], [-1,-1,-1]] #Settings of weights and thresholds
    N = 20 #número
    inputs = [[i, i] for i in np.linspace(0, 1, N, endpoint=True)]
    network = Feedforward(inputs_size=2, outputs_size=1, activation=rna.logistic, beta=1)

def l3p2a():
    pass

def l3p2b():
    pass

def l5p2():
    pass