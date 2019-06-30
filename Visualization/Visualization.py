#!/usr/bin/env python
# coding: utf-8

# In[105]:
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import ElasticNet, LassoLars, Ridge, LinearRegression, Lasso



# In[106]:
# Load data from path
TimeConstraint1 = pd.read_csv("data/time_constraint.csv")
TimeConstraint = pd.read_csv("../SynData/data/GeneratedData.csv")
D_rt_none = pd.read_pickle("data/170408-2141-rt-none.pkl")
D_rt_nginx = pd.read_pickle("data/170408-2154-rt-nginxlb.pkl")
D_rt_socat = pd.read_pickle("data/170408-2206-rt-socat.pkl")
D_rt_redir = pd.read_pickle("data/170408-2232-rt-squid.pkl")
D_rt_nginx_socat_redir = pd.read_pickle("data/170409-0718-rt-nginxlb-socat-squid.pkl")
D_rt_socat_redir_nginx = pd.read_pickle("data/170409-1606-rt-socat-squid-nginxlb.pkl")
D_rt_redir_nginx_socat = pd.read_pickle("data/170410-0054-rt-squid-nginxlb-socat.pkl")


# In[107]:


def main():
    print("NFV Data Visualization")
    print(TimeConstraint.head())
    print("Info")
    print(TimeConstraint.info())
    print("Describe")
    print(TimeConstraint.describe())
    f, ax = plt.subplots(3, figsize=(12,18))
    TimeConstraint.drop('id', axis=1)
    #sns.distplot(TimeConstraint.CPU, color='c', ax=ax[1])
    #sns.distplot(TimeConstraint.throughput, color='c', ax=ax[2])
    plt.plot(TimeConstraint.CPU, TimeConstraint.throughput)
    plt.show()
    le = LabelEncoder()
    #TimeConstraint.topology = le.fit_transform(TimeConstraint.topology)
    TimeConstraint.info()

    x = TimeConstraint.drop('throughput_kbyte_per_second',axis=1)
    y = TimeConstraint.throughput_kbyte_per_second

    x_train,x_, y_train,y_ = train_test_split(x,y,test_size=0.15,random_state=25)
    x_dev,x_test,y_dev,y_test = train_test_split(x_,y_,test_size=0.5,random_state=25)

    sc = StandardScaler()
    sc.fit(x_train)
    sc.transform(x_train)
    sc.transform(x_dev)

    clf = LinearRegression()
    clf.fit(x_train,y_train)
    print('Training score: {:0.3f}'.format(r2_score(y_train,clf.predict(x_train))))
    print('Training MSE: {:0.3f}'.format(mean_squared_error(y_train,clf.predict(x_train))))
    print('Dev set score: {:0.3f}'.format(r2_score(y_dev,clf.predict(x_dev))))
    print('Dev set MSE: {:0.3f}'.format(mean_squared_error(y_dev,clf.predict(x_dev))))
    print('Coefficients: {}\n Intercept: {}'.format(clf.coef_,clf.intercept_))

    clf = ElasticNet(alpha=1)
    clf.fit(x_train,y_train)
    print('Training score: {:0.3f}'.format(r2_score(y_train,clf.predict(x_train))))
    print('Training MSE: {:0.3f}'.format(mean_squared_error(y_train,clf.predict(x_train))))
    print('Dev set score: {:0.3f}'.format(r2_score(y_dev,clf.predict(x_dev))))
    print('Dev set MSE: {:0.3f}'.format(mean_squared_error(y_dev,clf.predict(x_dev))))
    print('Coefficients: {}\n Intercept: {}'.format(clf.coef_,clf.intercept_))

    clf = Ridge(alpha=10)
    clf.fit(x_train,y_train)
    print('Training score: {:0.3f}'.format(r2_score(y_train,clf.predict(x_train))))
    print('Training MSE: {:0.3f}'.format(mean_squared_error(y_train,clf.predict(x_train))))
    print('Dev set score: {:0.3f}'.format(r2_score(y_dev,clf.predict(x_dev))))
    print('Dev set MSE: {:0.3f}'.format(mean_squared_error(y_dev,clf.predict(x_dev))))
    print('Coefficients: {}\n Intercept: {}'.format(clf.coef_,clf.intercept_))

    clf = LassoLars(alpha=1)
    clf.fit(x_train,y_train)
    print('Training score: {:0.3f}'.format(r2_score(y_train,clf.predict(x_train))))
    print('Training MSE: {:0.3f}'.format(mean_squared_error(y_train,clf.predict(x_train))))
    print('Dev set score: {:0.3f}'.format(r2_score(y_dev,clf.predict(x_dev))))
    print('Dev set MSE: {:0.3f}'.format(mean_squared_error(y_dev,clf.predict(x_dev))))
    print('Coefficients: {}\n Intercept: {}'.format(clf.coef_,clf.intercept_))

def Data():
    D_rt_nginx = pd.read_pickle("data/170408-2154-rt-nginxlb.pkl")
    print(D_rt_nginx.info())
    print(D_rt_nginx.describe())

# In[109]:
main()
Data()



