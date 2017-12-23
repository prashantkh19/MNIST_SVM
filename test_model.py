from input_data import get_labels,get_images
import pickle
import numpy as np

filename = 'finalized_model_50000_f.sav'

# load the model from disk
clf = pickle.load(open(filename, 'rb'))

test_data=get_images('t10k-images-idx3-ubyte/t10k-images.idx3-ubyte',True)  # True: for full length
test_labels=get_labels('t10k-labels-idx1-ubyte/t10k-labels.idx1-ubyte')

test_data = np.asmatrix(test_data).reshape(10000, 784)
result = clf.score(test_data, test_labels)
print("Accuracy: ",result)
