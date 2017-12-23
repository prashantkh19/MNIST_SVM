from input_data import get_labels,get_images
from sklearn import svm
import pickle
import numpy as np

train_data = get_images('train-images-idx3-ubyte/train-images.idx3-ubyte', length=50000)
train_labels = get_labels('train-labels-idx1-ubyte/train-labels.idx1-ubyte')

clf = svm.SVC()
train_data = np.asmatrix(train_data[:(50000*784)]).reshape(50000, 784)

clf.fit(train_data, train_labels[:50000])

# save the model to disk
filename = 'finalized_model_50000_f.sav'
pickle.dump(clf, open(filename, 'wb'))
print("Succeed!")