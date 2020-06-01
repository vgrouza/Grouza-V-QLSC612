# in the file myanalysis.py, I attempt to use some basic python functionality and hopefully
# agonizingly continue my transition away from matlab

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from scipy.stats import pearsonr
sns.set(style='white', font_scale=1.2)

# PART ONE: REPRODUCE PREVIOUS STUDY
# https://www3.nd.edu/~busiforc/handouts/Data%20and%20Stories/correlation/Brain%20Size/brainsize.html
# load provided data
data = pd.read_csv('practical/brainsize.csv', sep=';', index_col=0)
data = data.replace('.', np.nan)

# divide data by gender
group_by_gender = data.groupby('Gender')
data_male = group_by_gender.get_group('Male')
data_female = group_by_gender.get_group('Female')

# compute correlation coefficient between brain volume and FSIQ
corr_m, pval_m = pearsonr(data_male['FSIQ'], data_male['MRI_Count'])
corr_f, pval_f = pearsonr(data_female['FSIQ'], data_female['MRI_Count'])

# show output
print('PART ONE: CORRELATION OF FSIQ AND BRAIN SIZE')
print('Correlation in males:')
print('rho = %f' % corr_m)
print('p = %f \n' % pval_m)
print('Correlation in females:')
print('rho = %f' % corr_f)
print('p = %f \n' % pval_f)

# PART TWO: CORRELATE WITH NEW MEASURE
# introduce new variable
np.random.seed(3)
partY = np.random.normal(100, 10, len(data))
data['Reaction_Time'] = partY

# compute correlation with random noise
corr_2, pval_2 = spearmanr(data['FSIQ'], partY)

# show output
print('PART TWO: CORRELATION OF FSIQ AND REACTION TIME')
print('Reaction time, day one = %f +/- %f milliseconds.' % (partY.mean(), partY.std()))
print('rho = %f' % corr_2)
print('p = %f \n' % pval_2)

# make a plot
g = sns.JointGrid(data=data, x='FSIQ', y='Reaction_Time', xlim=(70, 150), ylim=(70, 130), height=5)
g = g.plot_joint(sns.regplot, color="xkcd:muted blue")
g = g.plot_marginals(sns.distplot, kde=False, bins=12, color="xkcd:bluey grey")
plt.tight_layout()
plt.show()

# now find another correlation with a second random variable
np.random.seed(17)
partY2 = np.random.normal(100, 10, len(data))
corr_3, pval_3 = spearmanr(data['FSIQ'], partY2)
print('Reaction time, day two = %f +/- %f milliseconds.' % (partY2.mean(), partY2.std()))
print('rho = %f' % corr_3)
print('p = %f \n' % pval_3)
