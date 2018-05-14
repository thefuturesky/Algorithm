 # 选择排序

def sort(list1):
	for i in range(0,len(list1)-1):
		index = i
		print("123")
		for j in range(i+1,len(list1)):
			if list1[j]<list1[index]:
				list1[j],list1[index] = list1[index],list1[j]
		print("Round:",i,"result:",list1)
	
 		
list2 = [2,8,22,-8,69,117,11.2,-13.6]
print("Selected Sort:")
print("123")
sort(list2)