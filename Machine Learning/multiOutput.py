import numpy as np
import pandas as pd

# Pre-processing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, PolynomialFeatures

# Regressors
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor

# Load data from file
TimeConstraint = pd.read_csv("../Data/time_constraint.csv")
le = LabelEncoder()
TimeConstraint.topology = le.fit_transform(TimeConstraint.topology)
x = TimeConstraint.throughput
y = TimeConstraint.drop(['throughput'],axis=1)
x = np.array(x).reshape(-1,1)
x_train,x_test, y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=0)
clf = MultiOutputRegressor(RandomForestRegressor(random_state=0))
clf.fit(x,y)
print(clf.predict([[47817.84]]))
print(clf.score(x_test, y_test))

