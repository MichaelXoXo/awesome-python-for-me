# awesome-python-for-me

## Python 好资源

- [awesome-python-cn](https://github.com/jobbole/awesome-python-cn)
- [taizilongxu/interview_python](https://github.com/taizilongxu/interview_python)
- [Migrating to Python 3 with pleasure 愉快地迁移到 Python 3](https://github.com/arogozhnikov/python3_with_pleasure)
- [Learn Python Programming-英文python综合教程-推荐](https://www.programiz.com/python-programming)

## 命令行工具

### ipython

- [第 1 章　IPython：超越 Python](http://www.ituring.com.cn/book/tupubarticle/19702#)

### pylint

- [pylint在项目中的使用](https://www.jianshu.com/p/c0bd637f706d)
- [pylint的配置和使用](https://blog.csdn.net/u013687821/article/details/51127070)
- [为什么Pylint既有用又不能用，以及如何使用它](https://python.freelycode.com/contribution/detail/491)
- [如何使用 Pylint 来规范 Python 代码风格](https://www.ibm.com/developerworks/cn/linux/l-cn-pylint/index.html)

## Python基础知识点

### Python打包知识点
- [关于python中的setup.py](https://lingxiankong.github.io/2013-12-23-python-setup.html)-孔令贤

### PEP

- [PEP Index](https://www.python.org/dev/peps/)
- [Python中10个必读的PEP提案](https://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650368690&idx=1&sn=4391ec8d8a1fe0a7102d38acfb23e592&chksm=be9cd1e689eb58f0566336c73b641c46efdf73da146c41477392dc67e1c005d60931f24f0bb9&mpshare=1&scene=1&srcid=0807piOiQrU4cs7hO0nw35Vg#rd)

### Python面向对象

- [一篇文章搞懂Python中的面向对象编程](http://yangcongchufang.com/%E9%AB%98%E7%BA%A7python%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/python-object-class.html)

### module与package的区别

- [python中的模块、库、包有什么区别？](https://www.zhihu.com/question/30082392)

### 浅拷贝、深拷贝的区别
- [一篇文章读懂Python赋值与拷贝](https://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650368292&idx=2&sn=99edf6dd8d4204b741b3ce148030b486&chksm=be9cd27089eb5b66b9fe2cbc912ba39f5ce75bf549269e94cfc14b8425f5faaff94032d7967e&scene=0#rd)

### Python annotations的用法
- [python3 -> 函数注释 Function Annotations](https://blog.csdn.net/feelang/article/details/38226591)
- [What does -> mean in Python function definitions?](https://stackoverflow.com/questions/14379753/what-does-mean-in-python-function-definitions)
- [Function Annotations](https://www.python.org/dev/peps/pep-3107/)


### Python常量设计

- [廖雪峰-使用枚举类](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143191235886950998592cd3e426e91687cdae696e64b000)
- [设计不可更改的python常量类](http://xiaorui.cc/2017/11/21/%E8%AE%BE%E8%AE%A1%E4%B8%8D%E5%8F%AF%E6%9B%B4%E6%94%B9%E7%9A%84python%E5%B8%B8%E9%87%8F%E7%B1%BB/)
- [Python 中的枚举类型](http://python.jobbole.com/84112/)
- [enum — Support for enumerations](https://docs.python.org/3/library/enum.html)
- [How can I represent an 'Enum' in Python?](https://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python)
- [在Python里如何用枚举类型?](https://taizilongxu.gitbooks.io/stackoverflow-about-python/content/7/README.html)

### Python闭包和装饰器

> 装饰器让你在一个函数的前后去执行代码。

`@wraps`接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。

- [PYTHON修饰器的函数式编程](https://coolshell.cn/articles/11265.html)
- [装饰器](https://funhacks.net/explore-python/Functional/decorator.html)
- [gitbook-装饰器](https://eastlakeside.gitbooks.io/interpy-zh/content/decorators/func_as_argument.html)

### Python 编码问题

- [Python 编码为什么那么蛋疼](http://python.jobbole.com/88264/)
> 我们用编辑器打开的文本，看到的一个个字符，最终保存在磁盘的时候都是以二进制字节序列形式存起来的。那么从字符到字节的转换过程就叫做编码（encode），反过来叫做解码（decode），两者是一个可逆的过程。编码是为了存储传输，解码是为了方便显示阅读。
str 本质上其实是一串二进制数据，而 unicode 是字符（符号），编码（encode）就是把字符（符号）转换为 二进制数据的过程，因此 unicode 到 str 的转换要用 encode 方法，反过来就是用 decode 方法

## Python开发习惯
- [ python-web-guide](http://python-web-guide.readthedocs.io/zh/latest/codingstyle/codingstyle.html)
- [ Google 开源项目风格指南](http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/contents/)

## Python测试

### pytest

- [Python 各种测试框架简介（四）：pytest](https://my.oschina.net/lionets/blog/269892)
- [【Pytest】python单元测试框架pytest简介](https://blog.csdn.net/liuchunming033/article/details/46501653)

### mock

- [Python mock 使用心得](https://www.linuxzen.com/python-mock-shi-yong-xin-de.html)

## 开发环境相关

### python2与python3共存
安装完成之后，在CMD里面直接输入python会启动Python2，而使用activate py3（py3即之前Python3安装目录文件夹的名字）命令之后，再使用python即可切换至Python3，如下图所示。使用activate py3命令之后，在命令行前面会出现一个[py3]标记，此时使用任何的python命令都是在Python3下进行的。使用deactivate命令可取消激活Python3。
- http://blog.csdn.net/Infin1te/article/details/50445217
- http://www.cnblogs.com/meelo/p/6034970.html

### linux下，怎么查看默认python的路径？怎么修改默认的python版本？

- [LINUX CENTOS7下安装PYTHON](https://www.cnblogs.com/lclq/p/5620196.html)
- [Find where python is installed (if it isn't default dir)](https://stackoverflow.com/questions/6767283/find-where-python-is-installed-if-it-isnt-default-dir)

## Python常用技巧
- [requests包的编码使用问题](https://github.com/requests/requests/issues/1604)

### Python执行命令行
- [Python执行系统命令的方法](http://xstarcd.github.io/wiki/Python/python_system_command.html)

##参考：
- [stackoverflow about python](https://taizilongxu.gitbooks.io/stackoverflow-about-python/content/76/README.html)
- [Python 使用 pip 升级所有包](https://blog.csdn.net/kl28978113/article/details/77980778)


## Python好文

- [Python向来以慢著称，为啥Instagram却唯独钟爱它？](http://www.infoq.com/cn/articles/instagram-pycon-2017)
- [利强的博客--聊聊 python 的 jit](http://liuliqiang.info/post/173/)
- [CoderZH-Python天天美味(总)](http://www.cnblogs.com/coderzh/archive/2008/07/08/pythoncookbook.html)
- [教你阅读Python开源项目代码](https://zhuanlan.zhihu.com/p/22275595?refer=python-cn)

## Python好问题
- [你用 Python 写过哪些有趣的脚本？](https://www.zhihu.com/question/28661987)

###  编程基本功
+ [如何系统地自学 Python？](https://www.zhihu.com/question/29138020)
+ [应该学习最新版本的 Python 3 还是旧版本的 Python 2？](https://www.zhihu.com/question/24549965)
+ [初学 Python，有哪些 Pythonic 的源码推荐阅读？](https://www.zhihu.com/question/20336475)
+ [你是如何自学 Python 的？](https://www.zhihu.com/question/20702054)
+ [如何处理 Python 入门难以进步的现象？](https://www.zhihu.com/question/27969262)
+ [SF专栏-python数据结构](https://segmentfault.com/blog/wzhvictor)

###  python工具
+ [为什么说 virtualenv、fabric 和 pip 是 pythoneer 的三大神器？](https://www.zhihu.com/question/19717006)
+ [有哪些值得推荐的 Python 开发工具？](https://www.zhihu.com/question/20381207)
+ [Mac-打造自己的Python编码环境?](http://xymlife.com/2016/02/07/%E6%89%93%E9%80%A0%E8%87%AA%E5%B7%B1%E7%9A%84Python%E7%BC%96%E7%A0%81%E7%8E%AF%E5%A2%83/)
- [知乎-还在用 ppt？教你用Python Jupyter notebook 制作代码分享 ppt ](https://zhuanlan.zhihu.com/p/47418033)

###  学习资料总结
+ [Python 有哪些好的学习资料或者博客？](https://www.zhihu.com/question/34907211)

### 数据挖掘总结
+ [如何系统地学习Python 中 matplotlib, numpy, scipy, pandas？](https://www.zhihu.com/question/37180159)
+ [CSDN-python机器学习博客](http://blog.csdn.net/lsldd/article/category/2709209)
+ [业余时间如何学数据分析？](https://www.zhihu.com/question/22119753)
+ [学习机器学习有哪些好工具推荐？](https://www.zhihu.com/question/20472776)

### 数据分析实战
+ [coursera上有哪些值得学习的Python,数据分析的课程？](https://www.zhihu.com/question/36254617#answer-25104011)
+ [你用 Python 做过什么有趣的数据挖掘/分析项目？](https://www.zhihu.com/question/28975391/answer/69556795)

### python技巧型
+ [一行 Python 能实现什么丧心病狂的功能？](https://www.zhihu.com/question/37046157)
+ [如何写出pythonic代码-让你的Python代码更加pythonic](http://wuzhiwei.net/be_pythonic/)
+ [初学 Python，有哪些 Pythonic 的源码推荐阅？](https://www.zhihu.com/question/20336475/answer/16093609)

### python-web实战
+ [超小团队选择django还是flask？](https://www.zhihu.com/question/33538127)
+ [关于python Django与Flask学习的一些疑惑？](https://www.zhihu.com/question/36625971)
+ [v2ex-python 开发 Web 的正确姿势是什么](http://www.v2ex.com/t/244426)

### python面试题
+ [github-关于Python的面试题-taizilongxu/interview_python](https://github.com/taizilongxu/interview_python)
+ [CSDN-Python面试题汇总](http://blog.csdn.net/jerry_1126/article/details/44023949)
+ [Blog-Python面试题汇总](http://www.selfrebuild.net/2015/08/25/Python%E9%9D%A2%E8%AF%95%E9%A2%98%E6%B1%87%E6%80%BB/)
+ [Python面试题笔试题:](http://www.mianwww.com/html/category/it-interview/python)
+ [聊python面试这件事儿](http://dongweiming.github.io/blog/archives/liao-liao-pythonmian-shi-zhe-jian-shi-er/)
+ [Python工程师面试题集合](http://blog.csdn.net/u013510614/article/details/50509387)


## Python好教程

- [explore-python-Python之旅](http://funhacks.net/explore-python/)
- [Python进阶](https://eastlakeside.gitbooks.io/interpy-zh/content/)
- [Python 101](http://python101.pythonlibrary.org/index.html)
- [梦中谍影-blog](https://gtcsq.readthedocs.io/en/latest/)
- [Python高手之路（第3版）](https://www.kancloud.cn/epubit/python3/301709)
- [Python 算法与数据结构视频教程](https://python-data-structures-and-algorithms.readthedocs.io/zh/latest/)

## 有用的模块

收集写 python 项目时发现的好用的模块

- [argparse 模块](https://github.com/Michael728/python-useful-modules/tree/master/learn_argparse) 标准库，获取命令行参数的模块

## 有趣的项目

Collect favorite python projects 🍔

来收藏Python相关好项目

- [requests](https://github.com/requests/requests)：调API时喜欢用的包，有人对其源码写了[阅读笔记](https://github.com/wangshunping/read_requests)
- [wagtail-CMS系统](https://wagtail.io/developers/) Django 系统
- [值得看的Python的开源项目有哪些？](https://www.zhihu.com/question/19840137) 好问题
- [taizilongxu/interview_python](https://github.com/taizilongxu/interview_python) 求职

## 参考

- [jobbole/awesome-python-cn](https://github.com/jobbole/awesome-python-cn)
- [vinta/awesome-python](https://github.com/vinta/awesome-python)
