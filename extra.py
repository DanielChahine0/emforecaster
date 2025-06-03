import os
from scipy.io import loadmat

path = "emforecaster/data/forecasting/rf_emf/LongTerm17.mat"
print(os.path.exists(path))  # Should print: True

data = loadmat(path)
print(data.keys())  # See contents
