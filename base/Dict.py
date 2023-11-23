# 键必须是唯一的，而且必须是不可变的，如字符串、数字
# 值可以取任何数字类型

# 创建字典
emptyDict = {}
emptyDict1 = dict()
tinydict1 = { 'abc': 123, 98.6: 37 }

# 打印字典
print(tinydict1)

# 访问字典值
print(tinydict1['abc'])

# 修改字典值
tinydict1['abc'] = 456
print(tinydict1['abc'])

# 删除字典元素
tinydict2 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del tinydict2['Name']
print(tinydict2)

tinydict2.clear()
print(tinydict2)


