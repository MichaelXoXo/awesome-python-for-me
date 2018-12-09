# Argparse
![](https://ws1.sinaimg.cn/mw690/6d9475f6ly1fy0x6l6n0hj20hs0a0403.jpg)

argparse 是 Python 内置的一个用于命令项选项与参数解析的模块。Python 也有第三方的库可用于命令行解析，而且功能也更加强大，比如 [docopt](http://docopt.org/)，[Click](https://click.palletsprojects.com/en/5.x/)

主要有三个步骤：

- 创建 ArgumentParser() 对象
- 调用 add_argument() 方法添加参数
- 使用 parse_args() 解析添加的参数

## 参数说明

### add_argument

```python
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required]
[, help][, metavar][, dest])
```

每个参数解释如下:

- name or flags - 选项字符串的名字或者列表，例如 foo 或者 -f, --foo。
- action - 命令行遇到参数时的动作，默认值是 store。
    - store_const，表示赋值为const；
    - append，将遇到的值存储成列表，也就是如果参数重复则会保存多个值;
    - append_const，将参数规范中定义的一个值保存到一个列表；
    - count，存储遇到的次数；此外，也可以继承 argparse.Action 自定义参数解析；
- nargs - 应该读取的命令行参数个数，可以是具体的数字，或者是?号，当不指定值时对于 Positional argument 使用 default，对于 Optional argument 使用 const；或者是 * 号，表示 0 或多个参数；或者是 + 号表示 1 或多个参数。
- const - 一个在 action 和 nargs 选项所需的常量值。
- default - 不指定参数时的默认值。
- type - 命令行参数应该被转换成的类型。
- choices - 参数可允许的值的一个容器。
- required - 可选参数是否可以省略 (仅针对可选参数)。
- help - 参数的帮助信息，当指定为 argparse.SUPPRESS 时表示不显示该参数的帮助信息.
- metavar - 在 usage 说明中的参数名称，对于必选参数默认就是参数名称（上面的 name or flags），对于可选参数默认是全大写的参数名称.
- dest - parse_args() 方法返回的对象所添加的属性的名称。默认情况下，对于可选参数选取最长的名称，中划线转换为下划线.

## 官方示例

```python
# 创建了 ArgumentParser 对象，该对象具有解析命令行转为 Python 数据类型的全部信息
parser = argparse.ArgumentParser(description='Process some integers.')

# 增加参数
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
parser.add_argument('--foo', action='store_true')
parser.add_argument('--bar', action='store_false')

# 调用 parse_args() 会返回对象的两个属性，integers 和 accumulate。 integers 属性是一个列表
# 如果在命令行中指定了 --sum，例如 python a.py 1 --sum ，则 accumulate 属性将是 sum() 函数，
# 如果没有加上 --sum，例如 python a.py 1，则 accumulate 为 max() 函数

>>> parser.parse_args(['--sum', '7', '-1', '42'])
Namespace(accumulate=<built-in function sum>, integers=[7, -1, 42])

```

这里的 `store_const` 可以这么理解，它对应的属性是可以手动赋值的，比如这里的 `accumulate`，该属性值是自动获取：
- 如果参数中使用了 `--sum`，那么后面不赋值，accumulate 也会根据取 const 指定的值取值；
- 如果参数中没有出现 `--sum`，那么这个可选参数会去 `default` 指定的值，如果不指定默认值，会取值 `None`

这里的 `store_false` 可以这么理解，它对应的属性也是不可以赋值的，是自动获取的：
- 命令行使用了 `--foo`，这个属性就为 `True`，否则为 `False`
- 命令行使用了 `--bar`，这个属性就为 `False`，否则就为 `True`

## 互斥示例

```python
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
```

参考：

- [极客学院-argparse](http://wiki.jikexueyuan.com/project/explore-python/Standard-Modules/argparse.html)
- [官宣-Python argparse](https://docs.python.org/3/library/argparse.html)
- [知乎-Python-argparse-命令行与参数解析](https://zhuanlan.zhihu.com/p/34395749)
- [简书-python argparse用法总结](https://www.jianshu.com/p/fef2d215b91d) 理解了 store 和 互斥参数