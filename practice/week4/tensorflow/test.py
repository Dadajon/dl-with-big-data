import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf

a = tf.constant(100)
b = tf.constant(50)
add_op = a + b

v = tf.Variable(0)
v.assign(add_op)

tf.print(v)
