import tensorflow as tf

a = tf.Variable(tf.ones(shape=(1,3), dtype=tf.int32))

b = tf.constant(2)
x2_op = lambda a:a * b

r1 = x2_op(a * [1, 2, 3])
r2 = x2_op(a * [10, 20, 30])
tf.print(r1[0])
tf.print(r2[0])
