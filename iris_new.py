f = open("Iris.csv")
file = f.read()

sp = file.split('\n')[1:-1]

labels_list=[]

n_cols = len(sp[0].split(','))

for s in sp:
	t = s.split(',')
	if t[-1] not in labels_list:
		labels_list.append(t[-1])

previous_columns = file.split('\n')[0]
previous_columns = previous_columns.split(',')[0:-1]

new_labels = previous_columns + labels_list

new_labels = ','.join(new_labels)

sp1 = []

new_file = open("new_iris.csv", "w")
new_file.write(new_labels + '\n')

for s in sp:
	t = s.split(',')
	new_file.write(','.join(t[:-1]))
	for l in labels_list:
		if t[-1] == l:
			new_file.write(',1')
		else:
			new_file.write(',0')
	new_file.write('\n')
