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

# 七、recitation

## 序列接口（Sequence Interface）（L02，L07）

序列以某种外在顺序有一批项目，每个存储的项目在序列中有一个排名，包含首部、尾部项目。所谓外在的，我们意味着：首个项目是”first“，并非因为项目是什么，而是因为外部方把它放到了那。序列是栈和队列的概括，它支持序列操作的子集。

| 类型            | 方法                                                                                                      | 描述                                                                                     |
|:------------- |:------------------------------------------------------------------------------------------------------- |:-------------------------------------------------------------------------------------- |
| 容器（container） | build(X)<br>len()                                                                                       | 给定一个可迭代的X，通过X中的项目构建序列<br>返回存储序列的数量                                                     |
| 静态（static）    | iter_seq()<br>get_at(i)<br>set_at(i, x)                                                                 | 以序列顺序挨个返回其中存储的项目<br>返回$i^{th}$项目<br>用x取代$i^{th}$项目                                     |
| 动态（dynamic）   | insert_at(i, x)<br>delete_at(i)<br>insert_first(x)<br>delete_first()<br>insert_last(x)<br>delete_last() | 添加x作为$i^{th}$项目<br>移除并返回$i^{th}$项目<br>添加x作为首个项目<br>移除并返回首个项目<br>添加x作为最后项目<br>移除并返回最后项目 |

注意：在更改项目后，insert_/delete_操作改变了所有项目的排名

## 集合接口（Set Interface）（L03-L08）

相对而言，集合基于内在属性（包括项目是什么，通常基于唯一键，x.key，与每个项目x关联）有一批项目。集合是字典（dictionary）和其它内在查询数据库的概括。

| 类型            | 方法                                                                     |                                                                              |
| ------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 容器（container） | build(x)<br>len()                                                      | 给定一个可迭代的X，通过X中的项目构建集合<br>返回存储项目的数量                                           |
| 静态（static）    | find(k)                                                                | 返回键为key的项目                                                                   |
| 动态（dynamic）   | insert(x)<br>delete(k)                                                 | 添加x到集合（如果已经存在，取代值为x.key的项目）<br>移除并返回键为key的项目                                 |
| 顺序（order）     | iter_ord()<br>find_min()<br>find_max()<br>find_next(k)<br>find_prev(k) | 以键值顺序挨个返回存储的项目<br>返回拥有最小键的项目<br>返回拥有最大键的项目<br>返回比k大的最小键项目<br>返回比k小的最大键项目<br> |

注意：如果没有合适的项目存在，find操作返回None。

## 序列实现（Sequence implementations）

我们将讨论三个数据结构来实现序列接口。在problemSet1，你将拓展链表（linkedList）和动态数组（dynamic array）来让首部、尾部动态操作花费$\mathcal{O}(1)$时间复杂度。注意：这些数据结构没有一个能支持：在任意索引处动态操作为次线性（sub-linear）时间。我们将在lecture7学习如何提升这个操作。

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

## 数组序列（Array Sequence）

计算机内存是有限的资源。现代计算机，多进程共享相同主存，因此操作系统将为每个活跃（active）进程分配一块固定的内存地址。分配内存的数量取决于进程需要和可用的空闲内存。举例，当计算机程序发出请求，存储一个变量，程序必须告诉操作系统需要多少内存（多少比特位）来存它。为了满足该请求，操作系统将在进程分配的内存地址空间中，找到可用内存，并为该目的预留它（分配它）直到它不再被需要。内存管理和分配是一个许多高级语言（包括python）抽象的细节，但要知道，无论何时你让Python存储某些东西，python会向操作系统发出请求（幕后），得到固定数量内存来存它。

现在假设计算机程序想存储两个数组，每个存储10个64位的字。程序为两块内存发出单独请求（每个640位），操作系统满足请求。举例，保留进程分配地址空间的前10字给第一个数组A，第二个10字地址空间给第二个数组B。现在假设随着计算机程序执行，第11个字w需要被添加到数组A。在A附近，看起来像是没有空间来存储新字：进程分配地址空间的起始处在A的左侧，数组B存在右侧。我们如何把w加到数组A？一种方法是：向右移动B来为w制造空间，但大量数据可能已经挨着B被预留，你不得不也移它。更好的方式：简单地请求11字新内存，把A拷贝到新分配内存的起始处，w存到最后，释放进程分配地址空间的前10个字，用于未来内存请求。

固定长度数组是一个数据结构（我们计算模型的内在基础，你可以将你的计算机内存看作为一个大的固定长度数组，你的操作系统从中进行分配）。使用数组实现一个序列，数组中的索引i对应序列中的项目i，允许get_at和set_at$\mathcal{O}(1)$时间复杂度。然而当在序列中删除或插入时，我们需要移动项目并resize数组，意味着这些操作可以在最坏情形下花费线性时间。下面是一个数组序列完整的python实现。

```python
class Array_Seq:
    def __init__(self):
       self.A = []
       self.size = 0

    def __len__(self):    return self.size
    def __iter__(self):   yield from self.A

    def build(self, X):
        self.A = [a for a in X]
        self.size = len(self.A)

    def get_at(self, i):    return self.A[i]
    def set_at(self, i, x):    self.A[i] = x

    def _copy_forward(self, i, n, A, j):
        for k in range(n):
            A[j + k] = self.A[i + k]

    def _copy_backward(self, i, n, A, j):
        for k in range(n - 1, -1, -1):
            A[j + k] = self.A[i + k]

    def insert_at(self, i, x):
        n = len(self)
        A = [None] * (n + 1)
        self._copy_forward(0, i, A, 0)
        A[i] = x
        self._copy_forward(i, n - i, A, i + 1)
        self.build(A)

    def delete_at(self, i):
        n = len(self)
        A = [None] * (n - 1)
        self._copy_forward(0, i, A, 0)
        x = self.A[i]
        self._copy_forward(i + 1, n - i - 1, A, i)
        self.build(A)
        return x

    def insert_first(self, x):    self.insert_at(0, x)
    def delete_first(self):    return self.delete_at(0)
    def insert_last(self, x):    self.insert_at(len(self), x)
    def delete_last(self):    return self.delete_at(len(self) - 1)
```

## 链表序列（Linked List Sequence）

整体而言，链表是一个不同类型的数据结构。不会分配连续内存来存储项目，链表在每个节点存储项目，node：一个拥有两个属性、固定尺寸的容器，node.item存储项目，node.next存储节点（包含序列下个项目）内存地址。

```python
class Linked_List_Node
    def __init__(self, x):
        self.item = x
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)
```

这种数据结构有时称为基于指针的、或链式的，比起基于数组的数据结构更加灵活，因为它们的组成项目可以被存在内存任意地方。链表存储node（存储列表首个元素称为列表的头）地址，以及链表的尺寸（存储在链表的项目数量）。很容易在列表中某项目后添加一个项目，简单地改变地址（例如重新链接指针）。特别地，添加新项目到列表头部花费$\mathcal{O}(1)$时间。然而，找到序列$i^{th}$个项目的仅有方式为：一个一个地遍历项目，导致get_at和set_at操作最坏情形下花费线性时间。下面是一个链表序列的Python实现。

```python
class Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):    return self.size

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, X):
        for a in reversed(X):
            self.insert_first(a);

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        new_node = Linked_List_Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete_first(self):
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x

    def insert_at(self, i, x):
        if i == 0:
            self.insert_first(x)
            return
        new_node = Linked_List_Node(x)
        node = self.head.later_node(i - 1)
        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def delete_at(self, i):
        if i == 0:
            return self.delete_first()
        node = self.head.later_node(i - 1)
        x = node.next.item
        node.next = node.next.next
        self.size -= 1
        return x

    def insert_last(self, x):    self.insert_at(len(self), x)
    def delete_last(self):    return self.delete(len(self) - 1)
```

## 动态数组序列（Dynamic Array Sequence）

数组的动态序列操作需要线性时间（对应数组A的长度）。存在一种无需每次添加一个元素付出线性转换消耗，来向数组添加元素的方式？一种支持快速插入的直接方式是：当你为数组请求空间时分配额外空间。那么，插入元素就会像拷贝新值到下个空槽那样简单。这个折中交易一点额外空间换取常量时间插入。听起来像是一个好主意，但需要一些额外的分配；最终，重复地插入将会填满额外的空间，数组将再次需要重新分配并拷贝。另外，预留一些额外空间将意味着，你程序其它部分更少可用空间。

那么python如何支持，在长度为n的Python列表尾部追加，最坏情形$\mathcal{O}(1)$时间复杂度的？答案是简单的：它不支持。有时追加到python列表尾部需要$\mathcal{O}(n)$时间来转换数组到分配的更大内存，因此有时追加到python列表尾部花费线性时间。然而以正确方式分配额外空间可用保证：任意序列，n次插入仅最多花费$\mathcal{O}(n)$时间（这种线性时间的转换操作不会经常发生），因此每次插入平均花费$\mathcal{O}(1)$时间。我们称这种渐近运行时间为分摊常量时间（amortized constant time），因为操作消耗被分摊到多次应用操作。

为了实现插入数组为分摊常量运行时间，我们的策略将根据数组尺寸等比地分配额外空间。分配\mathcal{O}(n)额外空间保证：溢出分配的插入前，线性数量插入必然发生。动态数组的典型实现，将分配两倍的所需空间来存储当前数组，有时称为table doubling。然而，分配任意固定比例的额外空间将实现分摊。Python List根据下面公式（来自Python的C源码）分配额外空间：

new_allocated = (newsize >> 3) + (newsize < 9 ? 3 :6);

额外分配是谨慎的，大约1/8数组尺寸被追加（尺寸向右位移3位等于除8）。但额外分配与数组尺寸仍然是线性的，因此平均上，每线性时间数组分配，n/8插入被执行，分摊常量时间。

如果我们也想从数组尾部移除项目，弹出最后项目会以常量时间执行，简单地减少存储的数组长度（Python这么做的）。然而，大量项目从大list中移除，未使用的额外分配将占据大量浪费内存（不可用于其它目的）。当数组长度变得十分小时，我们将转换数组内容到一个新的、更小的内存分配，因此更大内存分配可以被释放。这个新分配该多大？如果我们分配数组尺寸，无额外的分配，一个立即地插入会触发另外的分配。对任意序列n为了实现常量分摊运行时间的追加、弹出，当我们重建更小数组时，我们需要确保：留有线性比例未使用空间，这保证了：下次需要重新分配内存前，至少$\Omega(n)$动态操作必然发生。

下面是一个动态数组序列的Python实现，包括操作insert_last（Python list append）和delete_last（python list pop），使用table doubling。当尝试追加到分配的末尾时，数组的内容被转换到两倍大的分配上。当移除到分配空间1/4时，数组内容转移到一半大的分配上。当然python List已经使用这些技术支持动态操作。这个代码被提供用于帮你理解分摊常量追加（append）和弹出（pop）如何被实现。

```python
class Dynamic_Array_Seq(Array_Seq):
    def __init__(self, r = 2):
        super().__init__()
        self.size = 0
        self.r = r
        self._compute_bounds()
        self._resize(0)

    def __len__(self):    return self.size

    def __iter__(self):
        for i in range(len(self)): yield self.A[i]

    def build(self, X):
        for a in X: self.insert_last(a)

    def _compute_bounds(self):
        self.upper = len(self.A)
        self.lower = len(self.A) // (self.r * self.r)

    def _resize(self, n):
        if (self.lower < n < self.upper): return
        m = max(n, 1) * self.r
        A = [None] * m
        self._copy_forward(0, self.size, A, 0)
        self.A = A
        self._compute_bounds()

    def insert_last(self, x):
        self._resize(self.size + 1)
        self.A[self.size] = x
        self.size += 1

    def delete_last(self):
        self.A[self.size -1] = None
        self.size -= 1
        self._resize(self.size)

    def insert_at(self, i, x):
        self.insert_last(None)
        self._copy_backward(i, self.size - (i + 1), self.A, i + 1)
        self.A[i] = x

    def delete_at(self, i):
        x = self.A[i]
        self._copy_forward(i + 1, self.size - (i + 1), self.A, i)
        self.delete_last()
        return x

    def insert_first(self, x): self.insert_at(0, x)
    def delete_first(self):    return self.delete_at(0)
```