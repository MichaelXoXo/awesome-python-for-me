# coding:utf-8
import argparse
import sys

"""
学习内置模块 argparse 用法
- http://wiki.jikexueyuan.com/project/explore-python/Standard-Modules/argparse.html
- https://zhuanlan.zhihu.com/p/34395749
"""


def cmd():
    # 创建 ArgumentParser() 对象
    parser = argparse.ArgumentParser(description='Process some integers.', epilog='Information end')

    # 增加参数
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    parser.add_argument('--foo', action='store_true')
    parser.add_argument('--bar', action='store_false')
    args = parser.parse_args()
    print("parser.parse_args=args, args :", args, type(args))

    # 所有的参数 组成了一个字典 args.__dict__ 可以显示全部参数
    d = args.__dict__
    print(d)
    # 位置参数可以通过 对象.属性 的方式访问, 值存放在 list 中
    print("args.accumulate: {}".format(args.accumulate))
    for k, v in d.items():
        print('{}={}'.format(k, v))

    print(args.accumulate(args.integers))


if __name__ == '__main__':
    print(sys.modules.keys())
    cmd()
