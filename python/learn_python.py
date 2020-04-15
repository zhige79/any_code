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
is_and = True and False     # 逻辑与
is_or = True or False       # 逻辑或
is_not = not True           # 逻辑非

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
print("True and False = " + str(is_and))    # 且
print("True or False = " + str(is_or))      # 或
print("not True = " + str(is_not))          # 非
# 成员运算符
print("     成员运算符")
print("\'a\' in \'apple\' = " + str(is_member))  # 包含在内
print("\'a\' not in \'apple\' = " + str(not_member))    # 不包含在内
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
var_int = 1          # 1是一个整型数据
var_float = 1.2      # 1.2是一个浮点型数据
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
str_joint = var_str1 + var_str2     # 字符串相加的操作被称作字符串拼接
str_section_1 = var_str1[1]         # 变量名[索引值]：被称为切片，可以通过切片访问字符串中的值

