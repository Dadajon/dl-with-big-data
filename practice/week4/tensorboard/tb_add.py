import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

a = tf.constant(100, name='a')
b = tf.constant(200, name='b')
c = tf.constant(300, name='c')
v = tf.Variable(0, name='v')

calc_op = a + b * c
assign_op = tf.assign(v, calc_op)

sess = tf.Session()

tw = tf.summary.FileWriter('log_dir', graph=sess.graph)

sess.run(assign_op)
print(sess.run(v))
