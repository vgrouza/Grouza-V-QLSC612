# initial start
import pandas as pd
import numpy as np

data = pd.read_csv('practical/brainsize.csv', delimiter=';')
data = data.replace('.', np.nan)


