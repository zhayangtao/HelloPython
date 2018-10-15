# 多元线性回归
# 第一步：数据预处理
# 倒入库
import pandas as pd
import numpy as np

# 导入数据集
dataset = pd.read_csv('D:/machineLearning/50_Startups.csv')
print(dataset)
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values
print('X:', X)
print('Y:', Y)
# 将类别数据数字化
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()

# 躲避虚拟变量陷阱
X = X[:, 1:]

# 拆分数据集为训练集和测试集
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

#       第二步：在训练集上训练多元线性回归模型
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# 第三步：在测试集上预测结果
y_pred = regressor.predict(X=X_test)
