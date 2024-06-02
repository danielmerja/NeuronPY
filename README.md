# Logic Gate Neural Network Trainer

## Overview
This project implements a simple neural network to learn the behavior of basic logic gates (AND, OR, NAND, XOR) using Python. The neural network uses a single-layer perceptron model with a sigmoid activation function. The training process uses numerical gradient estimation to update the weights and bias based on the mean squared error cost function.

## Features
- Training neural networks to simulate logic gates.
- Configurable parameters such as learning rate, number of iterations, and epsilon for gradient estimation.
- Easy switching between different logic gate training sets via configuration.

## Installation
No external libraries are required for the main functionality as it uses only NumPy, which can be installed via pip if not already available:

```bash
pip install numpy
```

## Usage
The project is divided into two main files:
- `config.py`: Contains all configurable parameters and training data sets.
- `main.py`: Contains the neural network model, training logic, and performance evaluation.

To run the training process, execute the following command in your terminal:

```bash
python main.py
```

## Configuration
Modify the `config.py` file to change the learning parameters or switch between different logic gates. Here’s a brief explanation of the configuration options available:

- `learning_rate`: How quickly the network adjusts its weights in response to the error.
- `epsilon`: A small number used for numerical gradient approximation.
- `max_iterations`: The total number of training iterations to perform.
- `random_seed`: Seed for NumPy's random number generator to ensure reproducibility.
- `default_training_set`: Choose which logic gate to train on (AND, OR, NAND, XOR).

Example of changing a configuration in `config.py`:

```python
learning_rate = 0.05  # Reduce learning rate for slower convergence
default_training_set = training_data_xor  # Change to XOR gate training
```

## Customizing Training Data
You can add new logic gates or different kinds of training data by editing the `config.py` file. Ensure each new dataset follows the format shown for existing gates, i.e., an array of input-output pairs.

## Output
After running `main.py`, the terminal will display the cost after each training epoch, along with the final learned weights and biases. It also evaluates the trained model on all possible inputs for the selected logic gate to demonstrate the performance.

## Contributing
Contributions to this project are welcome. Please ensure to keep the structure consistent, and add or update the corresponding configurations and documentation as needed.
