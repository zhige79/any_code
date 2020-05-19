# 这是一段注释
"""
这也是一段注释
"""
# 适当的添加注释能够使代码变得更易于理解

# 在学习此文件时，你必须先将python语言的编程环境安装到您的计算机内

# 去访问www.python.org下载或在windows下使用该文件夹下的python-3.7.3-amd64.exe文件安装

# 此后所有的代码都是基于python3.7版本

# 所有基础教程均在此文件内，每个代码知识点运行时的结果我们使用20个=来分隔

# 开始
# ====================
# 一,第一个python程序     hello world
# 学习一门编程语言，大多数人先学习在屏幕上打印hello world
print("一、====================")  # 这是为了运行时分清代码块
# 代码：

print("hello world")

# hello world 使用""包含是为了表示它是一个字符串，print("hello world")表示在屏幕上打印字符串hello world
# 这是一个惯例，python的打印字符串就是如此简单明了,一行解决
print("二、====================")

# 二、有打印语句，即输出语句，自然也有输入语句 使用input

# 这边先说一下什么是变量，变量就像一个名字,
# 比如a = 1 ，a是变量，它是数据1的一个名字，通过访问名字a,就可以访问到数据1
# 我们试一下
a = 1  # 此处定义了一个变量a，将a所对应的值设置为1
print(a)  # print语句，在屏幕上打印a的值
# 这时，我们看到电脑上显示了a所代表的1
# 再来看输入语句
# 代码:

input_var = input("输入提示：")

# 我们使用变量input_var来接收你输入的内容,input接收一个参数，一个提示字符串
# 提示字符串会先行打印到屏幕上，然后程序暂停，等待输入
# 你任意输入一些内容，然后点击回车
# 这时，我们打印一下变量input_var,这个变量接收了你输入的内容
print(input_var)

# ok, 你成功打印出来了吗？
# input语句的返回值是一个字符串，如果你需要返回其他类型的数据，请使用强制类型转换，这会在后面讲解


# 三、python运算符
print("三、====================")

# 简单的例子：4 + 5 = 9 ,4 和 5 我们称作操作数，“+”被称作运算符

# 算数运算符
add = 10 + 5  # 加法运算
minus = 10 - 5  # 减法运算
multiply = 10 * 5  # 乘法运算
divide = 10 / 5  # 除法运算
remainders = 10 % 5  # 求余运算
power = 10 ** 5  # 幂运算，即10的5次方
aliquot = 10 // 4  # 整除运算

# 比较运算符
is_same = 1 == 1  # “==”计算两边值是否相等 ，相等该变量就为True,不相等就为False
not_same = 1 != 1  # “!=”计算两边值是否不相等,不相等为True，相等为False
greater_than = 2 > 1  # “>”计算左边值是否大于右边值，大于则为True，否则为False
less_than = 2 < 1  # “<”计算左边值是否小于右边值，小于则为True,否则为False
greater_or_same = 2 >= 1  # 与上同理
less_or_same = 2 <= 1  # 与上同理

# 赋值运算符
assignment = 3  # 简单赋值运算符
# 其他的赋值运算符在输出语句中演示

# 位运算符      将数字看作二进制进行计算
# 60 = 00111100        13 = 00001101
Bitwise_and = 60 & 13  # 按位与
Bitwise_or = 60 | 13  # 按位或
Bitwise_not_or = 60 ^ 13  # 按位异或
Bitwise_not = ~60  # 按位取反
Bitwise_left = 60 << 2  # 按位左移，左边为数据，右边为移动的位数
Bitwise_right = 60 >> 2  # 按位右移

# 逻辑运算符         True和False的运算符
is_and = True and False  # 逻辑与
is_or = True or False  # 逻辑或
is_not = not True  # 逻辑非

# 成员运算符
is_member = 'a' in 'apple'
not_member = 'a' not in 'apple'

# 身份运算符     判断是否是同一个对象的引用
a = 1
b = a
absolute_same = a is b
absolute_not_same = a is not b
# 依次打印这些变量
# 算数运算符
print("     算数运算符")
print("10 + 5 = " + str(add))  # 加法   str(add)使用了强制类型转换，整型数据转为了字符串
print("10 - 5 = " + str(minus))  # 减法
print("10 * 5 = " + str(multiply))  # 乘法
print("10 / 5 = " + str(divide))  # 除法
print("10 % 5 = " + str(remainders))  # 求余
print("10 ** 5 = " + str(power))  # 幂
print("10 // 4 = " + str(power))  # 整除
# 比较运算符
print("     比较运算符")
print("1 == 1 是" + str(is_same))  # 相等
print("1 != 1 是" + str(not_same))  # 不相等
print("2 > 1 是" + str(greater_than))  # 大于
print("2 < 1 是" + str(less_than))  # 小于
print("2 >= 1 是" + str(greater_or_same))  # 大于等于
print("2 <= 1 是" + str(less_or_same))  # 小于等于
# 赋值运算符
print("     赋值运算符")
print("给变量assignment赋值：" + str(assignment))
assignment += 2  # 等同于assignment = assignment + 1 一下同理，只换了符号，但是注意上下文的数据变化
print("assignment进行+=2运算：" + str(assignment))
assignment -= 2
print("assignment进行-=2运算：" + str(assignment))
assignment *= 2
print("assignment进行*=2运算：" + str(assignment))
assignment /= 2
print("assignment进行/=2运算：" + str(assignment))
assignment %= 2
print("assignment进行%=2运算：" + str(assignment))
assignment **= 2
print("assignment进行**=2运算：" + str(assignment))
assignment //= 2
print("assignment进行//=2运算：" + str(assignment))
# 位运算符
print("     位运算符")
print("60 & 13 = " + str(Bitwise_and))  # 按位与
print("60 | 13 = " + str(Bitwise_or))  # 按位或
print("60 ^ 13" + str(Bitwise_not_or))  # 按位异或
print("~60 = " + str(Bitwise_not))  # 按位取反
print("60 << 2 = " + str(Bitwise_left))  # 按位左移
print("60 >> 2 = " + str(Bitwise_right))  # 按位右移
# 逻辑运算符
print("     逻辑运算符")
print("True and False = " + str(is_and))  # 且
print("True or False = " + str(is_or))  # 或
print("not True = " + str(is_not))  # 非
# 成员运算符
print("     成员运算符")
print("\'a\' in \'apple\' = " + str(is_member))  # 包含在内
print("\'a\' not in \'apple\' = " + str(not_member))  # 不包含在内
# 身份运算符
print("     身份运算符")
print("a = 1    b = a")
print("a is b = " + str(absolute_same))
print("a is not b = " + str(absolute_not_same))
# 运算符优先级
print("运算符优先级       从上到下优先级递减\n"
      "**\n"
      "~ ，+， -\n"
      "*，/， %， //\n"
      "+，-\n"
      ">>，<<\n"
      "&\n"
      "^，|\n"
      "<=，<，>，>=\n"
      "==, !=\n"
      "=，%=，/=，//=，-=，+=，*=，**=\n"
      "is，is not\n"
      "in，not in\n"
      "not，and，or"
      )

# 四、数据类型及数据类型转换
print("四、====================")

# 1、数字类型
var_int = 1  # 1是一个整型数据
var_float = 1.2  # 1.2是一个浮点型数据
var_complex = 1 + 2j
# 1+2j是一个复数数据，也可以写成complex(1, 2)，实部和虚部都是浮点型数据,j是相当于数学复数里的i
# 数字类型可以进行运算
# 例如：
double_2 = 2 + 2
double_2_2 = 2.2 + 2.2
double_2_2j = (2 + 2j) + (2 + 2j)
# 打印一下
print("整型数据:" + str(var_int))
print("浮点型数据:" + str(var_float))
print("复数数据" + str(var_complex))
print("2 + 2 = " + str(double_2))
print("2.2 + 2.2 = " + str(double_2_2))
print("(2 + 2j) + (2 + 2j) = " + str(double_2_2j))
# 2、字符串类型
var_str1 = " hello "
var_str2 = " world "
str_joint = var_str1 + var_str2  # 字符串相加的操作被称作字符串拼接
str_section_1 = var_str1[1]  # 变量名[索引值]：被称为切片，可以通过切片访问字符串的一个字符
str_section_2 = var_str1[1:3]  # 变量名[索引值:索引值]，也是切片，通过这种语法访问字符串中的一部分,返回索引1，2的值
# 骚操作来了
cool_str = var_str1[1:3] + var_str2  # 可以通过切片所生成的字符串进行拼接
# 打印一下
print("字符串1：" + var_str1)
print("字符串2： " + var_str2)
print("字符串拼接 字符串1+字符串2：" + str_joint)
print("字符串切片 字符串1中索引1所对应的值:" + str_section_1)
print("字符串切片 字符串中")

# 另外，还有*运算符，重复输出字符串
print("\'hello\' * 5 = " + "hello" * 5)
# 字符串格式化
print("I say \"%s\"" % "hello world")
# 字符串切片
print("apple"[2:3])
# 三引号字符串的操作，所见即所得的字符串，可用于html，sql等
three = """
第一行字符串
第二行字符串"""
print(three)
# f-string型字符串
print(f'{1 + 2}')

# 列表        # 列表是最常用的数据类型之一，可以包含任意数据类型 可修改
a = [1, 2, 3, 4]
b = ["a", "b", "c", "d"]
print("这是2个列表")
print(a)
print(b)
# 通过索引来访问列表中的值
print(a[2])
# 索引是从0开始计算的，这就是为啥大家说程序员数数都是从0开始数
print(b[1:3])  # 列表切片
# 可以通过索引值直接修改列表中的元素
a[2] = 5  # 修改列表a中索引为2的元素为5
print(a)  # 输出
del a[2]  # 删除元素

# 元组        # 与列表基本相同，唯一的不同是不可修改
a = (1, 2, 3, 4)
print(type(a))  # type()方法返回变量a的类型，这个方法是python的一个内置方法，对于任何对象都有用
b = (1,)  # 如果一个元组里面只有1个元素，需要加一个逗号，否则会将()看作运算符
print(type(b))
# 访问元组      使用索引
print(a[2])
# 修改元素
# a[2] = 5  是非法的，会引发异常
# 可以通过创建一个新的元组来实现修改
c = a + b
print(c)
# 删除
# 元组中的元素不支持删除，但是可以直接删除整个元组
del c
# print(c)        # 这行会报错

# 字典
# 字典是另一种可变容器模型，可存储任意类型对象，利用{}表示
d = {'1': 'one', '2': 'two'}  # 这是一个字典    key, value对象，键值对对象
print(d['1'])  # 字典通过键来作为内容索引，键一般是唯一的
print(d)
# 修改字典内容
d['3'] = 'three'  # 添加内容
print(d)
d['1'] = 'no.1'  # 更新内容
print(d)
del d['1']  # 通过键删除字典中某个元素
print(d)
d.clear()  # 清空字典中所有条目
print(d)
del d  # 删除字典
# print(d)        运行会报错，因为这时字典d已经不存在
"""
      注意：
            1、不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
            2、键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
            3、
"""
# 这里列出了一些字典常用的函数
a = {'1': 'one'}
b = {'2': 'two', '1': 'one'}
seq = [1, 2, 3]
print(len(a))  # 输入字典的长度
print(str(a))  # 输出字典可打印的字符串表示
print(type(a))  # 输出变量a的类型，即字典
a.clear()  # 清空字典a中的所有元素
b.copy()  # 返回字典b的浅复制
a.fromkeys(seq, 10)  # 前一个参数是一个序列，用这个序列作为字典的键，后一个参数作为字典所有键的初始值
b.get('1', '无此元素')  # 返回指定键的值，如果值不在字典中返回default值
b.items()  # 以列表返回可遍历的(键, 值) 元组数组
print(b.keys())  # 返回字典b中的所有键
a.update(b)  # 把字典b中的元素更新到字典a
print(a.values())  # 以列表形式返回字典中的所有值

# 五、函数与类
print("五、====================")


# 函数
# 函数使用关键字def定义
# 这里创建了一个add函数，用来实现2数相加
def add(a, b, c=0):     # c设置了一个默认值
    return a + b + c


# 在这里调用这个函数
print(add(1, 2))  # 这里输出1+2的值
# 匿名函数，使用lambda关键字
sums = lambda a, b: a+b
print(sums(1, 2))       # 使用变量名来作为函数名，可有效精简代码
# 全局变量与局部变量
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
# 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。


# 类         面向对象编程 class关键字
# 类就像一个模板，可以通过类去创建对象实例
# 这里我们创建一个学生类
class Student:
      def __init__(self, name):           # __init__函数实现了对象的初始化
            self.name = name

# 这里来创建实例
xiaoming = Student('xiaoming')            # 创建了一个实例
print(xiaoming.name)                      # 通过实例，输出该实例的属性

# 六，异常处理
print("六、====================")
# 我们在程序调试的时候，经常会遇到程序出现异常，大多数异常不会被程序处理，异常的处理就显得尤为重要
# 使用try except语句进行异常处理

try:
      a = {'1', 'd'}
      del a
      print(a)          # 此处故意创建了一个NameError异常
      print("正常运行")
except NameError:             # 程序捕获该异常，并给出处理办法
      print("出现错误")
      pass
else:                         # 没有发生异常就进入else处理逻辑
      print('输出else语句')
finally:                      # 无论是否发生异常都会进入finally处理逻辑
      print('进入finally处理逻辑')
