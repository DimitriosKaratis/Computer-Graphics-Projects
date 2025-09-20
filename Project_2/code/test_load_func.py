import numpy as np

# This script loads a NumPy file and prints the keys and types of the data it contains.
def test_load():
    data = np.load("hw2.npy", allow_pickle=True).item()

    print("Available keys in hw2.npy:")
    print(data.keys())

    for key in data:
        print(f"{key}: type={type(data[key])}, shape={np.shape(data[key])}")


test_load()