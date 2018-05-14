#希尔排序
def shell_sort(list1):
	m = len(list1)
	gap = m//2
	while gap>0:
		print(gap)
		'''
		列表中的list[i]，按间隔gap从列表中取元素list[i+1],list[i+1+gap],list[i+1+2gap]...与list[i]比较 
                  选择小的与list[i]交换
		'''
		for i in range(m):
			index=i
			j=i+1
			while j<m:
				if list1[j]<list1[index]:
					index=j
				j +=gap
			if index != j :  #若有元素比list[i]小，交换
				list1[index],list1[i] = list1[i],list1[index]
			print(list1)
		gap = gap // 2

	return list1

if __name__== '__main__':  
    list_0 = [4,1,9,13,34,26,10,7,4,3]  
    list_1 = shell_sort(list_0)


# def shell_sort(lsit2):
# 	m = len(list2)
# 	gap = m//2

# 	while gap >0:

# 		for i in range(m):

# 			index = i
# 			j = i+1
# 			while j<m:
# 				if list2[j]<list2[index]:
# 					index=j
# 				j += gap

# 			if index != i :
# 					list2[i],lsit2[index] = list2[index],list2[i]
# 		gap = gap//2

# 	return lsit2