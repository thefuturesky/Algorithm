#冒泡排序

def bubble_sort(list1):

	length = len(list1)

	for i in range(length):
		for j in range(length-i-1):
			if list1[j]>list1[j+1]:
				list1[j],list1[j+1] = list1[j+1],list1[j]
	return list1

#冒泡算法的改进
# def bubble_sort(list1):
# 	length = len(list1)
# 	found = False
# 	for i in range(length):
# 		for j in range(length-i-1):
# 			if list1[j]>list1[j+1]:
# 				list1[j],list1[j+1] = list1[j+1],list1[j]
# 				found = True
# 		if not found:
# 			break

if __name__ == "__main__":

	list1 = [1,8,56,114,23,-14,-69,25,86,3,5]
	list2 = bubble_sort(list1)
	print(list2)
