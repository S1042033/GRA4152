import tensorflow as tf

class DataLoader:
    """
    Super class for loading and preprocessing data for machine learning models.

    Attributes
    ----------
    _x_tr : np.ndarray
        Training data features (private).
    _x_te : np.ndarray
        Test data features (private).
    _y_tr : np.ndarray
        Training data labels (private).
    _y_te : np.ndarray
        Test data labels (private).

    """
    def __init__(self):
        """
        Initializes the DataLoader with null values for training and test data.
        """
        self._x_tr = None
        self._x_te = None
        self._y_tr = None
        self._y_te = None

    @property
    def x_tr(self):
        """
        Returns
        -------
        np.ndarray
            Training data features.
        """
        return self._x_tr

    @property
    def x_te(self):
        """
        Returns
        -------
        np.ndarray
            Test data features.
        """
        return self._x_te

    @property
    def y_tr(self):
        """
        Returns
        -------
        np.ndarray
            Training data labels.
        """
        return self._y_tr

    @property
    def y_te(self):
        """
        Returns
        -------
        np.ndarray
            Test data labels.
        """
        return self._y_te
    
    def _preprocess_data(self):
        """
        Internal method to preprocess the data, including normalization and one-hot encoding.
        """
        self._x_tr = self._x_tr.astype('float32') / 255
        self._x_te = self._x_te.astype('float32') / 255
        self._y_tr = tf.keras.utils.to_categorical(self._y_tr, num_classes=10)
        self._y_te = tf.keras.utils.to_categorical(self._y_te, num_classes=10)

    def loader(self, batch_size):
        """
        Creates a TensorFlow data loader with the given batch size.

        Parameters
        ----------
        batch_size : int
            Size of the batch for the data loader.

        Returns
        -------
        tf.data.Dataset
            A TensorFlow dataset object for the training data.
        """
        tf_dl = tf.data.Dataset.from_tensor_slices((self._x_tr, self._y_tr)) \
                    .shuffle(self._x_tr.shape[0]).batch(batch_size)
        return tf_dl


class MNIST(DataLoader):
    """
    DataLoader subclass for the MNIST dataset.
    """
    def __init__(self):
        """
        Initializes the MNIST dataset by loading data, reshaping and preprocessing the data.
        """
        super().__init__()
        (self._x_tr, self._y_tr), (self._x_te, self._y_te) = tf.keras.datasets.mnist.load_data(path='mnist.npz')
        self._x_tr = self._x_tr.reshape((-1, 28*28))
        self._x_te = self._x_te.reshape((-1, 28*28))
        self._preprocess_data()
      

class CIFAR10(DataLoader):
    """
    DataLoader subclass for the CIFAR-10 dataset.
    """
    def __init__(self):
        """
        Initializes the CIFAR10 dataset by loading and preprocessing the data.
        """
        super().__init__()
        (self._x_tr, self._y_tr), (self._x_te, self._y_te) = tf.keras.datasets.cifar10.load_data()
        self._preprocess_data()

