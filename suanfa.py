#键盘行
'''
q = 'qwertyuiopQWERTYUIOP'
a = 'asdfghjklASDFGHJKL'
z = 'zxcvbnmZXCVBNM'
words = ["Hello", "Alaska", "Dad", "Peace"]
result = []
for i in words:
	if i[0] in q:
		for j in i:
			if j not in q:
				break
		if j == i[-1]:
			result.append(i)
	elif i[0] in a:
		for j in i:
			if j not in a:
				break
		if j == i[-1]:
			result.append(i)
	else :
		for j in i:
			if j not in z:
				break
		if j == i[-1]:
			result.append(i)
print(result)
'''
'''
#反转字符串
words = "Let's take LeetCode contest"
result = ''
for word in words.split():
	word = word[::-1]
	result+=word+' '
print(result[:-1])
'''
'''
num = 4
binary = ""
while num!=0:
	binary+=str(num%2)
	num//=2
binary = binary[::-1]
tag = False
print(binary)
for i in range(len(binary)-1):
	if binary[i] =="1":
		if binary[i+1]!="0":
			tag = True
	else:
		if binary[i+1]!="1":
			tag = True
print(tag)
'''
'''
#数组的拆分
#给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 
#例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。
ls = [1,4,3,2]
ls.sort()
result = 0
bs = [i for i in range(len(ls)) if i%2==0]
for j in bs:
	result+=ls[j]
print(result)
'''
'''
岛屿的周长
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

y_len = len(grid)
x_len = len(grid[0])
islands_len = 0

def count(x,y,arr):
	if (-1<x<x_len) and (-1<y<y_len):
		return 1 if (arr[x][y]==0) else 0
	return 1

if __name__ == "__main__":
	for x in range(x_len):
		for y in range(y_len):
			if grid[x][y]==1:
				for index in range(4):
					islands_len+= count(x+dx[index],y+dy[index],grid)
	print(islands_len)
'''
'''
#字符最短距离
S = "loveleetcode"
C = 'e'
temp = []
for i in range(len(S)):
	if S[i]==C:
		temp.append(i)
result = []
key=0
for j in range(len(S)):
	if j<temp[key]:
		if key == 0:
			result.append(temp[key]-j)
		else:
			result.append(min(j-temp[key-1],temp[key]-j))
	elif temp[key]<j:
		if key+1<=len(temp)-1:
			result.append(min(j-temp[key],temp[key+1]-j))
		else:
			result.append(j-temp[key])
	elif j in temp:
		result.append(0)
		if key+1<=len(temp)-1:
			key+=1
print(result)
'''