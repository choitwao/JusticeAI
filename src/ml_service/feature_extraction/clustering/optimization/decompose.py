from src.ml_service.ml_models.models import load_facts_from_bin
from sklearn import decomposition
import matplotlib.pyplot as plt
import numpy
import math
import joblib
import os
from src.ml_service.reporting.logger import Log
from src.ml_service.outputs.output import Log, Save

def optimal_feature_size(matrix, evaluate_percent, plot=False):
    numpy.random.shuffle(matrix)
    pca = decomposition.PCA()
    percent = math.floor((len(matrix)) * evaluate_percent)
    pca.fit_transform(matrix[:percent])
    scores = pca.explained_variance_ratio_.cumsum()
    index = 0
    for variance in scores:
        if variance >= 0.95:
            break
        index += 1
    if plot:
        plt.hist(scores, bins=100)
        plt.show()
    return index

def decompose(matrix, size):
    pca = decomposition.PCA(n_components=size)
    result = pca.fit_transform(matrix)
    return result

def execute():
    model = load_facts_from_bin()
    matrix = model[0]
    sentence = model[1]
    files = model[2]
    model = None
    Log.write("Computing optimal dimension reduction")
    size = optimal_feature_size(matrix, 1)
    Log.write('Optimal size: ' + str(size))
    Log.write("Decomposing matrix")
    new_matrix = decompose(matrix, size)
    Log.write('Saving Model')
    model = (new_matrix, sentence, files)
    s = Save('decomposed_model')
    s.binarize_model('decomposed_model.bin', model)


if __name__ == '__main__':
    execute()
