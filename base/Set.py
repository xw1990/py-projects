# 无序不重复元素序列

# 集合的创建
# 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
emptySet = set()
set1 = {1, 2, 3, 4}            # 直接使用大括号创建集合
set2 = set([4, 5, 6, 7])      # 使用 set() 函数从列表创建集合

# 集合推导式
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

s = set()

# 添加元素
s.add(1)
s.update({1,3,5,7,2,4,8})
print("s =",s)

# 移除元素
s.remove(1) #元素不再会报错
print("s =", s)
s.discard(1) #元素不再也不会报错
x=s.pop() #随机删除
print("x =", x)
s.clear()
