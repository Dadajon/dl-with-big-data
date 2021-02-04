import tensorflow as tf

a = tf.constant(120, name='a')
b = tf.constant(130, name='b')
c = tf.constant(140, name='c')

v = tf.Variable(0, name='v')

calc_op = a + b + c
v.assign(calc_op)

tf.print(v)
