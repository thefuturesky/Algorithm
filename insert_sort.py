#插入排序

def insert_sort(list1):
	count = len(list1)
	for i in range(1,count):
		key = list1[i]
		j=i
		while j>0 and list1[j-1]>key :
			list1[j]=list1[j-1]
			j -= 1
		list1[j] = key
		print("Round:",i,"result:",list1)

list1 = [2,8,22,-8,69,117,11.2,-13.6,3]
print("Selected Sort:")
insert_sort(list1)
