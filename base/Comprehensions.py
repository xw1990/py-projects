# 推导式可以从一个数据序列构建另一个行的数据序列的结构体

# 列表推导式
# [out_exp_res for out_exp in input_list] or [out_exp_res for out_exp in input_list if condition]
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

# 字典推导式
# { key_expr: value_expr for value in collection } or { key_expr: value_expr for value in collection if condition}
listdemo = ['Google','Runoob', 'Taobao']
newdict = {key:len(key) for key in listdemo}
print(newdict)

# 集合推导式
# { expression for item in Sequence } or { expression for item in Sequence if conditional }
newset = {i**2 for i in (1,2,3)}
print(newset)

# 元组推导式
# (expression for item in Sequence ) or (expression for item in Sequence if conditional )
a = (x for x in range(1,10))
print(tuple(a))