#有理数类的定义

class Rational:
	@staticmethod   #参数不带self，可以通过类的名字通过.直接调用，也可以通过类的实例对象通过.调用
	def _gcd(m,n):   #_下划线开头的函数和属性都当作内部使用,一般不应该在类外使用.__双下划线开头的,不能直接运用名字访问
		if n > m :
			m,n=n,m
		while n!=0:
			m,n=n,m%n
		return m

	def __init__(self,num , den=1):
		if not  isinstance(num,int) or not isinstance(den,int):
			raise TyprError
		if den == 0 :
			raise ZeroDivisionError
		sign = 1
		if num<0:
			num , sign = -num , -sign
		if den<0:
			den , sign = -den , -sign
		g = Rational._gcd(num,den)

		self._num = sign * (num//g)
		self._den = den//g

	def get_num(self):		#返回有理数分子和分母的接口
		return self._num
	def get_den(self):
		return self._den

	def __add__(self, another): 	#python为所有的算术运算符规定了特殊的方法名,都以两个下划线开头和结尾
		den = self._den * another.get_den()
		num = self._num * another.get_den() + self._den * another.get_num()
		return Rational(num , den)
	
	def __mul__(self,another):
		return Rational(self._num*another.get_num(),self._den*another.get_den())
	
	def __floordiv__(self,another):
		if another.get_num() == 0:
			raise ZeroDivisionError
		return Rational(self._num*another.get_den(),self._den*another.get_num())

	#比较相等和不等
	def __eq__(self,another):
		return self._num*another.get_den() == self._den*another.get_num()  #等于
	def __lt__(self,another):
		return self._num*another.get_den() < self._den*another.get_num()  #小于 

	#为了便于输出
	def __str__(self):
		return str(self._num)+"/"+str(self._den)
	# 或者这些写
	def print(self):
		print(self._num,"/",self._den)


five = Rational(5,6)
x = Rational(3,5)
print("输出有理数x:")
x.print()
print(x.__str__())

print("输出有理数five:")
five.print()
print(five.__str__())

y = five + x*Rational(5,17)
print("有理数y:")
print(y)


#字典推导式
#{key:value for (key,value) in iterable}
#列表推导式
#[x for x in range(5)]