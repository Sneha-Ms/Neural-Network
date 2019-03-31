import random

weights = []

DIM = [4, 5, 3]

for i in range(DIM[0]):
	weights.append([])
	for j in range(DIM[1]):
		weights[-1].append([])
		for k in range(DIM[2]):
			weights[-1][-1].append(random.random())

# net = []

