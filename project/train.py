import tensorflow as tf
from dataloader_module import MNIST, CIFAR10
from NN_module import FullyConNN, ConNN
import argparse, textwrap
from sklearn.metrics import roc_auc_score

# Command-line argument parsing
parser = argparse.ArgumentParser(prog='train.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
                                     Train a neural network model on either the MNIST or CIFAR10 dataset.
                                    ------------------------------------------------------------------------------------------------------------------------

                                     This script allows the user to specify the type of neural network (Fully Connected or Convolutional),
                                     the number of epochs for training, the number of neurons, the batch size, and the dataset to be used
                                     (MNIST or CIFAR10). Note that the Fully Connected NN should only be used with the MNIST data set, 
                                     and the Convolutional NN should only be used with the CIFAR10 data set.

                                     Arguments:
                                     --nn_type: The type of neural network to use ('fully_con' for Fully Connected NN or 'conv' for Convolutional NN).
                                     --epochs: The number of epochs for training the model (default: 10).
                                     --neurons: The number of neurons in the network (default: 50).
                                     --batch_size: The size of batches for training the model (default: 256).
                                     --dset: The dataset to use for training the model ('mnist' or 'cifar10').

                                     The script uses an Adam optimizer with a learning rate of 5e-4 for training and computes the area under the
                                     ROC curve (AUC) as a performance metric after training.
                                     
                                    '''),
        epilog=textwrap.dedent('''\
                                    ------------------------------------------------------------------------------------------------------------------------
                                     Eksamples of terminal commands:
                                     python3 train.py --dset cifar10 --nn_type conv --epochs 10                                 
                                     python3 train.py --dset mnist --nn_type fully_con --epochs 10
                                     
                               ''')
                    )


parser.add_argument("--nn_type", type=str, choices=["fully_con", "conv"], required=True)
parser.add_argument("--epochs", type=int, default=10)
parser.add_argument("--neurons", type=int, default=50)
parser.add_argument("--batch_size", type=int, default=256)
parser.add_argument("--dset", type=str, choices=["mnist", "cifar10"], required=True)
args = parser.parse_args()

# Ensure proper input arguments
# including that ConvNN is used only with CIFAR10 and FullyConNN only with MNIST
assert not (args.nn_type == "conv" and args.dset != "cifar10"), "ConvNN must be used with cifar10 dataset"
assert not (args.nn_type == "fully_con" and args.dset != "mnist"), "FullyConNN must be used with mnist dataset"
assert args.epochs > 0, "Number of epochs must be positive"
assert args.neurons > 0, "Number of neurons must be positive"
assert args.batch_size > 0, "Batch size must be positive"

# Data loading - possibility of specifying "MNIST" and "CIFAR10" as well
if args.dset.lower() == "mnist":
    data = MNIST()
elif args.dset.lower() == "cifar10":
    data = CIFAR10()

# Load the training data
tr_data = data.loader(args.batch_size)

# Model selection
if args.nn_type == "fully_con":
    model = FullyConNN(neurons=args.neurons)
elif args.nn_type == "conv":
    model = ConNN(neurons=args.neurons)

optimizer = tf.keras.optimizers.Adam(learning_rate=5e-4)

# Training loop
step = 0
while step < args.epochs:
    for i, data_batch in enumerate(tr_data):
        losses = model.train(data_batch, optimizer)
    step += 1

# Testing and AUC calculation
pi_hat, y_hat = model.test(data.x_te)
auc = roc_auc_score(data.y_te, pi_hat)
print('final auc %0.4f' % (auc) )
