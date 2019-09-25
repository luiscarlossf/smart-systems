import rna
from xlrd import open_workbook

class Feedforward:
    def __init__(self, inputs_size, outputs_size, activation=None, beta=1):
        self.inputs_size = inputs_size
        self.outputs_size = outputs_size
        self.output_layer = rna.OutputLayer(inputs_size, outputs_size, activation=activation, beta=beta)
    
    def get_outputs(self, inputs, beta=1):
        return self.output_layer.get_output(inputs)

class MultiFeedforward:
    def __init__(self, inputs_size, outputs_size, hidden_sizes=None, activation=None,  beta=1):
        self.inputs_size = inputs_size
        self.outputs_size = outputs_size
        self.hidden_sizes = hidden_sizes
        self.hidden_layers = list()
        if self.hidden_sizes != None:
            for i in range(len(self.hidden_sizes)):
                self.hidden_layers.append(rna.HiddenLayer(self.inputs_size, hidden_sizes[i], activation=activation))
                self.inputs_size = hidden_sizes[i]
        self.output_layer = rna.OutputLayer(self.inputs_size, outputs_size, activation=activation, beta=beta)
    
    def set_activation(self, activation, layer_index):
        self.hidden_layers[layer_index-1].set_activation(activation)
    
    def set_weigths(self, weights, layer_index, neuron_index):
        self.hidden_layers[layer_index - 1].set_weights(weights, neuron_index)
    
    def get_outputs(self, inputs, beta=1):
        if self.hidden_sizes != None:
            output_layer = self.hidden_layers[0].get_output(inputs)
            for hidden in self.hidden_layers[1:]:
                output_layer = hidden.get_output(output_layer)

        return self.output_layer.get_output(output_layer)

if __name__ == "__main__":

    network = MultiFeedforward(inputs_size=1, hidden_sizes=[3], outputs_size=1)

    network.set_weigths(weights=[3.38888, 0.962803], layer_index=1, neuron_index=1)
    network.set_weigths(weights=[11.0847, 1.88752], layer_index=1, neuron_index=2)
    network.set_weigths(weights=[1.55095, 2.51054], layer_index=1, neuron_index=3)
    network.output_layer.set_weights(weights=[-0.4186, -1.9956, 1.625224, 0.88538], neuron_index=1)

    network.set_activation(activation=rna.tan_hiperbolic, layer_index=1)
    
    network.output_layer.set_activation(activation=rna.linear)

    xlsx_file = open_workbook('RNA_Aproximação_Universal_PPB.xls')
    values_x1 = [i.value for i in xlsx_file.sheet_by_index(0).col(0)[1:]]
    print([network.get_outputs([i]) for i in values_x1])
