# MNIST Handwritten Digits Classification

This project implements a simple neural network for classifying handwritten digits from the **MNIST dataset**. The dataset contains grayscale images of digits (0-9), and the model predicts the correct digit.

---

## Features

- **Dataset**: [MNIST Handwritten Digits](http://yann.lecun.com/exdb/mnist/) (normalized to [0, 1]).
- **Model Architecture**:
  - Input Layer: 784 neurons (flattened 28x28 images).
  - Hidden Layers:
    - Layer 1: 25 neurons with ReLU activation.
    - Layer 2: 15 neurons with ReLU activation.
  - Output Layer: 10 neurons (one for each digit).
- **Loss Function**: Sparse Categorical Crossentropy.
- **Optimizer**: Adam optimizer.
- **Metrics**: Accuracy.
- **Visualizations**:
  - Training and validation loss plots.
  - Predicted vs. actual labels for random images.
  - Error analysis.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Torajabu/multiclass-classifcation-simple-neural-network--mnist-handwritten-dataset.git

"""
Navigate to the project directory:
cd multiclass-classifcation-simple-neural-network--mnist-handwritten-dataset


Install dependencies:

pip install tensorflow numpy matplotlib sklearn

Run the script:

    python mnist_neural_network.py

Results

    Model Performance:
        Training and validation loss reduce consistently over epochs.
        Random predictions on MNIST images with correct/incorrect classification are visualized.
    Misclassified Images:
        The total number of errors is displayed along with the incorrectly classified images.

For detailed results, check the Results Folder.
Notes

    Acknowledgment: The MNIST dataset is publicly available and was created by Yann LeCun and colleagues. For more information, visit MNIST.
    Model Customization:
        Add more layers or neurons to improve performance.
        Experiment with learning rates or activation functions (tanh, etc.).
        Use dropout layers to prevent overfitting
