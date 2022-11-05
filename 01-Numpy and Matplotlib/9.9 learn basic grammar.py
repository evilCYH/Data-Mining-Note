import requests  # 通过import导入包


def link(myurl):  # 定义函数
    r = requests.request(method='GET', url=myurl)  # 通过get方式访问
    if r.status_code == 200:    # 状态码要正确
        print(r.text)  # 打印返回页面
    elif r.status_code == 404:      # 根据状态码打印一些常见错误
        print('资源不存在 not found~')
    elif r.status_code == 502:  # 根据状态码打印一些常见错误
        print('访问的人太多辣')
    else:
        print('网页错误')


if __name__ == '__main__':  # 主函数
    myurl = "http://81.70.101.23:1234"  # 想要访问的url(我的服务器)
    link(myurl)


# print('\n-----------------定义、切片方法-----------------')
# list1 = ['apple1', 'pear1', 'strawberry1', 'banana1']  # 定义list
# print(list1[0])  # list索引从0开始
# print(list1[-1])  # -1索引则代表从后开始取
# print(list1[-2])  # 所以-2就是从后往前取第二个
# print(list1[1:2])  # [n:m]，代表从索引n取到索引m-1
# print(list1[1:])  # 如果m=0，则代表取到最后一个
#
# print('\n-----------------操作方法-----------------')
# list2 = ['apple2', 'pear2', 'strawberry2', 'banana2']
# list2.append('watermalon')  # append方法用于在末尾追加
# print(list2)
# list2.insert(1, 'tomato')  # insert方法用于在指定索引处插入
# print(list2)
# list2.remove('tomato')  # remove方法用于去除指定数据
# print(list2)
# list2.clear()  # clear方法用于直接清空列表
# print(list2)

# print('\n-----------------定义、切片方法-----------------')
# tuple1 = ('cat1', 'dog1', 'bear1', 'yuhong')    # 定义tuple
# print(tuple1)
# tuple4 = ('cat2',)   # 如果只有一个元素，一定要加逗号
# print(tuple4)
# tuple5 = ('cat3')   # 不加逗号会定义成字符串
# print(tuple5)
#
# # 切片方法与list相同
# print(tuple1[-1])  # -1索引则代表从后开始取
# print(tuple1[-2])  # 所以-2就是从后往前取第二个
# print(tuple1[1:2])  # [n:m]，代表从索引n取到索引m-1
# print(tuple1[1:])  # 如果m=0，则代表取到最后一个
#
# print('\n-----------------操作方法-----------------')
# # 由于tuple不能更改元素，所以方法相对少很多，只有一些基础函数
# tuple2 = ('cat2', 'dog2', 'bear2', 'yuhong', 2, 55, 1)
# print(len(tuple2))      # 统计长度方法
# tuple3 = (100, 2, 55, 1)
# print(max(tuple3))      # 最大
# print(min(tuple3))      # 最小
#
# # 看似例外: 当tuple元素为list时可以改变list元素，看起来tuple元素变了
# tuple3 = ('cat3', 'dog3', ['bear3', 'bear4'], 'yuhong')
# tuple3[2][0] = 'woof1'
# tuple3[2][1] = 'woof2'
# print(tuple3)

# print('\n-----------------定义、访问方法-----------------')
# dict1 = {'name':'cyh', 'age':18, 'major':'information'}     # 定义dict字典：key-value
# print(dict1['age'])     # 通过key访问
#
# print('\n-----------------操作方法-----------------')
# dict2 = {'name':'zyh', 'age':19, 'major':'teacher'}
# print(dict2.get('name'))    # 也可以通过get方法取到key的相应value
# print(dict2.get('name~'))    # 如果key不存在则返回none
# dict2.pop('major')      # 通过pop方法删除key-value键值对
# print(dict2)

# print('\n-----------------函数的定义和主函数调用-----------------')
# def power(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
# if __name__ == '__main__':
#     print(power(4,3))

# print('\n-----------------类的定义和使用-----------------')
#
#
# class Student:  # 类通过class来定义
#     """
#     class中的函数称为方法
#     定义特殊的__init__方法，在创建实例的时候可以赋予我们认为必要的属性
#     并且__init__方法的第一个参数必须是self，表示创建的实例本身
#     """
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# s1 = Student("yuhong", 19)  # 由类创建的对象称为实例
#
# print(s1.name)
# print(s1.age)
#
# print('\n-----------------修改属性的值-----------------')
# # 类的对象可以通过赋值直接修改属性的值
# s2 = Student("yuhong", 19)
# print("修改前: \n"+s2.name)
# print(s2.age)
#
# s2.age = 20     # 修改示例属性的值
# print("修改后: \n"+s2.name)
# print(s2.age)
#
# # 删除属性
# s3 = Student("yuhong", 19)
# print("删除前: \n"+s3.name)
# print(s3.age)
#
# del s3.age     # 修改示例属性的值
# print("删除后: \n"+s3.name)
# print(s3.age)

# print('\n-----------------类的继承-----------------')
#
#
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print("\n这是printname方法")
#         print(self.firstname, self.lastname)
#
#
# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
#
#
# x = Student("yuhong", "chen")
# x.printname()

# num = random.randint(0, 100)
# print('共有6次猜测机会哦~')
# for i in range(1, 7):
#     guess_num = int(input('请输入第%d次猜数的数值:' % i))
#     if guess_num == num:
#         print('恭喜你，猜对了，共花了%d次猜数机会' % i)
#         break
#     elif i == 6:
#         print('很遗憾，你的次数已经用完，正确答案是'+str(num))
#     elif guess_num < num:
#         print('抱歉，你猜小了')
#     elif guess_num > num:
#         print('抱歉，你猜大了')

# def num():
#     arr = []
#     for i in range(1, 5):
#         for j in range(1, 5):
#             for k in range(1, 5):
#                 num = 100 * i + 10 * j + k
#                 if i != j and j != k and i != k and num not in arr:  # 互不相同且无重复数字的三位数
#                     arr.append(num)
#     print("共有%d个互不相同且无重复数字\n" % len(arr))
#     print("分别为: "+str(arr))
#
#
# if __name__ == '__main__':
#     num()
