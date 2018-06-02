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

'''
一个网站域名，如"discuss.leetcode.com"，包含了多个子域名。作为顶级域名，常用的有"com"，下一级则有"leetcode.com"，最低的一级为"discuss.leetcode.com"。
当我们访问域名"discuss.leetcode.com"时，也同时访问了其父域名"leetcode.com"以及顶级域名 "com"。
给定一个带访问次数和域名的组合，要求分别计算每个域名被访问的次数。其格式为访问次数+空格+地址，例如："9001 discuss.leetcode.com"。
接下来会给出一组访问次数和域名组合的列表cpdomains 。要求解析出所有域名的访问次数，输出格式和输入格式相同，不限定先后顺序。
from collections import defaultdict		#可以指定一个工厂函数，来初始化键对应该的值，每次初始化一个键时，都会调用这一函数,如果指定int那么会初始化成0

示例 2
输入: 
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
输出: 
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
说明: 
按照假设，会访问"google.mail.com" 900次，"yahoo.com" 50次，"intel.mail.com" 1次，"wiki.org" 5次。
而对于父域名，会访问"mail.com" 900+1 = 901次，"com" 900 + 50 + 1 = 951次，和 "org" 5 次。


url_ls = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
dict_domain = defaultdict(int)
for i in url_ls:
	times , domian = i.split()
	times = int(times)
	dict_domain[domian]+=times

	while '.' in domian:
		domian = domian[domian.index('.')+1:]
		dict_domain[domian] += times
print([str(dic)+" "+v for v , dic in dict_domain.items()])
'''

'''
修剪二叉搜索树
给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。
输入: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

输出: 
      3
     / 
   2   
  /
 1
思路：
	首先判断当前节点的value与边界之间的关系。如果是空，则终止递归，直接返回空。如果节点的值小于L则返回节点的右子树，如果节点的值大于R则返回其右节点调用递归函数的值。
	如果节点的值小于L则返回其左节点调用递归函数的值。最后，如果节点的值在范围内则将左右节点调用递归函数的值赋值给其左右节点，并返回该节点。

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        if root.val>R:
            return self.trimBST(root.left,L,R)
        if root.val<L:
            return self.trimBST(root.right,L,R)
        root.left = self.trimBST(root.left,L,R)
        root.right = self.trimBST(root.right,L,R)
        return root
        '''
'''
你现在是棒球比赛记录员。
给定一个字符串列表，每个字符串可以是以下四种类型之一：
1.整数（一轮的得分）：直接表示您在本轮中获得的积分数。
2. "+"（一轮的得分）：表示本轮获得的得分是前两轮有效 回合得分的总和。
3. "D"（一轮的得分）：表示本轮获得的得分是前一轮有效 回合得分的两倍。
4. "C"（一个操作，这不是一个回合的分数）：表示您获得的最后一个有效 回合的分数是无效的，应该被移除。

每一轮的操作都是永久性的，可能会对前一轮和后一轮产生影响。
你需要返回你在所有回合中得分的总和。

ls = ["5","2","C","D","+"]
result = []
for i in ls:
	if i == 'C':
		result.pop()
	elif i == '+':
		result.append(result[-1]+result[-2])
	elif i == "D":
		result.append(2*result[-1])
	else:
		result.append(int(i))
sum_score =0
for j in result:
	sum_score+=j
print(sum_score)
'''

'''
两整数之和

不使用运算符 + 和-，计算两整数a 、b之和。
示例：
若 a = 1 ，b = 2，返回 3。

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a,b])
'''
'''
Excel表列序号
给定一个Excel表格中的列名称，返回其相应的列序号。
示例 1:
输入: "A"
输出: 1

示例 2:
输入: "AB"
输出: 28

示例 3:
输入: "ZY"
输出: 701

s = "ZY"
result = 0
for i in range(len(s)):
	result += (ord(s[i])-64)*26**(len(s)-i-1)
return result
'''
'''
罗马数字转整数
luoma = "IV"#任意一个罗马数字字符串
ls = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
result = 0
for i in ls.keys():
	while True:
		if i not in luoma:
			break
		if luoma.index(i)==0:
			result+=ls.get(i)
			luoma = luoma[1:]
		else:
			result+=ls.get(i)-ls.get(luoma[0])
			luoma = luoma[2:]
print(result)
'''


'''
#下一个更大元素 
给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。

nums1 = [3,1,5,7,9,2,6]
nums2 = [1,2,3,5,6,7,9,11]
result = []
for i in nums1:
	if nums2.index(i)==len(nums2)-1:
		result.append(-1)
	else:
		tag = True
		for j in nums2[nums2.index(i)+1:]:
			if j>i:
				result.append(j)
				tag = False
				break
		if tag:
			result.append(-1)
print(result)
'''


'''
# Fizz Buzz
写一个程序，输出从 1 到 n 数字的字符串表示。
1. 如果 n 是3的倍数，输出“Fizz”；
2. 如果 n 是5的倍数，输出“Buzz”；
3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result =[]
        for i in range(1,n+1):
            if i%3==0 and i%5!=0:
                result.append('Fizz')
            elif i%5==0 and i%3!=0:
                result.append("Buzz")
            elif i%3==0 and i%5==0:
                result.append("FizzBuzz")
            else:
                result.append(str(i))
        return result
'''


'''
#分糖果
给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。
输入: candies = [1,1,2,2,3,3]
输出: 3
解析: 一共有三种种类的糖果，每一种都有两个。
     最优分配方案：妹妹获得[1,2,3],弟弟也获得[1,2,3]。这样使妹妹获得糖果的种类数最多。

candies = [1,1,2,2,3,3]
all_cotegroy = set(candies)
if len(all_cotegroy)<=len(candies)//2:
	print(len(all_cotegroy))
else:
	print(len(candies)//2)

'''


'''
#写字符串需要的行数
我们要把给定的字符串 S 从左到右写到每一行上，每一行的最大宽度为100个单位，
如果我们在写某个字母的时候会使这行超过了100 个单位，那么我们应该把这个字母写到下一行。我们给定了一个数组 widths ，
这个数组 widths[0] 代表 'a' 需要的单位， widths[1] 代表 'b' 需要的单位，...， widths[25] 代表 'z' 需要的单位。

现在回答两个问题：至少多少行能放下S，以及最后一行使用的宽度是多少个单位？将你的答案作为长度为2的整数列表返回。
示例 2:
输入: 
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaa"
输出: [2, 4]
解释: 
除去字母'a'所有的字符都是相同的单位10，并且字符串 "bbbcccdddaa" 将会覆盖 9 * 10 + 2 * 4 = 98 个单位.
最后一个字母 'a' 将会被写到第二行，因为第一行只剩下2个单位了。
所以，这个答案是2行，第二行有4个单位宽度。

widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"
S = "bbbcccdddaaa"
my_dict =dict(zip(s,widths))
temp = 0
result = [1,0]
for i in S:
	if temp+my_dict[i] >100:
		result[0]+=1
		temp=0
	temp +=int(my_dict[i])
result[1]=temp
print(result)
'''
