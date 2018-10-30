from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD


model = Sequential()

model.add(Dense(units=64, input_dim=100))
model.add(Activation("relu")) # 激活函数
model.add(Dense(units=10))
model.add(Activation("softmax"))

# 使用 compile 编译模型
# 编译模型时必须指明损失函数和优化器，
model.compile(loss='categorical_crossentropy',
              optimizer=SGD(lr=0.01, momentum=0.9, nesterov=True), metrics=['accuracy'])

# 完成模型编译后，我们在训练数据上按batch进行一定次数的迭代来训练网络
model.fit()