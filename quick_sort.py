#快速排序
# def quick_sort(arr):
# 	if len(arr) > 1:
# 		qsort(arr,0,len(arr)-1)

# def qsort(arr,start,end):
# 	base = arr[start]
# 	pl = start
# 	pr = end

# 	while pl<pr:
# 		while pl <pr and arr[pr] >= base :
# 			pr -=1
# 		if pl == pr:
# 			break
# 		else: 
# 			arr[pr],base = base,arr[pr]


# 		while pl < pr and arr[pl] <= base:
# 			pl+=1
# 		if pl == pr:
# 			break
# 		else:
# 			arr[pl],base = base , arr[pl]

# 	if pl - 1 >start:
# 		qsort(arr,start,pl-1)
# 	if pr + 1 <end:
# 		qsort(arr,pr + 1,end)

def qsort(arr):
	if len(arr)>1:
		quick_sort(arr,0,len(arr)-1)
def quick_sort(array, left, right):  
    if left >= right:  
        return  
    i = left  
    j = right  
    key = array[i]  
    while i < j:  
        while i < j and array[j] > key:  
            j -= 1  
        array[i] = array[j]  
        while i < j and array[i] <= key:  
            i += 1  
        array[j] = array[i]  
    array[i] = key  
    quick_sort(array, left, i - 1)  
    quick_sort(array, i + 1, right)


from random import Random
r = Random()
a=[]

for i in range(20):
	a.append(r.randint(0,1000))

print(a)
qsort(a)
print(a)