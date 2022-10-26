# 一、数据结构接口

* 数据结构是存储数据的一种方式，算法支持数据操作

* 支持的操作集合称为接口（**API**或**ADT**）

* 接口是声明：支持哪些操作（问题）

* 数据结构是表示（**representation**）：操作如何被支持（解法）

* 本课中，两个主要接口：序列（**Sequence**）和集合（**Set**）

# 二、序列（Sequence）接口（L02，L07）

* 维护项目序列

* 例如：($x_0,x_1,x_2,...,x_{n-1}$)

* 使用n来表示存在数据结构中的项目数

* 支持序列操作

| 类型            | 方法                                                                                                      | 描述                                                                                     |
|:------------- |:------------------------------------------------------------------------------------------------------- |:-------------------------------------------------------------------------------------- |
| 容器（container） | build(X)<br>len()                                                                                       | 给定一个可迭代的X，通过X中的项目构建序列<br>返回存储序列的数量                                                     |
| 静态（static）    | iter_seq()<br>get_at(i)<br>set_at(i, x)                                                                 | 以序列顺序挨个返回其中存储的项目<br>返回$i^{th}$项目<br>用x取代$i^{th}$项目                                     |
| 动态（dynamic）   | insert_at(i, x)<br>delete_at(i)<br>insert_first(x)<br>delete_first()<br>insert_last(x)<br>delete_last() | 添加x作为$i^{th}$项目<br>移除并返回$i^{th}$项目<br>添加x作为首个项目<br>移除并返回首个项目<br>添加x作为最后项目<br>移除并返回最后项目 |

* 特殊情形接口

| 类型        | 方法                            |
| --------- | ----------------------------- |
| **stack** | insert_last(x)和delete_last()  |
| **queue** | insert_last(x)和delete_first() |

# 三、集合（Set）接口（L03-L08）

* 序列与外在顺序有关，集合与内在顺序有关

* 保存一组有唯一键的项目（例如项目x有key：x.key）

* Set还是multi-Set，我们限制为唯一键

* 通常我们让项目的key是项目本身，但也可能想比key存储更多的信息

* 支持的集合操作：

| 类型            | 方法                                                                     |                                                                              |
| ------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 容器（container） | build(x)<br>len()                                                      | 给定一个可迭代的X，通过X中的项目构建集合<br>返回存储项目的数量                                           |
| 静态（static）    | find(k)                                                                | 返回键为key的项目                                                                   |
| 动态（dynamic）   | insert(x)<br>delete(k)                                                 | 添加x到集合（如果已经存在，取代值为x.key的项目）<br>移除并返回键为key的项目                                 |
| 顺序（order）     | iter_ord()<br>find_min()<br>find_max()<br>find_next(k)<br>find_prev(k) | 以键值顺序挨个返回存储的项目<br>返回拥有最小键的项目<br>返回拥有最大键的项目<br>返回比k大的最小键项目<br>返回比k小的最大键项目<br> |

* 特殊情形接口：
  
  | 类型            | 描述        |
  | ------------- | --------- |
  | 字典（directory） | 没有顺序操作的集合 |

# 四、数组序列

* 数组利于静态操作。get_at(i)和set_at(i, x)为$\theta(1)$时间。

* 但并不利于动态操作

* 为了连续性，我们保持不变性：数组是满的

* 插入、删除项目需要：
  
  重新分配数组、移动更改项目后的所有项目
  
  <div>
  
  <table>
      <tr>    
          <td rowspan=3>数据结构</td>
          <td colspan=5 align="center">操作，最坏情形O</td>    
      </tr>
      <tr>
          <td>容器（container）</td>
          <td>静态（static）</td>
          <td colspan=3 align="center">动态（dynamic）</td>
      </tr>
      <tr>
          <td>build(x)</td>
          <td>get_at(i)<br>set_at(i, x)</td>
          <td>insert_first(x)<br>delete_first()</td>
          <td>insert_last(x)<br>delete_last()</td>
          <td>insert_at(i, x)<br>delete_at(i)</td>
      </tr>
      <tr>
          <td>数组</td>
          <td>n</td>
          <td>1</td>
          <td>n</td>
          <td>n</td>
          <td>n</td>
      </tr>
  </table>
  </div>

# 五、链表序列

* 指针数据结构（这跟Python的list无关）

* 每个项目存储在一个节点中，节点包含指向序列下个节点的指针

* 每个节点有两个属性：node.item和node.next

* 可以通过重新链接指针来操纵节点

* 保存指向序列首个节点的指针（称为head）

* 首部的插入、删除为$\theta(1)$时间

* 有效地在尾部插入、删除也是可行的，见PS1

* get_at(i)和set_at(i, x)每个花费$\mathcal{O}(n)$时间

* 我们可以在两方面做到最好么？是的

<div>
<table>
    <tr>    
        <td rowspan=3>数据结构</td>
        <td colspan=5 align="center">操作，最坏情形O</td>    
    </tr>
    <tr>
        <td>容器（container）</td>
        <td>静态（static）</td>
        <td colspan=3 align="center">动态（dynamic）</td>
    </tr>
    <tr>
        <td>build(x)</td>
        <td>get_at(i)<br>set_at(i, x)</td>
        <td>insert_first(x)<br>delete_first()</td>
        <td>insert_last(x)<br>delete_last()</td>
        <td>insert_at(i, x)<br>delete_at(i)</td>
    </tr>
    <tr>
        <td>链表</td>
        <td>n</td>
        <td>n</td>
        <td>1</td>
        <td>n</td>
        <td>n</td>
    </tr>
</table>
</div>

# 六、动态数组序列

* 制造一个数组：有效地进行last动态操作

* python list是一个动态数组

* 分配额外的空间，因此重新分配不会在每次动态操作时发生

* 填充比率：0<=r<=1，项目/空间的比率

* 当数组满了时（r=1），分配$\theta(n)$额外空间到尾部，填充比率$r_i$变为1/2

* 在下次再分配前，将必须插入$\theta(n)$个项目

* 触发再分配的单个操作花费$\theta(n)$时间

* $\theta(n)$操作花费$\theta(n)$时间

* 因此平均起来，每个操作花费$\theta(1)$时间

## 摊还分析

* 分摊消耗到多个操作上

* 每个操作的摊还消耗为T(n)，那么k个操作消耗<=kT(n)

* “T(n)摊还时间”大体意味着多个操作时间为T(n)

* 动态数组插入花费$\theta(1)$摊还时间

* 更多摊还分析技术在6.046

## 动态数组删除

* 尾部删除，$\theta(1)$时间

* 可能空间会严重浪费。想让数据结构尺寸保持在$\theta(n)$

* 如果非常空，resize r=1。交替插入、删除可能不好

* 当$r<r_d$，resize数组

* $\theta(n)$个容易的操作（时间复杂度低）必须在下次昂贵的resize前完成

* 限制额外的空间使用

* 动态数组仅支持动态last操作以$\theta(1)$时间

* python list的append和pop操作是摊还$\mathcal{O}(1)$时间，其它操作是$\mathcal{O}(n)$

* 首部有效地插入/删除也是可能的，见PS1

<div>
<table>
    <tr>    
        <td rowspan=3>数据结构</td>
        <td colspan=5 align="center">操作，最坏情形O</td>    
    </tr>
    <tr>
        <td>容器（container）</td>
        <td>静态（static）</td>
        <td colspan=3 align="center">动态（dynamic）</td>
    </tr>
    <tr>
        <td>build(x)</td>
        <td>get_at(i)<br>set_at(i, x)</td>
        <td>insert_first(x)<br>delete_first()</td>
        <td>insert_last(x)<br>delete_last()</td>
        <td>insert_at(i, x)<br>delete_at(i)</td>
    </tr>
    <tr>
        <td>数组</td>
        <td>n</td>
        <td>1</td>
        <td>n</td>
        <td>n</td>
        <td>n</td>
    </tr>
    <tr>
        <td>链表</td>
        <td>n</td>
        <td>n</td>
        <td>1</td>
        <td>n</td>
        <td>n</td>
    </tr>
    <tr>
        <td>动态数组</td>
        <td>n</td>
        <td>1</td>
        <td>n</td>
        <td>1(摊还时间)</td>
        <td>n</td>
    </tr>
</table>
</div>