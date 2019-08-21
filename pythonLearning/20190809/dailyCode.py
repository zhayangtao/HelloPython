import tensorflow as tf

x = tf.placeholder(tf.float32, shape=(1, 2))
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

# 定义前向传播
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 用会话计算过程
with tf.Session() as  sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    print("y is:\n", sess.run(y, feed_dict={x: [[0.7, 0.5]]}))
