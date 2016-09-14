import numpy as np
import matplotlib.pyplot as plt

N = 50
x = range(1,501)
y1 = []
y2 = []
y3 = []

# with open('./results/cluttered_mnist_cnn_3x3.dat','r') as f:
# 	for line in f:
# 		line = line.strip()
# 		y1.append(float(line))

# with open('./results/cluttered_mnist_cnn_5x5.dat','r') as f:
# 	for line in f:
# 		line = line.strip()
# 		y2.append(float(line))

# with open('./results/cluttered_mnist_stn.dat','r') as f:
# 	for line in f:
# 		line = line.strip().split(',')
# 		y3.append(float(line[1]))
with open('./results/svhn_cnn.dat','r') as f:
	for line in f:
		line = line.strip()
		y1.append(float(line))

# with open('./results/cnn_stn_variant1.dat','r') as f:
# 	for line in f:
# 		line = line.strip().split(',')
# 		y2.append(float(line[1]))

# with open('./results/cnn_stn_variant2.dat','r') as f:
# 	for line in f:
# 		line = line.strip().split(',')
# 		y3.append(float(line[1]))

plt.plot(x, y1, label='CNN',color='green',linewidth=2)

plt.title('Performance of CNN model on SVHN data')
plt.ylabel('Training accuracy')
plt.xlabel('Number of epochs')
plt.legend(loc=4)
plt.show()