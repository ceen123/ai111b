import matplotlib . pyplot as plt
import numpy as np
import random

# x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
# y = np.array([2, 3, 4, 5, 6], dtype=np.float32)
x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
y = np.array([1.9, 3.1, 3.9, 5.0, 6.2], dtype=np.float32)

def predict(a, xt):
	return a[0]+a[1]*xt

def MSE(a, x, y):
	total = 0
	for i in range(len(x)):
		total += (y[i]-predict(a, x[i]))**2
	return total

def loss(p):
	return MSE(p, x, y)

# p = [0.0, 0.0]
# plearn = optimize(loss, p, max_loops=3000, dump_period=1)
def optimize(P):
	# Please modify this function to automatically find the p that minimizes the loss

	failCount = 0
	while (failCount < 10000):
		dx=random.uniform(-0.1, 0.1)
		dy=random.uniform(-0.1,0.1)

		Pcount = [P[0]+dx, P[1]+dy]

		if loss(P)<loss(Pcount):
			failCount += 1
		else :
			P = Pcount
			failCount = 0

	return P

P = [0, 0]
p = optimize(P)

# Plot the graph
y_predicted = list(map(lambda t: p[0]+p[1]*t, x))
print('y_predicted=', y_predicted)
plt.plot(x, y, 'ro', label='Original data')
plt.plot(x, y_predicted, label='Fitted line')
plt . legend()
plt.show()