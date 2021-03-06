## 欢迎来到Stage_1/front部分
### 名词解释
* 计算
* 计算模型
* 序列
* 有穷
###### 计算
借助某种工具，遵照一定规则，以明确而机械的形式进行
###### 计算模型
你可以理解为，将解决一个问题而经历的所有步骤的总结和抽象，就是这个解决这个问题的计算模型。这个描述并不精确，随着你学习的深入，
你会慢慢理解这个词汇。后续学习中也将进一步解释这个词汇。
###### 序列
有序的一个队列
###### 有穷
一个描述性词语，意为有结束的，可以结束的，有限的，有结尾的。
### 什么是算法?算法有哪些特性?
所谓的算法，即在特定的计算模型下，旨在解决特定问题的指令序列
* 输入
* 输出
* 正确性
* 确定性
* 可行性
* 有穷性
###### 输入
待处理的信息
###### 输出
处理后的信息
###### 正确性
的确可以解决指定的问题
###### 确定性
任意算法都应该可以被描述成一个由 基本操作 组成的序列
###### 可行性
每一基本操作都可以实现，并且在 常数时间 内完成
###### 有穷性
对于任何输入，经过 有穷 次基本操作，都可以得到输出

### 如何评判一个算法是否为好的算法?
评判一个算法的标准有很多，大体可以归纳为以下几点：
* 正确
* 效率
* 健壮
* 可读
###### 正确
符合语法，能够编译且运行，能够正确处理 简单的、大规模的、一般性的、退化的和任意合法的输入
###### 效率
速度尽可能的快，消耗的资源尽可能的少。有时候二者冲突，应根据需求情况来取舍
###### 健壮
能够辨别不合法的输入并进行适当的处理，而不至于非正常退出
###### 可读
结构化的设计，符合规范的命名，详尽的注释
###### 理解就是度量。如果你不能度量它，你就不能提升它。 ------Lord Kelvin

### 衡量算法的标准
我们将一个算法的时间成本和空间成本均记为计算成本，而计算成本的高低便是我们衡量算法的标准之一。但是即使是同一问题A的同一规模n的不同实例，也有可能出现不同的计算成本，因此，我们通常在规模为n的所有实例中，只关注成本最高者(最坏情况)和平均成本(平均情况)。

