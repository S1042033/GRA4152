import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from dataloader_module import MNIST


class NeuralNetworks(tf.keras.Model):
    """
    Base class for creating neural network models using TensorFlow.

    Attributes
    ----------
    _hidden : tf.keras.layers.Layer or None
        Hidden layers of the neural network, to be defined in subclasses.
    _cls : tf.keras.models.Sequential
        The classifier layer of the neural network.
    _params : list of tf.Tensor or None
        List of trainable parameters of the neural network, to be defined in subclasses.

    Parameters
    ----------
    neurons : int
        Number of neurons to use in the neural network.
    y_dim : int
        The dimensionality of the output space (number of classes).
    """
    def __init__(self, neurons, y_dim):
        super().__init__()
        self._hidden = None
        self._cls = self._classifier(neurons, y_dim)
        self._params = None

    def _classifier(self, neurons, y_dim):
        """
        Creates a classifier layer for the neural network.

        Parameters
        ----------
        neurons : int
            Number of neurons in the classifier.
        y_dim : int
            The dimensionality of the output space.

        Returns
        -------
        tf.keras.models.Sequential
            A Sequential model representing the classifier.
        """
        cls = Sequential([layers.InputLayer(input_shape=neurons), 
                          layers.Dense(y_dim, activation='softmax')])
        return cls

    def _get_cls(self):
        """
        Returns
        -------
        tf.keras.models.Sequential
            The classifier layer of the neural network.
        """
        return self._cls
    
    def call(self, inputs):
        """
        Forward pass for the neural network.

        Parameters
        ----------
        inputs : tuple
            Tuple containing input data and true labels.

        Returns
        -------
        tf.Tensor
            Computed loss of the neural network.
        """
        x, y = inputs
        out = self._hidden(x)
        out = self._cls(out)
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y, out))
        return loss
    
    def test(self, x):
        """
        Tests the model on the provided input data.

        Parameters
        ----------
        x : tf.Tensor
            Input data for testing.

        Returns
        -------
        tuple
            Tuple containing the (pseudo)probabilities and the predicted labels.
        """
        out = self._hidden(x)
        out = self._cls(out)
        y_hat = tf.math.argmax(out, 1)
        return out, y_hat
    
    def train(self, inputs, optimizer):
        """
        Trains the model on the provided input data.

        Parameters
        ----------
        inputs : tuple
            Tuple containing input data and true labels.
        optimizer : tf.keras.optimizers.Optimizer
            Optimizer to use for training.

        Returns
        -------
        tf.Tensor
            Computed loss of the neural network after the training step.
        """
        with tf.GradientTape() as tape:
            loss = self.call(inputs)
        gradients = tape.gradient(loss, self._params)
        optimizer.apply_gradients(zip(gradients, self._params))

        return loss
    

class FullyConNN(NeuralNetworks):
    """
    Fully connected neural network class inheriting from NeuralNetworks.

    Parameters
    ----------
    neurons : int, optional
        Number of neurons in each layer.
    input_shape : int, optional
        Input shape of the data.
    y_dim : int, optional
        The dimensionality of the output space (number of classes).
    """
    def __init__(self, neurons=50, input_shape=784, y_dim=10):
        super().__init__(neurons, y_dim)
        self._hidden = self._hidden_layers(neurons, input_shape)
        self._params = self._get_cls().trainable_variables + self._hidden.trainable_variables

    def _hidden_layers(self, neurons, input_shape):
        """
        Creates hidden layers for the fully connected neural network. It creates an input layer
        and two dense layers.

        Parameters
        ----------
        neurons : int
            Number of neurons in each layer.
        input_shape : int
            Input shape of the data.

        Returns
        -------
        tf.keras.models.Sequential
            A Sequential model representing the hidden layers.
        """
        return Sequential([layers.InputLayer(input_shape=input_shape),
                           layers.Dense(neurons), 
                           layers.Dense(neurons)
                           ])
    
    def __repr__(self):
        """
        Returns a string representation of the Fully Connected Neural Network.

        Returns
        -------
        str
            String representation of the network.
        """
        return (f"Fully Connected Neural Network with:("
                f"Number of trainable variables={len(self._params)}, "
                f"Input shape={self._hidden.layers[0].input_shape})")


class ConNN(NeuralNetworks):
    """
    Convolutional neural network class inheriting from NeuralNetworks.

    Parameters
    ----------
    neurons : int, optional
        The number of filters in the final convolutional layer.
    input_shape : tuple of int, optional
        Input shape of the data (height, width, channels).
    filters : int, optional
        Number of filters in the first convolutional layer, and half the filters in the second.
    kernel_size : int, optional
        Size of the kernel in the convolutional layers.
    strides : tuple of int, optional
        Strides for the convolutional layers.
    y_dim : int, optional
        The dimensionality of the output space (number of classes).
    """
    def __init__(self, neurons=50, input_shape=(32,32,3), filters=32, kernel_size=3, strides=(2,2), y_dim=10):
        super().__init__(neurons, y_dim)
        self._hidden = self._hidden_layers(neurons, input_shape, filters, kernel_size, strides)
        self._params = self._get_cls().trainable_variables + self._hidden.trainable_variables

    def _hidden_layers(self, neurons, input_shape, filters, kernel_size, strides):
        """
        Creates hidden layers for the convolutional neural network. It creates an input layer and three
        convolutional layers.

        Parameters
        ----------
        neurons : int
            The number of filters in the final convolutional layer.
        input_shape : tuple of int
            Input shape of the data (height, width, channels).
        filters : int
            Number of filters in the first convolutional layer, and half the filters in the second.
        kernel_size : int
            Size of the kernel in the convolutional layers.
        strides : tuple of int
            Strides for the first two convolutional layers.

        Returns
        -------
        tf.keras.models.Sequential
            A Sequential model representing the hidden layers.
        """
        return Sequential([layers.InputLayer(input_shape=input_shape), 
                           layers.Conv2D(filters=filters, kernel_size=kernel_size, strides=strides), 
                           layers.Conv2D(filters=2*filters, kernel_size=kernel_size, strides=strides), 
                           layers.Conv2D(filters=neurons, kernel_size=kernel_size, strides=(5,5)), layers.Flatten()
                           ])
    
    def __repr__(self):
        """
        Returns a string representation of the Convolutional Neural Network.

        Returns
        -------
        str
            String representation of the network.
        """
        return (f"Convolutional Neural Network with:("
                f"Number of trainable variables={len(self._params)}, "
                f"Input shape={self._hidden.layers[0].input_shape})")
