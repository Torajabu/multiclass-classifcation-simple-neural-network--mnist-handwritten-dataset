#consists of 10 classes, one for each digit from 0 to 9.

#Model Complexity: my model has a relatively simple architecture with only three dense layers. Increasing the complexity of the model by adding more layers or neurons might help improve performance.
#Training Epochs: Training the model for more epochs could lead to better learning, although I already trained for 40 epochs. You might want to experiment with different numbers of epochs.
#Data Preprocessing: Ensure that the data is normalized properly. The MNIST dataset ranges from 0 to 255, and I have already normalized it to 0-1, which is good.
#Learning Rate: The learning rate might be too high or too low. You can try adjusting it and see if it improves the model's performance.
#Overfitting: Overfitting might occur if the model is too complex. You can add dropout layers to prevent overfitting and improve generalization.
#Activation Functions: Using different activation functions in the hidden layers might also improve performance. You can experiment with other activation functions like tanh.

#FOR OUTPUTS OF THIS NEURAL NETWORK , PLEASE REFER TO https://github.com/Torajabu/multiclass-classifcation-simple-neural-network--mnist-handwritten-dataset/tree/main/SIMPLE%20NEURAL%20NET%20RESULTS%20MNIST



import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

# Function to load and preprocess the MNIST dataset
def load_data():
    (X_train, y_train), (X_val, y_val) = tf.keras.datasets.mnist.load_data()

    # Normalize the input data
    X_train = X_train.reshape(X_train.shape[0], -1).astype('float32') / 255
    X_val = X_val.reshape(X_val.shape[0], -1).astype('float32') / 255

    return X_train, y_train, X_val, y_val

# Load the data
X_train, y_train, X_val, y_val = load_data()

# Model Definition
tf.random.set_seed(1234)  # for consistent results
model = tf.keras.Sequential([
    Dense(25, activation='relu', input_shape=(784,), name='L1'),
    Dense(15, activation='relu', name='L2'),
    Dense(10, activation='linear', name='L3')
], name="my_model")

# Model Compilation
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Model Training
history = model.fit(X_train, y_train, epochs=10, batch_size=128, validation_data=(X_val, y_val))

# Plotting Loss
def plot_loss_tf(history):
    plt.plot(history.history['loss'], label='train')
    if 'val_loss' in history.history:
        plt.plot(history.history['val_loss'], label='val')
    plt.title('Model Loss')
    plt.xlabel('Epochs')
    plt.legend()
    plt.show()

plot_loss_tf(history)

# Visualization Code
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

m, n = X_train.shape

fig, axes = plt.subplots(8, 8, figsize=(5, 5))
fig.tight_layout(pad=0.13, rect=[0, 0.03, 1, 0.91])

for i, ax in enumerate(axes.flat):
    random_index = np.random.randint(m)
    X_random_reshaped = X_train[random_index].reshape((28, 28))
    ax.imshow(X_random_reshaped, cmap='gray')

    # Predict using the Neural Network
    prediction = model.predict(X_train[random_index].reshape(1, 784))
    prediction_p = tf.nn.softmax(prediction)
    yhat = np.argmax(prediction_p)

    # Display the label above the image
    ax.set_title(f"{y_train[random_index]},{yhat}", fontsize=10)
    ax.set_axis_off()

fig.suptitle("Label, yhat", fontsize=14)
plt.show()

# Display Errors Function
def display_errors(model, X, y):
    f = model.predict(X)
    yhat = np.argmax(f, axis=1)
    misclassified = yhat != y
    idxs = np.where(misclassified)[0]
    return len(idxs)

print(f"{display_errors(model, X_val, y_val)} errors out of {len(X_val)} images")

model.summary()

# BEGIN UNIT TEST
# Placeholder function for unit testing
def test_model(model, units, input_shape):
    assert model.input_shape == (None, input_shape)
    assert model.output_shape == (None, units)
    print("Model passed unit tests.")
    
test_model(model, 10, 784)
# END UNIT TEST

[layer1, layer2, layer3] = model.layers

# Examine Weights shapes
W1, b1 = layer1.get_weights()
W2, b2 = layer2.get_weights()
W3, b3 = layer3.get_weights()
print(f"W1 shape = {W1.shape}, b1 shape = {b1.shape}")
print(f"W2 shape = {W2.shape}, b2 shape = {b2.shape}")
print(f"W3 shape = {W3.shape}, b3 shape = {b3.shape}")

model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
)

history = model.fit(
    X_train, y_train,
    epochs=40,
    validation_data=(X_val, y_val)
)

plot_loss_tf(history)

# Display a specific digit
def display_digit(image):
    plt.imshow(image.reshape((28, 28)), cmap='gray')
    plt.show()

image_of_two = X_train[1015]
display_digit(image_of_two)

prediction = model.predict(image_of_two.reshape(1, 784))

print(f"Predicting a Two: \n{prediction}")
print(f"Largest Prediction index: {np.argmax(prediction)}")

prediction_p = tf.nn.softmax(prediction)

print(f"Predicting a Two. Probability vector: \n{prediction_p}")
print(f"Total of predictions: {np.sum(prediction_p):0.3f}")

yhat = np.argmax(prediction_p)

print(f"np.argmax(prediction_p): {yhat}")

warnings.simplefilter(action='ignore', category=FutureWarning)

m, n = X_train.shape

fig, axes = plt.subplots(8, 8, figsize=(5, 5))
fig.tight_layout(pad=0.13, rect=[0, 0.03, 1, 0.91])  # [left, bottom, right, top]
for i, ax in enumerate(axes.flat):
    random_index = np.random.randint(m)
    
    X_random_reshaped = X_train[random_index].reshape((28, 28))
    ax.imshow(X_random_reshaped, cmap='gray')
    
    prediction = model.predict(X_train[random_index].reshape(1, 784))
    prediction_p = tf.nn.softmax(prediction)
    yhat = np.argmax(prediction_p)
    
    ax.set_title(f"{y_train[random_index]},{yhat}", fontsize=10)
    ax.set_axis_off()
fig.suptitle("Label, yhat", fontsize=14)
plt.show()

print(f"{display_errors(model, X_val, y_val)} errors out of {len(X_val)} images")
