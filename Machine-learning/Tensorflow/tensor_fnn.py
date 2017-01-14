import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as ip


mnist = ip.read_data_sets("MNIST_data/",one_hot = True)
X = tf.placeholder(tf.float32, [None, 784])
# 28*28 size gray scale image hence 28,28,1 otherwiese 28,28,3
W = tf.Variable(tf.zeros([784,10])) #10 Neurons for first layer
#W are the weights to learn, hence hence variable
b = tf.Variable(tf.zeros([10]))
init = tf.global_variables_initializer()
Y = tf.nn.softmax(tf.matmul(X,W)+b)
Y_ = tf.placeholder(tf.float32,[None,10])
cross_entropy = -tf.reduce_sum(Y_*tf.log(Y))
is_correct = tf.equal(tf.argmax(Y,1), tf.argmax(Y_,1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
optimizer = tf.train.GradientDescentOptimizer(0.003)
train_step = optimizer.minimize(cross_entropy)
sess = tf.Session()
sess.run(init)
for i in range(1000):
    batch_X,batch_Y = mnist.train.next_batch(100)
    train_data = {X:batch_X, Y_:batch_Y}
    sess.run(train_step,feed_dict = train_data)
    a,c = sess.run([accuracy, cross_entropy], feed_dict = train_data)
    print a,c
test_data = {X:mnist.test.images, Y_:mnist.test.labels}
a,c = sess.run([accuracy, cross_entropy], feed_dict = test_data)
print "Accuracy"
print a,c
