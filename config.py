import numpy as np

# Configuration for the neural network training

# Learning parameters
learning_rate = 0.1
epsilon = 0.1  # Small value for numerical gradient approximation
max_iterations = 10000  # Number of iterations for training

# Random seed for reproducibility
random_seed = 0

# Training data for different logic gates
training_data_or = np.array([
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 1]
])

training_data_and = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
])

training_data_nand = np.array([
    [0, 0, 1],
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 0]
])

training_data_xor = np.array([
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 0]
])

# Default training data set to AND gate
default_training_set = training_data_and
