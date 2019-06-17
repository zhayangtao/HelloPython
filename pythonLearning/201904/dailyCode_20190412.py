import numpy as np
import matplotlib.pylab as plt

x = np.array([1.0, 2.0, 3.0])
print(x)
y = np.array([2.0, 4.0, 6.0])
print(x + y)

z = np.array([[1, 2, 3], [2, 4, 5]])
print(z.shape)

for row in z:
    print(row)

x = z.flatten()
print(x)

print(z > 2)
print(z[z > 2])

# 生成数据
x = np.arange(0, 6, 0.1)
y = np.sin(x)
# 绘制图形
# plt.plot(x, y)
# plt.show()

y1 = np.sin(x)
y2 = np.cos(x)
#
plt.plot(x, y1, label='sin')
plt.plot(x, y2, label='cos')  # 虚线绘制
plt.xlabel("x")
plt.ylabel('y')
plt.title('sin & cos')
plt.legend()
plt.show()

# 显示图像
from matplotlib.image import imread

img = imread("C:/Users/FC/Desktop/justinBieber/2455940031.jpg")
plt.imshow(img)
plt.show()


