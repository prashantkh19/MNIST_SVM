# MNIST_SVM

### SVM CLASSIFIER ON MNIST DATASET
The MNIST database of handwritten digits, available online, has a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image.

Extract files - finalized_model_50000_f.zip and Input_Data.zip to the root folder

Repo contains three files-
1. input_data.py
2. train_model.py
3. test_model.py

## input_data.py
contains functions to convert MNIST dataset to array

## train_model.py
create and train the svm-classifier model (with auto gamma and c) with 50,000 images sample dataset

## test_model.py
test the model with 10,000 test images and calculating the accuracy

## RESULTS
I trained the svm model with 50,000 training images and tested the model with 10,000 test images
I got 94.34% acccuracy with this model.

##### final model is saved in finalized_model_50000_f.zip
