import tensorflow as tf

a = tf.constant(1234)
b = tf.constant(5000)

add_op = a + b

tf.print(add_op)