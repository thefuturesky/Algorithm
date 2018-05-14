 # 选择排序

def select_sort(lists):
	count = len(lists)
	for i in range(0,count-1):
		min = i
		for j in range(i+1,count):
			if lists[j]<lists[min]:
				lists[j],lists[min] = lists[min],lists[j]
		print("Round:",i+1,"result:",lists)
	
 		
list1 = [2,8,22,-8,69,117,11.2,-13.6,3]
print("Selected Sort:")
select_sort(list1)