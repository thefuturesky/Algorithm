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


'''
#二叉树的层平均值
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

示例 1:

输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        if root == None:
            return result
        q = [root]
        while q:
            sum = 0
            len = 0
            q1 = []
            while q:
                temp = q.pop()
                if temp.left:
                    q1.append(temp.left)
                if temp.right:
                    q1.append(temp.right)
                sum+=temp.val
                len+=1
            result.append(sum*1.0/len)
            q = list(q1)
        return result
'''


'''
#托普利茨矩阵
如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是托普利茨矩阵。
给定一个 M x N 的矩阵，当且仅当它是托普利茨矩阵时返回 True。
示例 1:

输入: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
输出: True
解释:
1234
5123
9512
在上面这个矩阵中, 对角线分别是 "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]",

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        x = len(matrix)
        y = len(matrix[0])
        tag = True
        for i in range(x):
            for j in range(y):
                try:
                    if matrix[i+1][j+1]!=matrix[i][j]:
                        tag = False
                except IndexError:
                    pass
        return tag
'''


'''
#最大连续1的个数
给定一个二进制数组， 计算其中最大连续1的个数。
示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        temp =0
        for i in nums:
            if i ==1:
                temp+=1
            else:
                if temp>result:
                    result = temp
                temp = 0
        if temp>result:
            result = temp
        return result
'''


'''
#杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        result = [[1],[1,1]]
        temp = []
        for j in range(2,numRows):
            for i in range(j+1):
                if i==0 or i==j:
                    temp.append(1)
                else:
                    temp.append(result[j-1][i]+result[j-1][i-1])
            result.append(temp)
            temp=[]
        return result
'''


'''
#移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        le = len(nums)
        while i<le:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                le-=1
                continue
            i+=1
        print(nums)
'''


'''
#只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,1]
输出: 1

示例 2:
输入: [4,1,2,1,2]
输出: 4
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        while True:
            if i == len(nums)-1:
                break
            if nums[i]!=nums[i+1]:
                break
            i+=2
        return nums[i]
'''


'''
#检测大写字母
给定一个单词，你需要判断单词的大写使用是否正确。
我们定义，在以下情况时，单词的大写用法是正确的：
全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。

示例 1:
输入: "USA"
输出: True

示例 2:
输入: "FlaG"
输出: False

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if 65<=ord(word[0])<=90:
            if word[1:]==word[1:].lower():
                return True
            elif word[1:]==word[1:].upper():
                return True
            else:
                return False
        elif word.lower() == word:
            return True
        else:
            return False
'''


'''
#杨辉三角 II
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

示例:
输入: 3
输出: [1,3,3,1]

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        result = [[1],[1,1]]
        temp = []
        for j in range(2,rowIndex+1):
            for i in range(j+1):
                if i==0 or i==j:
                    temp.append(1)
                else:
                    temp.append(result[j-1][i]+result[j-1][i-1])
            result.append(temp)
            temp=[]
        return result[rowIndex]
'''


'''
#岛屿的最大面积
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 
的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)
示例 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

class Solution:
    def dfs(self,ls,x0,y0):
            ls[x0][y0] = 0
            s = 1
            n =len(ls)
            m = len(ls[0])
            dire = [[0,1],[0,-1],[1,0],[-1,0]]
            for i in range(4):
                x = x0 + dire[i][0]
                y = y0 + dire[i][1]
                try:
                    if x>=0 and x<=n and y>=0 and y<=m and ls[x][y]==1:
                        s += self.dfs(ls,x,y)
                except IndexError :
                    pass
            return s
        
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        mx = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    mx = max(mx,self.dfs(grid,i,j))
        return mx
'''


'''
#相同的树
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.myfun([],p) == self.myfun([],q)
        
    def myfun(self,result , tree):
        if tree == None:
            return
        result.append(tree.val)
        if tree.left==None and tree.right!=None:
            result.append(None)
        self.myfun(result,tree.left)
        self.myfun(result,tree.right)
        return result
'''


'''
#山羊拉丁文
class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        ls = S.split(' ')
        length = len(ls)
        result = ''
        container = ['a','e','i','o','u','A','E','I','O','U']

        for i in range(length):
            if ls[i][0] in container:
                result += ls[i]+'ma'+'a'*(i+1)+' '
            else:
                ls[i]=ls[i][1:]+ls[i][0]
                result +=ls[i]+"ma"+"a"*(i+1)+' '
        result = result.strip()
        return result
'''


'''
#合并两个有序链表
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

#递归求解
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        result = None
        if l1.val>l2.val:
            result = l2
            result.next = self.mergeTwoLists(l1,l2.next)
        else:
            result = l1
            result.next = self.mergeTwoLists(l1.next,l2)
        return result

#非递归求解
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        head = ListNode(0)
        current = head
        while l1 and l2:
            if l1.val > l2.val:
                current.next = l2
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1.next
            current = current.next
        if l1:
            current.next = l1
        else:
            current.next = l2
        return head.next
'''


'''
#求众数
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在众数。

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)/2
        set_temp = set(nums)
        result = 0
        for i in set_temp:
            if nums.count(i)>length:
                result = i
        return result
'''


'''
#区域和检索 - 数组不可变
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
示例：
给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._nums = nums
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self._nums[i:j+1])
'''

'''
#找不同
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ls = list(t)
        for i in s:
            ls.remove(i)
        return ls[0]
'''


'''
#二叉树的层次遍历 II
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root == None:
            return result
        stack = [root]
        while stack:
            temp =[]
            for i in range(len(stack)):
                current = stack.pop(0)
                temp.append(current.val)
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)
            result.append(temp)
        result.reverse()
        return result
'''


'''
#移除元素
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

使用while 循环，删除元素的时候i不加。
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        while i<len(nums):
            if nums[i]==val:
                nums.remove(val)
            else:
                i+=1
        return len(nums)
'''


'''
#员工的重要性
示例 1:
输入: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
输出: 11
解释:
员工1自身的重要度是5，他有两个直系下属2和3，而且2和3的重要度均为3。因此员工1的总重要度是 5 + 3 + 3 = 11。
"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        for employee in employees:
            if employee.id == id:
                result = employee.importance
                if not employee.subordinates:
                    return result
                for index in employee.subordinates:
                    result+=self.getImportance(employees,index)
                return result
'''


'''
#根据二叉树创建字符串
你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。
空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。
示例 1:
输入: 二叉树: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     
输出: "1(2(4))(3)"
解释: 原本将是“1(2(4)())(3())”，
在你省略所有不必要的空括号对之后，
它将是“1(2(4))(3)”。

class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        result = ""
        if t == None:
            return ""
        result += str(t.val)
        if t.right==None and t.left!=None:
            result += "("+self.tree2str(t.left)+")"
        elif t.left==None and t.right!=None:
            result += "()"+"("+self.tree2str(t.right)+")"
        elif t.left!=None and t.right!=None:
            result += "("+self.tree2str(t.left)+")"
            result += "("+self.tree2str(t.right)+")"
        
        return result
'''


'''
#两个数组的交集
给定两个数组，写一个函数来计算它们的交集。
例子:
给定 num1= [1, 2, 2, 1], nums2 = [2, 2], 返回 [2].
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums1:
            if i in nums2 and i not in result:
                result.append(i)
        return result
'''


'''
#报数
报数序列是指一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        if n==1:
            return "1"
        if n==2:
            return "11"
        res = "11"
        for i in range(2,n):
            tep = ""
            count = 1
            for j in range(1,len(res)):
                if res[j-1]==res[j]:
                    count+=1
                else:
                    tep +=str(count)+res[j-1]
                    count=1
            tep += str(count)+res[j]
            res = tep
        return res
'''


'''
#计数二进制子串
class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: strs
        :rtype: int
        """
        L = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split(' ')))  
        return sum(min(a,b) for a,b in zip(L, L[1:]) )
'''
<<<<<<< HEAD


'''
#相对名次
class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        length = len(nums)
        dic_1 = dict(zip([i for i in range(length)],nums))
        nums = sorted(nums)[::-1]
        for i in range(3,length):
            medal.append(str(i+1))
        dic_2 = dict(zip(nums,medal))
        for key,value in dic_1.items():
            dic_1[key] = dic_2[value]
        result=[]
        for value in dic_1.values():
            result.append(value)
        return result
'''

