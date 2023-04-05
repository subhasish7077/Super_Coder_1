# Bubble Sort
def bubbleSort(l):
	n = len(l)
	for i in range(n):
		for j in range(i+1, n):
			if l[i] > l[j]:
				l[i],l[j] = l[j], l[i]

l = [5, 1, 4, 2, 8]
bubbleSort(l)
print("Sorted array is:")
for i in l:
	print(i, end=" ")