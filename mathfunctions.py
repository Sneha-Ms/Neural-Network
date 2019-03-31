e = 2.71828

def tanh(x):
	a = (e**(2*x)-1)/(e**(2*x)+1)
	return a

def sigmoid(x):
	a = (e**x)/(e**x + 1)
	return a

def dtanh(x):
	a = 1-(tanh(x))**2
	return a

def dsigmoid(x):
	a = sigmoid(x)*(1-sigmoid(x))
	return a

def mse(a,b):
	r = 0
	for i in range(len(a)):
		r = r + (a[i]-b[i])**2
	return r/len(a)

# print(sigmoid(0))