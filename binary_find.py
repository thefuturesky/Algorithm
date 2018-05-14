class Two_find:
    def rank(self,key,array):
        lo = 0
        hi = len(array)-1
        key = int(key)
        while(lo<=hi):
            mid = (lo+hi)//2
            if key<array[mid]:
                hi = mid-1
            elif key>array[mid]:
                lo = mid+1
            else:
                return key
        return -1


    def main(self):
        num = input('用空格分隔多个数据:')
        a = [int(n) for n in num.split()]
        print(a)
        b = int(input("请输入一个需要查找的数："))
        c = self.rank(b,a)
        if c==-1:
            print("查找的数不存在！！！")
        else:
            print("查找的数：%d已经找到，下标位：%d" % (b,int(a.index(b))))


a=Two_find()
a.main()
