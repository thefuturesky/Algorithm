# 朴素匹配字符串

def naive_matching(t,p):   #p为主字符串
	m,n=len(t),len(p)
	i,j = 0,0

	while i<m and j<n:
		if t[i] == p[j]:
			i,j=i+1,j+1
		else:
			i,j=0,j-i+1
	if i==m:
		return j-i
	else:
		return -1

