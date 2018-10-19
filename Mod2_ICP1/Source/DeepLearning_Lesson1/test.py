import tensorflow as tf

a = tf.add("sneha","suyash")
sess = tf.Session()
print(sess.run(a))
print(a)

a = tf.add(5,3)
print(a)
print(sess.run(a))
sess.close()

with tf.Session() as ses1:
    print(ses1.run(a))

x=3
y=2
add = tf.add(x,y)
mul = tf.multiply(x,y)
op3 = tf.pow(add,mul)

with tf.Session() as ses:
    print(ses.run(op3))