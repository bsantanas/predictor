import json

with open('items.json') as data_file:
	data = json.load(data_file)
	# First five numbers from each of the entries in the file
	numbers = [list(map(int,c['numbers'][:5])) for c in data]

def c():
	L = []
	for i in range(1,67):
		for j in range (2,68):
			if j <= i:
				continue
			for k in range (3,69):
				if k <= j:
					continue
				for l in range (4,70):
					if l <= k:
						continue
					L.append([i,j,k,l])
	return L

def contains(l1,l2):
	return all(c in l2 for c in l1)

def remap_keys(mapping):
    return [{'key':k, 'value': v} for k, v in mapping.items()]

def iterate():
	L = {}
	comb = c()
	for i in range(len(data)):
		print( i/len(data))
		for j in range(len(comb)):
			l1 = comb[j]
			l2= numbers[i]
			if contains(l1,l2):
				x = tuple(l1)
				if x not in L:
					L[x] = 1
				else:
					L[x] += 1
	return L