import tensorflow as tf

x = tf.constant([[1., 2.]])
neg_op = tf.negative(x)

print('tensorflow version', tf.__version__)

