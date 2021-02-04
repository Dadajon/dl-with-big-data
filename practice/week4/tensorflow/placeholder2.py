import tensorflow as tf

a = tf.Variable(tf.ones(shape=(), dtype=tf.int32))

b = tf.constant(10)
x10_op = lambda a:a * b

r1 = x10_op(a*[1, 2, 3, 4, 5])
tf.print(r1)
r2 = x10_op(a*[10, 20])
tf.print(r2)
