from sklearn.datasets import load_iris
from sklearn.preprocessing import scale
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Keeping the Raw Data
rawData = load_iris()

data = scale(rawData.data)
# Entries
X = rawData.data[:, :3]
# Loading the Target
y = rawData.target

print(X)
print(y)
