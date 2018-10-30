# 函数式（Functional）模型
# 第一个模型：全连接网络
from keras.layers import Input, Dense
from keras.models import Model

inputs = Input(shape=(784, ))
x = Dense(64, activation='relu')(inputs)
x = Dense(64, activation='relu')(x)
predictions = Dense(10, activation='softmax')(x)

model = Model(inputs=inputs, outputs=predictions)
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
# model.fit(data, labels)

"%s" % "d"
"{}".format(1)
person = {'name': 'Eric', 'age': 74}
print("Hello, {name}. You are {age}.".format(name=person['name'], age=person['age']))
print("Hello, {name}. You are {age}.".format(**person))

name = "Eric"
age = 44
print(f"Hello, {name}. you are {age}")
print(F"Hello, {name}. you are {age}")
print(f"{2 * 22}")
print(f"{name.lower()} is fun")

# 多行 f-string
message = (f"Hi {name}."
           f"you are a {person}")