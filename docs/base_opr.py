# *** 字典 ***
# get() 返回指定键的值
# items() 返回一个列表，其中包含每个键值对的元组
# keys() 返回包含字典键的列表
# pop() 删除具有指定键的元素
# popitem() 删除最后插入的键值对
# setdefault() 返回指定键的值。如果密钥不存在：插入具有指定值的密钥
# update() 使用指定的键值对更新字典
# values() 返回字典中所有值的列表

# 初始化一个带默认类型的字典
from collections import defaultdict

defaultdict(list)  # {k: []}
defaultdict(set)  # {k: {}}
defaultdict(str)  # {k: ''}
defaultdict(int)  # {k: 0}
defaultdict(lambda: 0)  # {k: 0}

# 删除某一项，返回value；如果key不存在，返回defaultvalue
# dictionary.pop(keyname, defaultvalue)
d = dict()
d.get("a", "1")  # 字典本身不变，key不存在返回指定值，{}
d.setdefault("a", "2")  # key不存在，在字典中添加此项，{'a': '2'}

# *** 数组 ***
# append() 在列表末尾添加元素
# clear() 从列表中删除所有元素
# copy() 返回列表的副本
# count() 返回具有指定值的元素数
# extend() 将列表（或任何可迭代）的元素添加到当前列表的末尾
# index() 返回具有指定值的第一个元素的索引
# insert() 在指定位置添加元素
# pop() 删除指定位置的元素
# remove() 用于移除列表中某个值的第一个匹配项。
# reverse() 对列表 list 所有元素进行逆序排列
# sort() 排序列表

# 初始化数组
L = [0 for _ in range(9)]
L.pop()  # 模拟出栈
L.pop(0)  # 模拟出队列

# 初始化一个二维数组
r = 3
c = 3
# 由于此方法构造的二维数组是对[]*c引用了r次，更改其中一行的值会导致每行的值都被更改
L1 = [[0] * c] * r
# 单行使用列表推导式实现
L2 = [[0 for _ in range(c)] for _ in range(r)]
# 列表、字典和集合推导式及生成器表达式，[]/{k:v}/{}/()

# *** 集合 ***
# clear() 从字典中删除所有元素
# copy() 返回字典的副本
# fromkeys() 返回具有指定键和值的字典
# add() 将元素添加到集合中
# clear() 从集合中删除所有元素
# copy() 返回集合的副本
# difference() Returns a set containing the difference between two or more sets
# difference_update() 删除此集合中还包含在另一个指定集合中的项目
# discard() 删除指定的项目
# intersection() 返回一个集合，即另外两个集合的交集
# intersection_update() 删除此集合中其他指定集合中不存在的项目
# isdisjoint() 返回两个集合是否相交
# issubset() 返回另一个集合是否包含此集合
# issuperset() 返回此集合是否包含另一个集合
# pop() 从集合中删除一个元素
# remove() 删除指定的元素
# symmetric_difference() 返回具有两组对称差的一组
# symmetric_difference_update() 插入此集合和另一个中的对称差
# union() 返回一个包含集合并集的集合
# update() 使用此集合和其他集合的并集更新集合

# *** 字符串 ***

# *** 高级函数 ***
# 多条件排序
list_sort = list()
sorted(list_sort, key=lambda x: (-x[2], x[1], x[0]))
# 按照原数组的下标排序
sorted(list_sort, key=list_sort.index)
dict_sort = dict()
sorted(dict_sort.items(), key=lambda x: x[0], reverse=True)
sorted(dict_sort.items(), key=lambda x: -x[1])

from operator import itemgetter

a = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
sorted(a, key=itemgetter(1, 2))  # 先按照元组中下标为1的值对对象排序，当下标为1的值相同时，再按照下标2来排序
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
sorted(a, key=itemgetter(1, 2), reverse=True)  # 从大到小
# [('jane', 'B', 12), ('dave', 'B', 10), ('john', 'A', 15)]
sorted(a, key=itemgetter(2), reverse=True)  # 仅按照元组中下标为2的值对对象排序，从大到小。
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

# *** 正则 ***

# *** 标准库 ***
