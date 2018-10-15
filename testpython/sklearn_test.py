from sklearn import datasets


iris = datasets.load_iris() # 导入数据集
X = iris.data # 获取特征向量
Y = iris.target # 获取样本 label

# 创建数据集
from sklearn.datasets.samples_generator import make_classification
X, Y = make_classification(n_samples=6, n_features=5, n_informative=2,
                           n_redundant=2, n_classes=2, n_clusters_per_class=2,
                           scale=1.0, random_state=20)
for x_,y_ in zip(X, Y):
    print(y_, end=': ')
    print(x_)

# 数据预处理
from sklearn import preprocessing

data = [[0, 0], [0, 0], [1, 1], [1, 1]]
# 基于 mean 和 std 的标注化
scaler = preprocessing.StandardScaler()
# scaler.transform(tra)
X = [[ 1., -1.,  2.],
     [ 2.,  0.,  0.],
     [ 0.,  1., -1.]]
x_normalized = preprocessing.normalize(X, norm='l2')
print(x_normalized)