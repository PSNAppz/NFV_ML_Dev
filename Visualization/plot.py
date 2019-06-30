import matplotlib.pyplot as plt
from mlxtend.plotting import plot_linear_regression
import pandas as pd
import seaborn as sns

TimeConstraint = pd.read_csv("data/GeneratedData.csv")

sns.regplot(x=TimeConstraint.throughput, y=TimeConstraint.CPU, data=TimeConstraint)

plt.show()
