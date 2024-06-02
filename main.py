import numpy as np
from config import learning_rate, epsilon, max_iterations, random_seed, default_training_set

def sigmoid(x):
    """Sigmoid activation function."""
    return 1 / (1 + np.exp(-x))

def calculate_cost(weight_1, weight_2, bias, training_set):
    """Calculate the mean squared error cost across all training examples."""
    total_cost = 0.0
    for input_1, input_2, expected_output in training_set:
        predicted_output = sigmoid(input_1 * weight_1 + input_2 * weight_2 + bias)
        error = predicted_output - expected_output
        total_cost += error ** 2
    return total_cost / len(training_set)

def estimate_gradients(epsilon, weight_1, weight_2, bias, training_set):
    """Estimate the gradients of the cost function using numerical differentiation."""
    base_cost = calculate_cost(weight_1, weight_2, bias, training_set)
    gradient_w1 = (calculate_cost(weight_1 + epsilon, weight_2, bias, training_set) - base_cost) / epsilon
    gradient_w2 = (calculate_cost(weight_1, weight_2 + epsilon, bias, training_set) - base_cost) / epsilon
    gradient_b = (calculate_cost(weight_1, weight_2, bias + epsilon, training_set) - base_cost) / epsilon
    return gradient_w1, gradient_w2, gradient_b

# Set the random seed
np.random.seed(random_seed)

# Initialize weights and biases randomly
weight_1 = np.random.rand()
weight_2 = np.random.rand()
bias = np.random.rand()

# Training loop
for iteration in range(max_iterations):
    current_cost = calculate_cost(weight_1, weight_2, bias, default_training_set)
    print(f"Epoch {iteration}: Cost = {current_cost}, w1 = {weight_1}, w2 = {weight_2}, b = {bias}")
    grad_w1, grad_w2, grad_b = estimate_gradients(epsilon, weight_1, weight_2, bias, default_training_set)
    weight_1 -= learning_rate * grad_w1
    weight_2 -= learning_rate * grad_w2
    bias -= learning_rate * grad_b

# Final output
print("Trained parameters:")
print(f"Weight 1 = {weight_1}, Weight 2 = {weight_2}, Bias = {bias}")
