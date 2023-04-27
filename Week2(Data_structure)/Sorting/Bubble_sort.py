# Bubble Sort
def bubbleSort(l):
	n = len(l) 
	for i in range(n):
		for j in range(0, n):
			if l[i] < l[j]:
				l[i],l[j] = l[j], l[i] 
l = [5,7,30,2,10,8]
bubbleSort(l)
print("Sorted array is:")
for i in l:
	print(i, end=" ")