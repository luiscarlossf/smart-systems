from random import choices

class Group:
    def __init__(self, center):
        self.x = center[0]
        self.y = center[1]
        self.samplesx = list()
        self.samplesy = list()
    
    def recalcula(self):
        anterior = (self.x, self.y)
        self.x = sum(self.samplesx)/len(self.samplesx)
        self.y = sum(self.samplesy)/len(self.samplesy)
        self.samplesx = list()
        self.samplesy = list()
        return anterior != (self.x, self.y)
    
    def set_sample(self, sample):
        self.samplesx.append(sample['x'])
        self.samplesx.append(sample['y'])
    
    def __repr__(self):
        return "Group {0}\n center: {1}   samples: {2}\n".format(self, (self.x, self.y), [self.samplesx, self.samplesy])

def kmeans(k, samples):
    groups = [ Group(choices(samples, k=k)) for i in range(k)]
    recalcula = True
    while recalcula:
        recalcula = True
        for sample in samples:
            values = [(((sample['x'] - group.x) + (sample['y'] - group.y))) ** 2 for group in groups]
            minimo = min(values)
            groups[values.index(minimo)].set_sample(sample)
        for group in groups:
            recalcula = recalcula and group.recalcula()
    print(groups)

if __name__ == "__main__":
    samples = [{'cidade':1,'x':0.1990,'y':0.9442}, {'cidade':11, 'x':0.4397, 'y':0.1443}, {'cidade':2, 'x':0.6743, 'y':0.8386},
    {'cidade':12, 'x':0.7010,'y':0.6516},\
    {'cidade':3, 'x':0.9271, 'y':0.2584},\
    {'cidade':13, 'x':0.6097, 'y':0.9461},\
    {'cidade':4, 'x':0.3438, 'y':0.0429},\
    {'cidade':14, 'x':0.2999, 'y':0.8159},\
    {'cidade':5, 'x':0.5945,'y':0.0059},\
    {'cidade':15, 'x':0.8560, 'y':0.9302},\
    {'cidade':6, 'x':0.6155, 'y':0.5744},\
    {'cidade':16, 'x':0.1121, 'y':0.3099},\
    {'cidade':7, 'x':0.0034, 'y':0.7439},\
    {'cidade':17, 'x':0.2916, 'y':0.2688},\
    {'cidade':8, 'x':0.9820, 'y':0.8068},\
    {'cidade':18, 'x':0.0974, 'y':0.5365},\
    {'cidade':9, 'x':0.8995, 'y':0.6376},\
    {'cidade':19,'x':0.3974,'y':0.1633},\
    {'cidade':10,'x':0.6928,'y':0.2513},\
    {'cidade':20,'x':0.3333,'y':0.2110}]
    kmeans(2, samples)


