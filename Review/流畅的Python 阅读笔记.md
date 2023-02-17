# 流畅的Python 阅读笔记

## 第一部分：序幕

### 第1章：	Python数据模型

#### 	1.1	一摞Python风格的纸牌

​		使用collection中的namedtuple来构建FrenchDeck

​		三个方法：\_\_init\_\_，\_\_getitem\_\_，\_\_len\_\_

​		\_\_getitem\_\_可以实现迭代

​		\_\_contains\_\_，如果没有，in会遍历

#### 	1.2	如何使用特殊方法

​			很多时候调用特殊方法是隐式的。比如for...in...就是调用iter(x)，背后则是x.\_\_iter\_\_()

​			不要随意添加特殊方法

​				1.2.1	模拟数值类型	

​					\_\_repr\_\_ \_\_abs\_\_  \_\_add\_\_  \_\_mul\_\_ \_\_bool\_\_

​				1.2.2	字符串表示形式

​					\_\_repr\_\_和\_\_str\_\_的区别

​				1.2.3	算数运算符
​					+和*这两个方法通过\_\_add\_\_和\_\_mul\_\_实现

​				1.2.4	自定义的布尔值

​					bool背后调用\_\_bool\_\_方法，如果不存在会尝试调用\_\_len\_\_()，为0返回False，不然返回True

#### 	1.3	特殊方法一览

​			P11
#### 1.4	为什么len不是普通方法

​			Cpython会直接从一个C结构体里读取对象操作（后门）
#### 1.5	本章小结

​			collections.namedtuple

#### 1.6	延伸阅读



## 第二部分：数据结构

### 第2章：	序列构成的数组

####	2.1	内置序列类型概览

​	容器序列(引用)/扁平序列(值)

​	可变序列/不可变序列

####	2.2	列表推导和生成器表达式

​	2.2.1	列表推导和可读性

​	[表达式 for 迭代变量 in 可迭代对象 [if 条件表达式] ]

​	2.2.2	列表推导同fliter和map的比较

​		list(filter(筛选条件表达式，迭代变量））

​	2.2.3	笛卡儿积

​	[表达式 for 迭代变量 in 可迭代对象 for 迭代变量 in 可迭代对象]		

​	2.2.4	生成器表达式

​	(表达式 for 迭代变量 in 可迭代对象 [if 条件表达式] )

####	2.3	元祖不仅仅是不可变的列表

​	2.3.1	元组和记录

​		信息和位置是捆绑的

​	2.3.2	元组拆包

​		x,y = (x,y)

​		x,y = *(x,y)

​		_ 占位符

​		*args来获取不确定数量的参数

​		平行赋值 a,b,\*rest,c=range(5)， #0,1,[2,3],4

​	2.3.3	嵌套元组拆包

​		a,b,(c,d)=(a,b,(c,d))

​	2.3.4	具名元组

​		collections.namedtuple('类名','各字段名')

​		字段名可以是带空格的字符串，或者由数个字符串组成的可迭代对象

​		.\_\_fields
​		.\_\_make()
​		.\_\_asdict()
​	2.3.5	作为不可变列表的元组

####	2.4	切片
​	2.4.1	为什么切片和区间会忽略最后一个元素

​	2.4.2	对对象进行切片

​		对seq[start:stop:step]求值会调用seq.\_\_getitem\_\_(slice(start,stop,step))

​	2.4.3	多维切片和省略

​		主要针对Numpy这类

​		Python内置的序列类型都是一维的

​		省略 ...

​	2.4.4	给切片赋值

​		如果赋值的对象是一个切片，赋值语句的右侧必须是一个可迭代对象

​		赋值语句两侧的元素个数不需要一致

```python
l[2:5]=[100] #必须是一个可迭代对象，不能是100
```



####	2.5	对序列使用+和*

​	+和*的操作都不修改原有的操作对象，而是构建一个全新的序列

####	2.6	序列的增量赋值

​	优先\_\_iadd\_\_（用于就地加法，如果没有会选择add方法，这时类似a=a+b(得到新对象，赋值给a))

​	不要把可变对象放在元组中，增量赋值不是原子操作

#### 2.7	list.sort方法和内置函数sorted

​	list.sort会在元列表上操作

​	sorted会有新的列表返回

####	2.8	用bisect来管理已排序的序列

​	2.8.1	用bisect来搜索

​		参数是一个有序列表和一个值，返回插入位置

```python
bisect.bisect(a,x,lo=0,hi=len(a),*,key=None) # bisect_right
bisect.bisect_left
```

​	2.8.2	用bisect.insort插入新元素

​		参数是一个升序列表和一个值，插入后保持升序不变

```python
bisect.insort
bisect.insort_left
```



#### 2.9	当列表不是首选时

​	2.9.1	数组

​		array.array('类型',生成器)，只包含数字

​		支持方法：pop，insert，extend，frombytes，tofile

```python
array.array(typecode,[,initializer])

typecode
itemsize
append(x)
buffer_info()
byteswap()
count(x)
extend(iterable)
frombytes(s)
fromfile(f,n)
fromlist(list)
fromunicode(s)
index(x[,start[,stop]])
tolist()
tounicode()
insert(i,x)
pop([i])
remove(x)
reverse()
tobytes()
tofile(f)
```

​		不再支持list.sort排序，排序需要使用array.array(a.typecode,sorted(a))

​	2.9.2	内存视图

​		cast方法，以不同的类型来读取内存中的一段数据

​	2.9.3	Numpy和Scipy

​		两个重要的科学库

​	2.9.4	双向队列和其他形式的队列

​		双向队列collections.deque(可迭代对象，maxlen参数)

​			rotate，appendleft，extend，extendleft（加入时的顺序要注意）

####	2.10	本章小结

​				了解filter和map函数

​				collections库

​				bisect库

​				array.array

​				memoryview

####	2.11	延伸阅读



###	第3章：字典和集合

####	3.1	泛映射类型

​	collections.abc中的Mapping和MutableMapping是dict和其他类似的类型的超类

​	dict是abc.Mapping的子类

​	可散列的数据类型定义

​		实现hash方法和eq方法。元组只有在所有元素都是可散列的时候本身才可散列

​		散列值时按照id()的值散列

####	3.2	字典推导
​		{key:value for.....}

####	3.3	常见的映射方法
​		copy是浅复制

​		使用setdefault(key,[default])来处理找不到的键

####	3.4	映射的弹性键查询

​	3.4.1	defaultdict： 处理找不到的键的一个选择

​		collections.defaultdict(default_factory=None,/[,...])来构建字典

​	3.4.2	特殊方法 \_\_missing\_\_

​		\_\_missing\_\_方法只会被\_\_getitem\_\_调用

​			注意\_\_missing\_\_中可能会遇到的无线递归问题。\_\_missing\_\_一定要有退出机制

​		自定义映射类的时候适合继承collections.UserDict类

​		isinstance方法确认实例是不是属于这个类

####	3.5	字典的变种

​		collections.OrderDict：添加键的时候保持顺序

​		collections.ChainMap：可以容纳数个不同的映射对象，查找时会被作为一个整体查找

​		collections.Counter： 键的每次更新都会有计数器

​			update,mostcommon方法

​		collections.UserDict：标准dict的纯python版本，用来作为用户继承写子类

####	3.6	子类化UserDict

​		使用UserDict能避免dict中的部分捷径导致的子类需要重写

​		UserDict不是dict的子类，但其中的data部分是dict的实例

####	3.7	不可变映射类型

​		types.MappingProxyType：镜像一个字典，不能对这个镜像进行任何修改。修改元字典的结果会反馈到这个镜像字典上

​		types.MappingProxyType(mapping)

####	3.8	集合论

​	可以去重，集合中元素必须可以散列。

​	set本身是不可散列的，但frozenset可以

​	中缀运算符

​	3.8.1	集合字面量

​		{元素,[元素]}，空集合必须表示为set()

​		frozenset没有特殊字面量句法，必须使用构造方法 frozenset(set)

​	3.8.2	集合推导

​		{元素 for...}

​	3.8.3	集合的操作

​		中缀操作符需要两个都是集合，但其他的方法只要求传入的参数是可迭代对象

​		a.union(b,c,d)
####	3.9	dict和set的背后

​	3.9.1	一个关于效率的实验

​		不管查询多少个元素的字典或者集合，所耗费的时间都可以忽略不计

​	3.9.2	字典中的散列表

​		散列表是稀疏数组，每个键值对都占用一个元表，包含对键和值的两个引用

​		相等性，加盐操作和散列表算法

​	3.9.3	dict的实现及其导致的结果

​		键必须可以散列

​		内存开销大

​		键查询很快

​		键的次序取决于添加顺序（键值相同时）

​		添加新值可能改变顺序（因为可能扩容）

​	3.9.4	set的实现以及推导结果

​		set和frozenset也是依赖散列表，只有一个值的引用

####	3.10	本章小结

​				了解fliter函数和map函数

​				array.array

####	3.11	延伸阅读



###		第4章：文本和字节序列

####	4.1	字符问题

​	decode，encode

​	bytes以'b'开头

####	4.2	字节概要

​	bytes或者bytearry对象的各个元素都是0-255之间的数

​	每个字符可能含有1个或者多个字节

​	bytes[:]返回的是切片字节，而bytes[n]返回一个元素的话是256以内的整数

​	字节值可能会以三种方式转换

​		可打印ASCII范围的字节，使用字节自身

​		制表符，换行符，回车符和\对应使用转义

​		其他字节的值，使用十六进制转义序列

​	结构体和内存视图

​		struct模块提供一些函数看，把打包的字节序列转换成不同类型字段组成的元组，话有一些函数用于执行反向转换

​			struct.unpack(fmt,header)

​				header是memoryview读出的一段值，fmt是读取的格式，返回解读后的内容

####	4.3	基本的编码器

####	4.4	了解解码问题

​	4.4.1	处理UnicodeEncodeError

​		文本转为字节序列时目标编码中没有定义字符，抛出异常

​	4.4.2	处理UnicodeDecodeError

​		二进制转文本时，遇到无法转换的字节，抛出异常

​	4.4.3	使用预期之外的编码加载模块时抛出的SyntaxError

​		python3 默认utf-8

​	4.4.4	如何找出字节序列的编码

​		命令行文件 chardetect 文件名

​	4.4.5	BOM：有用的鬼符

​		UTF-16中的\xff\xfe就是BOM，字节序标记。指明编码时使用IntelCpu的小字节序列

####	4.5	处理文本文件

​	三明治法。尽早将输入的二进制文件转为字符串，最后将字符串转为二进制。业务中不要编码和解码

####	4.6	为了正确比较而规范化Unicode字符串

​	unicodedata.normalize(参数,str)

​		NFC

​		NFD

​		NFKD

​		NFKC

​	4.6.1	大小写折叠

​		str.casefold() 基本等同于str.lower()

​	4.6.2	规范化文本匹配使用函数

​	4.6.3	极端“规范化”：去掉变音符号

####	4.7	Unicode文本排序
​	非ASCII文本的标准排序方式是使用locale.strxfrm函数

​		locale.setlocale设定比较代码

​		locale.strxfrm作为key的比较函数

​	使用pyuca.Collator.sort_key方法

####	4.8	Unicode数据库

####	4.9	支持字符串和字节序列的双模式API

​	4.9.1	正则表达式中字符串和字节序列

​		字节构成的正则表达式只能匹配ASCII字符

​		字符串模式可以匹配Unicode数字或者字母

​	4.9.2	os函数中的字符串和字节序列

####	4.10	本章小结

####	4.11	延伸阅读



##	第三部分：把函数视视作对象

###	第5章： 一等函数

​	一等对象定义：

​		在运行时创建

​		能赋值给变量或数据结构中的元素

​		能作为参数传给函数

​		能作为函数的返回结果

​	python中所有函数都是一等对象

####	5.1	把函数视作对象

​	函数有属性，可以赋值给变量，也可以作为函数的参数

####	5.2	高阶函数

​	接受函数为参数，或者把函数作为结果返回的函数是高阶函数

​	map，fliter两个个函数（这两个函数返回生成器，可以用生成器替代）

​	all，any，functools.reduce三个归约函数

####	5.3	匿名函数

​	lambda

​	lambda函数的定义体中不能赋值，也不能使用while和try等语句

​	lambda只是语法糖，和def语句一样，会创建函数对象

####	5.4	可调用对象

​	通过callable()判断是否可以调用

​	7种可以调用的对象

​		用户定义的函数

​		内置函数

​		内置方法

​		方法

​		类

​		类的实例

​		生成器函数

####	5.5	用户定义的可调用类型

​	任何python对象都可以通过实现\_\_call\_\_方法来实现实例调用

####	5.6	函数内省

​	使用dir函数可以探知函数属性

​	函数较之其他对象所特有的属性

​		\_\_annotations\_\_	注释

​		\_\_call\_\_	调用

​		\_\_closure\_\_	绑定的自由变量

​		\_\_defaults\_\_	形式参数的默认值

​		\_\_get\_\_	实现只读描述符的协议

​		\_\_globals\_\_	函数所在模块的全局变量

​		\_\_kwdefaults\_\_	仅限关键字默认值

​		\_\_name\_\_	函数名称

​		\_\_qualname\_\_	限定名称

```python
func.__code__.co_varnames #func的参数名和func中的局部变量
func.__code__.co_argcount #func的参数数量
```



####	5.7	从定位参数到仅限关键字参数

​	定义函数时若想指定仅限关键字参数，要把它们放到前面有\*的参数后面。

​	如果不想支持数量不定的定位参数，但想支持仅限关键字参数，在签名中放一个*

​	func(参数1，参数2，*content，关键字1，关键字2，**可变参数)

####	5.8	获取关于参数的信息

​	函数的\_\_defaults__属性保存定位参数和关键字参数的默认值

​	仅限关键字参数的默认值在\_\_kwdefaults\_\_中

​	inspect.signature()探查属性

​	bind把一个个参绑定到签名中的形参上

```python
sig=inspect.signature(func)
sig.parameters.items() #获取func的所有属性
sig.bind(**args)#将属性绑定到func中
```



####	5.9	函数注解
​	可以在各个参数的：之后增加注解表达式，放在参数名和=号之间。存储在\_\_annotations\_\_中

```python
def clip(text:str, max_len:'int > 0'=80) ->str:
```



####	5.10	支持函数式编程的包

​	5.10.1	operator模块

​		operator.itemgetter

​		operator.attrgetter

​		operator.methodcaller

```python
f=attrgetter('name')
f(b) #返回b.name

f=itemgetter(2)
f(b)#返回b[2]

f=methodcaller('name')
f(b) #相当于b.name()
```



​	5.10.2	使用functools.partial冻结参数

​		基于一个函数创建一个新的调用对象，把原函数的某些参数固定

```python
triple=partial(mul,3) #将mul的第一个参数固定为3
```

####	5.11	本章小结
####	5.12	延伸阅读



###	第6章： 使用一等函数实现设计模式

####	6.1	案例分析： 重构“策略”模式
​	6.1.1	经典的“策略”模式

​		策略：抽象基类

​	6.1.2	使用函数实现“策略”模式

​		没有策略，通过函数实现

​	6.1.3	选择最佳策略；简单的方式

​	6.1.4	找出模块中的全部策略

```python
globals()[name] #返回当前的全局符号，通过name来找到对应方法

inspect.getmembers(模块名,inspect.isfunction) #查看模块中所有的函数对象
```



####	6.2	“命令”模式
####	6.3	本章小结

####	6.4	延伸阅读



###	第7章： 函数装饰器和闭包

​	用于在源码中“标记”函数，以某种方式增强函数行为

####	7.1	装饰器基础知识

​	装饰器可以调用的对象，其参数是另一个函数（被装饰的函数）。装饰器可能处理被装饰函数，然后把它返回，或将其替换成另一个函数或可调用对象

####	7.2	Python何时执行装饰器

​	装饰器在被装饰的函数定义之后立刻执行，通常是在导入时（加载模块时）

​		利用这个特性，可以生成一个函数列表在最初的时候装入所有被装饰器修饰过的函数

​	被装饰的函数只在调用时才执行

####	7.3	使用装饰器改进“策略”模式

####	7.4	变量作用域规则

​	Python不要求声明变量，但是假定在函数定义体中赋值的变量是局部变量

```python
b=6
def f(a):
    print(a)
    print(b)
    b=9
f(2) #报错  b在f中又被定义了，而且还在print函数后

```

####	7.5	闭包

​	闭包指延伸了作用域的函数，其中包含函数定义体中引用、但是补在定义体中定义的非全局变量。

​	闭包对于使用函数外的变量要注意类型。如果是不可变类型要特别注意自加之类的处理。

####	7.6	nonlocal声明

​	把变量标记为自由变量，即使在函数中为变量赋予新值，也会变成自由变量。如果已经是自由变量，会更新值。\_\_code\_\_.co_freevars中有自由变量名称，值绑定在\_\_closure\_\_中。

####	7.7	实现一个简单的装饰器

​	functools.wraps装饰器可以把相关的属性从func复制到clocked中

```python
def clock(func):
    @functools.wraps(func)
    def clocked(*args,**kwargs): #*args,**kwargs是func的参数，被wraps打包进来
        '''contents'''
    return clocked
```



####	7.8	标准库中的装饰器

​	7.8.1	使用functools.lru_cache做备忘

​		调用方法@functools.lru_cache()，可以有参数maxsize和typed

​		装饰器可以叠放

​	7.8.2	单分派泛函数

​		泛函数：函数对不同类型的参数会提供不同的处理方式；通过装饰器实现；类似重载机制

​		单分派：根据函数的第一个参数不同来调用具体的执行方式

```python
from functools import singledispatch
@singledispatch
def age(obj):
    print('请传入合法类型的参数！')
@age.register(int)
def _(age):
    print('我已经{}岁了。'.format(age))
@age.register(str)
def _(age):
    print('I am {} years old.'.format(age))
age(23)  # int
age('twenty three')  # str
age(['23'])  # list

```

​		可以把多个函数绑在一起组成一个泛函数

####	7.9	叠放装饰器

```python
@d1
@d2
def func():
    pass

d1(d2(func))
```

####	7.10	参数化装饰器

​	7.10.1	一个参数化的注册装饰器

​		两层函数，最外层带参数，第二层是真正的装饰器

```python
def register(active=True):
    def decorate(func): #真正的包装器
        def clocked(*_args): #具体包装的处理
            '''content'''
        return clocked
    return decorate
```

​	7.10.2	参数化clock装饰器

```python
@register(active=False)
def func():
    pass
```





##	第四部分：面向对象惯用法

### 第8章：对象引用、可变性和垃圾回收

####	8.1	变量不是盒子

​	变量应该是对象的标注，而不是存放对象的具体盒子

​	赋值语句先计算右侧，在将变量绑定在对象上。如果右侧计算出错，左侧变量不会被创建。

####	8.2	标识、相等性和别名

​	比较两个对象相等==是使用eq方法

​	is用来比较id（标识）是否一样，也就是比较是不是同一个对象，id在对象的生命周期中不会改变

​	两个指向同一个对象的变量互相是别名	

​	8.2.1	在==和is之间选择

​		==运算符比较的是值，is比较的是对象的标识

​		变量和单例值之间比较时使用is

​		is比==快，因为直接比较标识，不会重载。

​		==是\_\_eq\_\_的语法糖，相当于a.\_\_eq\_\_(b)，可以被重载

​	8.2.2	元组的相对不可变性

​		元组中包含可变元素（比如列表），修改列表，元组不相等，但id等还是一样的。

​		元组不变的是数据结构中的物理引用

####	8.3	默认做浅复制

​	构造方法list和[:]是浅复制

​	如果复制的对象包含可变元素（引用），则需要考虑两者变动会互相影响

​	如果对于复制对象中的可变元素的修改会导致可变元素id变换，引用发生改变

```python
a=[1,2,3,[4,5]]
b=list(a)
c=a[:]


a[0]=10
a[3][0]=40


print(a)
print(b)
print(c)

print(id(c[3]))
c[3]=[100,200]
print(id(c[3]))
print(c)
```

​	copy模块中的copy和decopy

####	8.4	函数的参数作为引用时

​	python是共享传参。共享传参是指函数的各个形式参数获得实参中各个引用的副本。函数内部的形参是实参的别名

​	函数可能会修改作为参数传的可变对象

​	8.4.1	不要使用可变类型作为参数的默认值

​	8.4.2	防御可变参数

####	8.5	del和垃圾回收

​	del语句删除的是名称，而不是对象，这可能导致对象由于没有引用而被回收。

​	重新绑定也可能导致对象的引用数量归零，导致对象被销毁

​	weakref.finalize可以查看对象的情况，并在对象销毁时运行指定函数

####	8.6	弱引用

​	弱引用不会增加对象的引用数量。引用的目标对象成为所指对象，所以不会妨碍所指对象被当作垃圾销毁

​	weakref.ref绑定弱引用

​	8.6.1	WeakValueDictionary简介

​		weakValueDictionary类实现的是一种可变映射，里面的值是对象的弱引用。被引用的对象在程序中的其他地方被当作垃圾回收后，对应的键会自动从weakValueDictionary中删除。因此经常被用于缓存。

​		对应有weakKeyDIctionary类，key是弱引用

​		weakSet类，保存元素弱引用的集合类

​	8.6.2	弱引用的局限

​		基本的list和dict实例都不能作为所指对象，但他们的子类可以

​		int和tuple不能作为所指对象，子类也不可以

####	8.7	Python对不可变类型施加的把戏

​	cpython有驻留，在copy时没有创建新的副本，而是相同对象的引用。但这只是内部实现，不能依赖

​	判断字符串或整数时应该使用==而不是is

####	8.8	本章小结

####	8.9	延伸阅读



###	第9章：符合Python风格的对象

​	鸭子类型：只需要按照预定行为实现对象所需的方法即可

####	9.1	对象表示形式

​	repr和str

​		\_\_repr\_\_ 便于开发者

​		\_\_str\_\_便于用户

​	bytes和format

​		\_\_bytes\_\_获取对象的字节序列	

​		\_\_format\_\_会被内置函数format()和str.format()调用

####	9.2	再谈向量类

​	为类添加\_\_iter\_\_方法，把实例编程可迭代对象

####	9.3	备选与构造方法

​	类方法使用classmethod修饰，不传入self实例本身，而是传入cls

####	9.4	classmethod与staticmethod

​	classmethod定义的操作类，而不是操作实例。类方法的第一个参数是类本身（cls），而不是实例（self）

​	staticmethod装饰器就是普通函数，只是碰巧在类的定义体中，而不是在模块层定义

####	9.5	格式化显式

​	\_\_format\_\_(format_spec) 格式说明符

​	没有format方法时，会继承str方法

####	9.6	可散列的Vector2d

​	类通过实现\_\_hash\_\_和\_\_eq\_\_两个方法来实现可散列

​	@property装饰器：把读值方法标记为特性

####	9.7	Python的私有属性和“受保护的“属性

​	python会自动为两个下划线的命名实例属性改名，存入实例的dict中，避免继承时被不小心覆盖

​	python解释器不会对使用单个下划线的属性名做特殊处理，但是程序员一般都会遵守，不去修改

####	9.8	使用__slots__类属性节省空间

​	实例的属性会被存储在dict中，会消耗大量内存，通过\_\_slots\_\_属性，让解释器用元组储存实例属性，用来减少实例的数据体积。一般使用元组来作为\_\_slots\_\_属性的值

​	继承自超类的\_\_slots\_\_没有效果，只会使用自己的

​	在类中定义\_\_slots\_\_属性后，实例不再有所列名称以外的其他属性，这是一个副作用

​	需要把\_\_weakref\_\_加入到\_\_slots\_\_中才能使实例作为弱引用目标

####	9.9 	覆盖类属性

​	python中类属性可以为实例属性赋值，如果实例中没有这个属性，会增加

####	9.10	本章小结

#### 9.11	延伸阅读



###	第10章：序列的修改、散列和切片

####	10.1	Vector类：用户定义的序列类型

####	10.2	Vector类第一版：与Vector2d类兼容

​	通过修改\_\_init\_\_方法让vector可以接受多个参数

​	\_\_repr\_\_方法生成返回内容

####	10.3	协议和鸭子类型

​	在面向对象编程中，协议是非正式的接口，只在文档中定义，在代码中不定义。比如python中的序列协议只要具有\_\_len\_\_和\_\_getitem\_\_两个方法就可以

​	协议是非正式的，没有强制力，如果知道具体的场景，通知只需要实现一个协议的一部分，比如为了支持迭代，只需要实现\_\_getitem\_\_即可。

#### 10.4	Vector类第2版：可切片的序列

​	10.4.1	切片原理

​		slice.indecs方法

​		切片[]中有逗号，\_\_getitem\_\_收到的是元组

​	10.4.2	能处理切片的\_\_getitem\_\_方法

####	10.5	Vector类第3版：动态存取属性

​	通过\_\_getattr\_\_方法查找

​	\_\_getattr\_\_将会顺着继承查找，如果没有就会调用所属类中的\_\_getattr\_\_方法，传入self和属性名称的字符串形式。\_\_getattr\_\_不能用来更新已有的值。只能获取已有值或者创建新属性并赋值。

​	super函数用于动态访问超类的方法

​	\_\_setter\_\_的调用需要使用super()，supper.\_\_setter\_\_(name,value)

​	多数时候如果实现了\_\_getattr\_\_方法，也要定义\_\_setattr\_\_方法，防止对象不一致

#### 10.6	Vector类第4版：散列和快速等值测试

​	functools.reduce(带两个参数的函数表达式，可迭代对象，[初始值])

​	zip函数：zip(*iterables,strict=False)

####	10.7	Vector类第5版：格式化

​	实现format函数

####	10.8	本章小结

#### 10.9	延伸阅读



###	第11章：接口，从协议到抽象类

####	11.1	Python文化中的接口和协议

​	python没有interface关键字，除了抽象基类，每个类都有接口：类实现或者继承的公开属性（方法或数据属性），包括特殊方法

​	接口是实现特定角色的方法集合，也就是协议。协议和继承没有关系。一个类可能会实现多个接口。

####	11.2	Python喜欢序列

​	python数据模型的哲学是尽量支持基本协议

​	虽然没有实现\_\_iter\_\_方法，但python会自动调用\_\_getitem\_\_，从0开始整数索引。没有\_\_contains\_\_方法，in会遍历然后返回结果

####	11.3	使用猴子补丁在运行时实现协议

​	可变序列必须提供\_\_setitem\_\_方法

​	把函数赋值给特殊方法的技术就是猴子补丁，这可以在运行时修改类或者模块而不改动源码，但补丁和程序要非常注意互相耦合。

​	鸭子类型的关键：对象的类型无关紧要，只要实现了特定的协议即可

####	11.4	Alex Martelli的水禽

#### 11.5	定义抽象基类的子类

​	继承基类必须实现基类的所有方法，即使不需要

​	加载模块时不检查抽象方法的实现，只在运行实例化时才检查

####	11.6	标准库中的抽象基类

​	11.6.1	collections.abc 模块中的抽象基类

​		Iterable,Container,Size

​		Sequence,Mapping,Set

​		MappingView

​		Callable,Hashable

​		Iterator

​	11.6.2	抽象基类的数字塔

​		numbers包

​			Number,Complex,Real,Rational,Integral

####	11.7	定义并使用一个抽象基类

​	自定义抽象基类需要继承abc.ABC

​	通过@abc.abstractmethod装饰器来定义抽象方法

​	抽象基类也可以包含具体方法

​	抽象方法可以有实现代码，但子类还是必须要覆盖抽象方法，不过子类可以使用super()函数调用抽象方法，为它添加功能，而不是从头开始

​	检查在实例创建时进行

​	11.7.1	抽象基类句法详解

​		声明抽象基类的最方便方法是继承abc.ABC或者其他抽象类

​		@abstractmethod装饰器

```python
#声明一个接口类继承于一个基类

#1:接口Drawable中没有抽象方法，可以被实例化
class Drawable(metaclass=ABCMeta):

    # @abstractmethod
    def size(self):
        return 'Drawable size'

    # @abstractmethod
    def draw(self, x, y, scale=1.0):
        pass

    def double_draw(self, x, y):
        self.draw(x, y, scale=2.0)

d=Drawable()


#2：接口Drawable中有抽象方法，实例化会报错
class Drawable(metaclass=ABCMeta):

    @abstractmethod
    def size(self):
        return 'Drawable size'

    # @abstractmethod
    def draw(self, x, y, scale=1.0):
        pass

    def double_draw(self, x, y):
        self.draw(x, y, scale=2.0)

d=Drawable()#会报错

#3：继承一个没有抽象方法的接口，不需要覆写实例方法
class Drawable(metaclass=ABCMeta):

    # @abstractmethod
    def size(self):
        return 'Drawable size'

    # @abstractmethod
    def draw(self, x, y, scale=1.0):
        pass

    def double_draw(self, x, y):
        self.draw(x, y, scale=2.0)


class Cicle(Drawable):
    # def size(self):
    #     return 'Cicle size'

    # def draw(self, x, y, scale=1.0):
    #     print(x * scale, y * scale)
    def paint(self):
        pass


c=Cicle()


#4：继承一个有抽象方法的接口类需要覆写抽象方法
from abc import ABCMeta, abstractmethod


class Drawable(metaclass=ABCMeta):

    @abstractmethod
    def size(self):
        return 'Drawable size'

    # @abstractmethod
    def draw(self, x, y, scale=1.0):
        pass

    def double_draw(self, x, y):
        self.draw(x, y, scale=2.0)


class Cicle(Drawable):=====》继承但没有实现抽象方法

    def paint(self):
        pass

c=Cicle() #会报错

##总结
#接口类(抽象类)->类(接口类)->接口类有抽象方法，类需要覆写；没有接口类不需要覆写
```

​	

​	11.7.2	定义Tombola抽象基类的子类

​		需要所有必要方法和可以自己添加新的方法

​	11.7.3	Tombola的虚拟子类

​		白鹅类型的一个基本特征是即使不继承，也有办法把一个类注册为抽象基类的虚拟子类，python不会检查，有问题会在运行时体现

​		虚拟子类保证了我们在写这个类的时候完全符合其父类的所有接口要求

​		在声明类前加@类.register

```python
@Tombola.register
class TomboList(list)

#ToboList是Tombola的虚拟子类，同时扩展list
```

​		类的继承关系在一个特殊的类属性中指定\_\_mro\_\_，即方法解析顺序，按顺序列出其超类，虚拟子类只会列出“真实”的超类，不包含虚拟的超类

####	11.8	Tombola子类的测试方式

​	\_\_subclasses\_\_()返回类的直接子类列表，不包含虚拟子类

​	\_\_abc_registry，一个weakset对象，只有抽象基类才有这个数据属性，是抽象基类注册的虚拟子类的弱引用

####	11.9	Python使用register的方式

​	register可以作为装饰器使用，也可以作为函数使用

​	类.register(虚拟子类)

```python
Tombola.register(Tombolist)
```

####	11.10	鹅的行为有可能像鸭子

​	由于有subclass的存在，可以使得某些鹅有鸭子的样子。不需要显式注册，只需要实现某些方法，就会使某些抽象基类的子类

​	\_\_issubclass__(子类,父类)

​	\_\_isinstance\_\_(子类,父类)

####	11.11	本章小结

​	鸭子类型和白鹅类型的区别

​	鸭子类型：协议、接口、对象三者没有区别。协议风格的接口与继承完全没有关系，实现同一个协议的各个类相互独立。

​	白俄类型：使用抽象基类明确声明接口，而且类可以子类化抽象基类或使用抽象基类注册（无需在继承关系中确立静态的强链接），宣称它实现了某个接口。

####	11.12	延伸阅读



### 第12章：继承的优缺点

####	12.1	子类化内置类型很麻烦

​	内置类型是用C语言编写的，子类不会调用用户定义的类覆盖内置类型的一些方法。

​		比如dict的\_\_init\_\_和\_\_update\_\_方法会覆盖我们在子类中重新覆写的\_\_setitem\_\_方法

​	不要子类化内置类型，用户自己定义的类应该继承collections模块中的类，比如UserDict，UserList和UserString

####	12.2	多重继承和方法解析顺序

​	菱形问题，Python会按照解析顺序来调用。\_\_mro\_\_属性是个元组，从当前类向上。

​	超类中的方法可以直接调用，只需要把实例作为显式参数传入

```python
#D的实例d调用超类C的方法
C.pong(d)
```

​	直接在类上调用实例方法时必须显式传入self

```python
#D.ping方法
def ping(self):
    A.ping(self) #不是super().ping()
    
#super也可以使用，但是要注意级数
```

####	12.3	多重继承的真实运用

####	12.4	处理多重继承

####	12.5	一个现代示例：Django通过视图中的混入

####	12.6	本章小结

####	12.7	延伸阅读



###	第13章：正确重载运算符

####	13.1	运算符重载基础

​	不能重载内置类型的运算符

​	不能新建运算符，只能重载现有的

​	某些运算符不能重载（is and or not）

####	13.2	一元运算符

​	\_\_neg\_\_

​	\_\_pos\_\_

​	\_\_invert\_\_

​	x和+x何时不相等（由于精度换算导致的不相同）

####	13.3	重载向量加法运算符+

​	\_\_add\_\_ 和 \_\_radd\_\_的关系

​	a+b

​		1：a有\_\_add\_\_，返回的值不是None或者NotImplement，调用\_\_add\_\_

​		2：a没有\_\_add\_\_，或者返回值是None或NotImplement，检查b有没有\_\_radd\_\_，如果有，并且返回不是None或者NotImplement，调用b.\_\_radd\_\_(a)

​		3：如果b没有\_\_radd\_\_或者返回None或NotImplement，抛出TypeError	

​	\_\_radd\_\_的通常定义为委托给\_\_add\_\_

####	13.4	重载标量乘法运算符*

​	\_\_mul\_\_ 和 \_\_rmul\_\_

​	中缀运算符@，代表a和b的点积

​		\_\_matmul\_\_，\_\_rmatmul\_\_和\_\_imatmul\_\_

#### 13.5	众多比较运算符

​	\_\_eq\_\_，\_\_ne\_\_，\_\_gt\_\_，\_\_lt\_\_，\_\_ge\_\_，\_\_le\_\_

####	13.6	增量赋值运算符

​	增量赋值不会修改不可变目标，而是新建实例，然后重新绑定

​	\_\_iadd\_\_

​	一个类没有实现\_\_iadd\_\_就地运算符，a+=b的作用和a=a+b，增量运算符只是一个语法糖。只需要有\_\_add\_\_方法，不用额外编写\_\_iadd\_\_，+=就能使用

####	13.7 本章小结

####	13.8 延伸阅读



##	第五部分：控制流程

###	第14章：可迭代的对象、迭代器和生成器

​	迭代器模式，一种惰性获得数据像的方式

​	所有生成器都是迭代器，完全实现了迭代器结构

####	14.1	Sentence类第1版：单词序列

​	序列可以迭代的原因：先检查对象有没有\_\_iter\_\_方法，有就调用，获得一个迭代器。没有的话如果实现了\_\_getitem\_\_方法，Python会创建一个迭代器，尝试从0开始索引获取元素。如果尝试失败，抛出TypeError异常。

​	检查x是否可以迭代使用iter(x)，抛出TypeError表示不可迭代

####	14.2	可迭代的对象与迭代器的对比

​	使用\_\_iter\_\_内置函数可以获取迭代器的对象。如果对象实现了\_\_iter\_\_方法，那么就是可迭代的。实现\_\_getitem\_\_方法，并且参数是从0开始的，那么也是可迭代的

​	Python可以从可迭代对象中获取迭代器

​	使用next函数获取下个元素

```python
s='abc'
it=iter(s)
next(it)
```



​	迭代器只需要实现\_\_next\_\_和\_\_iter\_\_两个方法，调用next后没有办法还原

####	14.3	Sentence类第2版：典型的迭代器

​	可迭代对象一定不能是自身的迭代器，也就是可迭代对象必须实现\_\_iter\_\_方法，但不能实现\_\_next\_\_方法

####	14.4	Sentence类第3版：生成器函数

​	生成器函数yield

​	只要Python函数的定义体中有yield关键字，该函式就是生成器函数。调用生成器函数时，会返回一个生成器对象

####	14.5	Sentence类第4版：惰性实现

​	在\_\_iter\_\_函数的for循环中使用yield来控制for循环的输出

```python
def __iter__(self):
    for match in iter:
        yield match
```



####	14.6	Sentence类第5版：	生成器表达式

####	14.7	何时使用生成器表达式

####	14.8	另一个示例：等差数列生成器

####	14.9	标准库中的生成器函数

​	itertools.count

​	itertools.takewhile

####	14.10	Python3.3 中出现的新句法：yield from

​	yield from有两个使用方式，一个用于协程，还有一个用于代替内侧循环

```python
for iter in iters:
    for it in iter:
        yield it
        
#等同于
for iter in iters:
    yield from iter
```

​	用于生成器函数需要产出另一个生成器生成的值

####	14.11	可迭代的归约函数

​	all，any，max， min，functools.reduce，sum

####	14.12	深入分析iter函数

​	iter有两个参数，可调用对象和哨符。在调用到哨符时抛出stopiteration异常（不产生哨符）

```python
iter(对象，哨符)
```



####	14.13	案例分析：在数据库转换工具中使用生成器

####	14.14	把生成器当成协程

​	.send() 和 \_\_next\_\_的区别

​	.send()可以使得生成器前进到下一个yield语句，还允许使用生成器的客户把数据发给自己，参数会成为函数定义题中yield表达式的值。

​	\_\_next\_\_()方法只允许客户从生成器中提取数据

####	14.15	本章小结

####	14.16	延伸阅读



###	第15章：上下文管理器和else模块

####	15.1	先做这个，再做那个：if语句之外的else块

​	if/else

​	for/else：仅当for运行完毕（没有被break）才运行else

​	while/else：仅当while因为假值退出（没有被break终止）才运行else

​	try/else：try中没有异常抛出才运行else，else中抛出的异常不会由前面的except子句处理

####	15.2	上下文管理器和with模块

​	with语句的目的是简化try/finally模式。

​	上下文管理器协议包含\_\_enter\_\_和\_\_exit\_\_。with开始时会在上下文管理器对象中调用\_\_enter\_\_方法，结束会调用\_\_exit\_\_方法

​	with后面的表达式得到的结果时上下文管理对象，把值绑定到目标变量上（as子句）是在上下文管理器对象上调用\_\_enter\_\_的结果。

​	with模块和函数不同，没有定义新的作用域

​	不管控制流程以哪种方式退出with块，都会在上下文管理器对象上调用\_\_exit\_\_方法，而不是在\_\_enter\_\_方法返回的对象上调用

​	\_\_exit\_\_(self,exc_type,exc_value,traceback) 异常类型、异常值、trackback对象异常位置。正常情况下python调用\_\_exit\_\_方法时传入的是3个none

​	为了告诉解释器异常已经处理，\_\_exit\_\_方法需要return True

####	15.3	contextlib模块中的实用工具

​	redirect_stdout

​	closing

​	suppress

​	@contextmanager 这个装饰器把简单的生成器函数变成上下文管理器，这样就不需要创建类去实现管理器协议了

​	ContextDecorator 这是一个基类，用于定义及鱼类的上下文管理器。

​	ExitStack

####	15.4	使用@contextmanager

​	在使用@contextlib.contextmanager装饰器的生成器中，yield语句的作用是把函数的定义体分成两部分：yield语句前面的所有代码在with块开始时（即解释器调用\_\_enter\_\_方法时）执行，yield语句后面部分的代码在with块结束时（即调用exit方法时）执行

​	在这个装饰器装饰的函数中，yield没有任何迭代作用

​	@contextmanager默认所有的异常都得到了处理，应该压制异常。如果不想压制，需要显式重新抛出异常。这个和\_\_exit\_\_机制相反

####	15.5	本章小结

####	15.6	延伸阅读



###	第16章：协程

​	协程使用yield关键字，一般出现在表达式右边，可以产出值，也可以不产出

​	协程可以从调用方法接收数据，使用.send(datum)方法，而不是next

####	16.1	生成器如何进化成协程

​	生成器可以结合.send()使用，发送的数据会成为生成器函数中yield表达式的值，所以生成器也可以作为协程使用

####	16.2	用作协程的生成器的基本行为

​	使用关键字yield

​	如果只从客户那里接受数据，那么yield关键字右侧没有表达式，产出值为None（隐式指定），客户传入值会直接赋给左侧变量

```python
s=yield
#.send()传入的值会传给s
#yield的返回值是None
```

​	调用函数会的生成器对象

​	实现要调用next来激活，停在第一个yield，或者使用send(None)

​	使用.send传值激活协程时，不能传None以外的值，会导致错误

​	send传值，协程恢复，运行到下一个yield或者终止

​	协程状态通过inspect.getgeneratorstate()来检查，一共四种：

​			GEN_CREATED

​			GEN_RUNNING

​			GEN_SUSPENDED #协程只有处于这个状态时才能.send()

​			GEN_CLOSED

####	16.3	示例：使用协程计算移动平均值

​	使用协程的好处是total和count声明为局部变量即可，无需使用实例属性或闭包再多次调用之间保持上下文

​	.close()可以关闭协程

####	16.4	预激协程的装饰器

​	@functools.wraps装饰器构造一个闭包形式的预激，返回预激后的对象

```python
from functools import wraps

def coroutine(func):
   	@wraps(func)
    def primer(*args,**kwargs):
        gen=func(*args,**kwargs)
        next(gen)
        return gen
   	return primer
```



####	16.5	终止协程和异常处理

​	协程中没有处理的异常会传给next或者send方法（触发协程的对象）

​	generator.throw(exc.type[,exc_value[,trackback]])可以致使生成器暂停在yield表达式处并抛出指定异常。如果生成器处理了抛出的异常（协程中有try/except流程），代码会向前到下一个yield，产出值为generator.throw方法得到的返回值。如果生成器没有处理异常，异常会上冒，传到调用方的上下文中

​	有错误的协程会终止，重新激活再发送值会返回stopiteration。利用这个特性可以使用向协程发送一个哨符，导致错误来终止协程

​	generator.close()可以致使生成器在暂停的yield表达式处抛出GeneratorExit异常。如果生成器没有处理这个异常，或抛出了StopIteration异常，调用方不会报错。如果收到GeneratorExit异常，生成器一定不能产生值，否则会抛出RuntimeError异常。

####	16.6	让协程返回值

​	协程的返回值需要协程正常终止

​	协程最后的return函数会传值给StopIteration异常的一个属性，需要获得可以在except语句中将StopIteration定义为exc，然后通过exc.value获得

```python
#协程中使用return来返回值

try:
    coro_avg.send(None)
except StopIteration as exc:
    result=exc.value #接受return的值
```

####	16.7	使用yield from

​	用于简化for循环中的yield表达式

​	在生成器gen()中使用yield from subgen()将会使得subgen获得控制权，把产出得值传给gen得调用方，即调用方可以直接控制subgen。同时

```python
from cllections import namedtuple

Result=namedtuple('Result','count average')

#子生成器
def averager():
    total=0.0
    count = 0
    average=None
    while True:
        term =yield
        if term is None:
            break
        total+=term
        count+=1
        average=total/count
    return Result(count,average)

#委派生成器：本质是将子生成器包裹起来，通过yield from 来调用，这样会有不少优势
def grouper(result,key):
    while True:
        results[key] = yield from averager()
        
#客户端代码，即调用方
def main(data):
    results={}
    for key, values in data.items():
        group=grouper(result,key)
        next(group)
        for value in values:
            group.send(value)#传入得值会通过averager中的term=yield这行，grouper不知道传什么值
        group.send(None)
	print(results)
```



####	16.8	yield from 的意义

​	子生成器产出的值都直接传给委派生成器的调用方

​	使用send()方法发给委派生成器的值直接传给了子生成器。如果发送的值是None，会那么会调用子生成器的\_\_next\_\_方法。如果发送的值不是None，那么会调用子生成器的send方法。如果调用的方法抛出StopIteration异常，那么委派生成器恢复运行。任何其他异常都会上冒，传给委派生成器。

​	生成器退出时，生成器（或子生成器）中的return expr表达式会出发StopIteration（expr）异常

​	yield from表达式的值是子生成器终止时传给StopIteration异常的第一个参数

​	参考：[python协程系列（三）——yield from原理详解_LoveMIss-Y的博客-CSDN博客](https://blog.csdn.net/qq_27825451/article/details/85244237)

####	16.9	使用案例：使用协程做离散事件仿真

​	16.9.1	离散事件仿真简介

​	16.9.2	出租车队运营仿真

####	16.10	本章小结

####	16.11	延伸阅读



###	第17章：使用future处理并发

####	17.1	示例：网络下载的三种风格

​	17.1.1	依序下载脚本

​	17.1.2	使用concurrent.futures模块下载

```python
from concurrent import futures
MAX_WORKERS=20

def download_one(cc):
    image=get_flag(cc)
    show(cc)
    save_flage(image,cc.lower()+'.gif')
    return cc

def download_many(cc_list):
    workers=min(MAX_WORKERS,len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res=executor.map(download_one,sorted(cc_list))
        
    return len(list(res))
```



​	17.1.3	future在哪里

####	17.2	阻塞型I/O和GIL

####	17.3	使用concurrent.futures模块启动进程

#### 17.4	实验Executor.map方法

​	futures.ThreadPoolExecutor(wokers) as executor:

​	futures.ProcessPoolExecutor() as executor:

​	Executor.map返回结果的顺序和调用顺序一致。即使后面的任务先完成了，也会在前面的任务返回后再返回，只是计算会被提前。如果需要先出结果就先返回，使用executor.submit 和 futures.as_completed这个组合。

####	17.5	显式下载进度并处理错误

​	17.5.1	flags系列示例处理错误的方式

​	17.5.2	使用futures.as_completed函数

​	17.5.3	线程和多进程的替代方案

####	17.6	本章小结

####	17.7	延伸阅读



###	第18章：使用asyncio包处理并发

​	threading包提供线程相关支持

​	threading.Thread

​	Python没有提供终止线程的API，若想关闭线程，必须给线程发送消息

####	18.1	线程与协程对比

​	18.1.1	asyuncio.Future：故意不阻塞

​	18.1.2	从future、任务和协程中产出

####	18.2	使用asyncio和aiohttp包下载

####	18.3	避免阻塞型调用

####	18.4	改进asyncio下载脚本

​	18.4.1	使用asyncio.as_completed函数

​	18.4.2	使用Executor对象，防止阻塞事件循环

####	18.5	从回调到future和协程

####	18.6	使用asyncio包编写服务器

​	18.6.1	使用asyncio包编写TCP服务器

​	18.6.2	使用aiohttp包编写Web服务器

​	18.6.3	更好地支持并发的智能客户端

####	18.7	本章小结

####	18.8	延伸阅读



## 第六部分：元编程

### 第19章：动态属性和特性

####	19.1	使用动态属性转换数据

​	19.1.1	使用动态属性访问JSON类数据

​	19.1.2	处理无效属性名

​	19.1.3	使用\_\_new\_\_方法以灵活的方式创建对象

​	19.1.4	使用shelve模块调整OSCON数据源的结构

​	19.1.5	使用特性获取链接的记录

####	19.2	使用特性验证属性

​	19.2.1	LineItem类第1版：表示订单中商品的类

​	19.2.2	LineItem类第2版：能验证值的特性

####	19.3	特性全解析

​	19.3.1	特性会覆盖实例属性

​	19.3.2	特性的文档

####	19.4	定义一个特性工厂函数

####	19.5	处理属性删除的操作

####	19.6	处理属性的重要属性和函数

​	19.6.1	影响属性处理方式特殊属性

​	19.6.2	处理属性的内置函数

​	19.6.3	处理属性的特殊方式

####	19.7	本章小结

####	19.8	延伸阅读



###	第20章：属性描述符

####	20.1	描述符示例：验证属性

​	20.1.1	LineItem类第3版：一个简单的描述符

​	20.1.2	LineItem类第4版：自动获取储存属性的名称

​	20.1.3	LineItem类第5版：一种新型描述符

####	20.2	覆盖型与非覆盖型描述符对比

​	20.2.1	覆盖型描述符

​	20.2.2	没有\_\_get\_\_方法的覆盖型描述符

​	20.2.3	非覆盖型描述符

​	20.2.4	在类中覆盖描述符

####	20.3	方法是描述符

####	20.4 描述符用法建议

####	20.5	描述符的文档字符串和覆盖删除操作

####	20.6	本章小结

####	20.7	延伸阅读



###	第21章：类元编程

####	21.1	类工厂函数

####	21.2	定制描述符的类装饰器

####	21.3	导入时和运行时的比较

####	21.4	元类基础知识

####	21.5	定制描述符的元类

####	21.6	元类的特殊方法\_\_prepare\_\_

####	21.7	类作为对象

####	21.8	本章小结

####	21.9	延伸阅读



