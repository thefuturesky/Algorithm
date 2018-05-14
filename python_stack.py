#python 实现栈

class Sstack:

	def __init__(self):
		self._element = []

	def Is_empty(self):
		return self._element == []

	def top(self):
		if self._element == []:
			raise StackUnderflow(" in Sstack.top()")

		return self._element[-1]

	def push(self,element):
		self._element.append(element)

	def pop(self):
		if self._element == []:
			raise StackUnderflow("in Sstack.pop()")

		return self._element.pop()

	#_element知识在类的内部使用，因此用下划线开头

st1 = Sstack()
a = "上海自来水来自海上一直在路上"
print("a:%s"%a)
b=[]
for i in a:
	st1.push(i)
while not st1.Is_empty():
	b.append((st1.pop()))
print("b:%s" % "".join(b))