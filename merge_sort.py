# 归并排序

def merge_sort(list1):
	length = len(list1)
	if length == 1 :
		return list1

	mid = length // 2
	left = list1[:mid]
	right = list1[mid:]

	left1 = merge_sort(left)
	right1 = merge_sort(right)

	return merge(left1,right1)

def merge(left1,right1):
	result = []

	while len(left1)>0 and len(right1)>0:
		if left1[0] <= right1[0]:
			result.append(left1.pop(0))
		else:
			result.append(right1.pop(0))
	result += left1
	result +=right1

	return result

if __name__ == "__main__":

	list1 = [7,22,-11,58,105,3,-22,0,55,14,78,22]
	list2 = merge_sort(list1)
	print(list2)

'''
def merge_sort(li):
	length = len(li)

	if length == 1:
		return li

	mid = length // 2

	left = li[:mid]
	right = li[mid:]

	li1 = merge_sort(left)
	li2 = merge_sort(right)

	return merge(li1,li2)

def merge(li1,li2):
	result = []

	while len(li1)>0 and len(li2)>0:
		if li1[0] <= li2[0]:
			result.append(li1.pop(0))
		else:
			result.append(li2.pop(0))
	result += li1
	result += li2
	return result
'''