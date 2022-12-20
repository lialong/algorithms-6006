# 一、回顾

* 比较查找下边界：任何有n个节点的比较树，高度$\ge \lceil lg(n+1)\rceil-1$

* 线性分支因子的操作，使用随机访问更快

* 直接访问数组是快的，但可能使用大量空间$(\Theta(u))$

* 通过映射（hashing）key的空间从u降到$m=\Theta(n)$，解决了空间问题

* 哈希表给出了期望$\mathcal{O}(1)$时间的操作，如果是动态操作则为分摊时间

* 期望输入独立：选择从全域哈希族中随机选取哈希函数

* 数据结构概览

* 最终我们实现了更快地查找。我们也能实现更快的排序？

<div>
<table>
    <tr>    
        <td rowspan=3>数据结构</td>
        <td colspan=5 align="center">操作，最坏情形O</td>    
    </tr>
    <tr>
        <td>容器（container）</td>
        <td>静态（static）</td>
        <td>动态（dynamic）</td>
        <td colspan=2 align="center">顺序（order）</td>
    </tr>
    <tr>
        <td>build(X)</td>
        <td>find(k)</td>
        <td>insert(x)<br>delete(k)</td>
        <td>find_min()<br>find_max()</td>
        <td>find_prev(k)<br>find_next(k)</td>
    </tr>
    <tr>
        <td>数组</td>
        <td>n</td>
        <td>n</td>
        <td>n</td>
        <td>n</td>
        <td>n</td>
    </tr>
    <tr>
        <td>有序数组</td>
        <td>nlogn</td>
        <td>logn</td>
        <td>n</td>
        <td>1</td>
        <td>logn</td>
    </tr>
    <tr>
        <td>直接访问数组</td>
        <td>u</td>
        <td>1</td>
        <td>1</td>
        <td>u</td>
        <td>u</td>
    </tr>
    <tr>
        <td>哈希表</td>
        <td>n</td>
        <td>1</td>
        <td>1</td>
        <td>n</td>
        <td>n</td>
    </tr>
</table>
</div>

# 二、比较排序下边界

* 比较模型表明：算法决策树是二叉的（常量分叉因子）

* 需要：叶子$L\ge$可能的输出

* 树高度的下边界$\Omega(\log L)$，因此最坏情形执行时间为$\Omega(\log L)$

* 为了对数组的n个元素进行排序，输出是：n!

* 因此归并排序在比较模型中是最佳的

* 我们能利用直接访问数组来更快排序？

# 三、直接访问数组排序

* 举例：[5, 2, 7, 0, 4]

* 假设所有key是独一无二的非负数，在范围：$\{0,...,u-1\},n\le u$

* 每个项目插入到尺寸为u的直接访问数组，$\Theta(n)$

* 以出现在直接访问数组中的顺序返回元素，$\Theta(u)$

* 运行时间为$\Theta(u)$，如果$u=\Theta(n)，$则运行时间为$\Theta(n)$

```python
def direct_access_sort(A):
    "对A排序，假定项目有不同的非负key"
    u= 1 + max([x.key for x in A])
    D = [None] * u
    for x in A:
        D[x.key] = x
    i = 0
    for key in range(u):
        if D[key] is not None:
            A[i] = D[key]
            i += 1
```

* 如果key有更大范围，像$u=\Omega(n^2)<n^2$

* 通过元组(a,b)表示每个key k，k=an+b，$0\le b <n$

* $a=\lfloor{k/n}\rfloor\lt n,b=(k\ mod\ n)$

* 这是python内置的一个操作：(a,b)=divmod(k, n)

* 举例：[17,3,24,22,12]=>[(3,2), (0,3), (4,4), (4,2), (2,2)]=>[32,03,44,42,22]，n=5

* 如何对元组排序？

# 四、元组排序

* 项目key是长度相等的元组，项目$x.key=(x.k_1,x.k_2,x.k_3,...)$

* 以字典序排列所有entry，因此首个key $k_1$是最重要的

* 如何排序？使用其他辅助排序算法来单独地对每个key排序

* 就像通过多列，对电子表格做行排序

* 排成什么顺序？最不重要到最重要

* 练习：[32,03,44,42,22]=>[42,22,32,03,44]=>[03,22,32,42,44]，n=5

---

* 使用元组排序，辅助直接访问数组排序来排序元组(a,b)

* 一些整数可能有同样的a或b值，即使输入key不同

* 需要排序允许重复key，保持输入顺序

* 想排序是稳定的：输出中的重复key顺序与输入顺序一致

* 直接访问数组排序不能对有相同key的数组排序

* 我们能更改直接访问数组，以稳定的方式来允许多个key么？

# 五、计数排序

* 不在每个数组索引处存储单个项目，而是存储一个链，就像是哈希

* 为了稳定性，链数据结构应该记住项目添加进去的顺序

* 使用一个序列数据结构，它保持了插入顺序

* 索引x.key处，插入项目x，insert_last到链的末尾

* 排序，按序列顺序读取所有链，一个一个返回项目

```python
def counting_sort(A):
    "Sort A assuming items have non-negative keys"
    u = 1 + max([x.key for x in A])     # O(n) find maximum key
    D = [[] for i in range(u)]          # O(u) direct access array of chains
    for x in A:                         # O(n) insert into chain at x.key
    D[x.key].append(x)
    i = 0
    for chain in D:                     # O(u) read out items in order
        for x in chain:
            A[i] = x
            i += 1
```

# 六、基数排序

* 如果$u<n^2$，使用辅助计数排序的元组排序来对元组(a,b)排序

* 先对最不重要的key b做排序，然后对最重要的key a排序

* 稳定性保证之前的排序依然保留

* 算法运行时间是$\mathcal{O}(2n)=\mathcal{O}(n)$

* 如果每个$key<n^c,c=\log_n(u)$，那么每个key最多有以n为基的c位数字

* 一个c位数可以被写为c个元素的元组，以$\mathcal{O}(c)$时间

* 我们对每个以n为基的c位数以$\mathcal{O}(n)$时间排序

* 因此用辅助计数排序的元组排序总共以$\mathcal{O}(cn)$时间运行

* 如果c是常量，每个$key<n^c$，这个排序是线性的$\mathcal{O}(n)$

```python
def radix_sort(A):
    n = len(A)
    u = 1 + max([x.key for x in A])
    c = 1 + (u.bit_length() // n.bit_length())
    class Obj: pass
    D = [Obj() for a in A]    
    for i in range(n):
        D[i].digits = []
        D[i].item = A[i]
        high = A[i].key
        for j in range(c)
            high, low = divmod(high, n)
            D[i].digits.append(low)
    for i in range(c):
        for j in range(n):
            D[j].key = D[j].digits[i]
        counting_sort(D)
    for i in range(n):
        A[i] = D[i].item
```

# 七、recitation

## 比较排序

上次我们讨论了比较模型中搜索的下边界。我们可以对任意搜索算法（仅使用比较模型）的最坏运行时间下边界使用一个相似的分析。排序算法有n!个可能输出：项目的n!个全排列。任意排序算法（仅使用比较）的决策树一定至少有n!个叶子，因此高度必须至少$\Omega(\log(n!))=\Omega(n\log n)$，运行时间至少$\Omega(n\log n)$

## 直接访问数组

为了搜索，我们不限制只通过比较操作，那么可能超越$\Omega(n\log n)$边界。如果要排序的项目有唯一的key，取值为有限正整数：$\{0,...,u-1\},n\le u$，我们可以简单地通过使用直接访问数组来排序。构建一个尺寸为u的直接访问数组，并插入每个项目x到索引x.key。然后简单地从左往右遍历直接访问数组，返回找到的项目。插入花费时间$\mathcal{O}(n)$，初始化、扫描直接访问数组花费时间$\Theta(u)$，因此这个排序算法以$\Theta(n+u)$时间运行。如果$u=\mathcal{O}(n)$，这个算法是线性的！不幸地是，这个排序算法有两个弊端：它不能处理重复key；不能处理key取值有大范围的情况。

```python
def direct_access_sort(A):
    u = 1 + max([x.key for x in A])
    D = [None] * u
    for x in A:
        D[x.key] = x
    i = 0
    for key in range(u)
        if D[key] is not None:
            A[i] = D[key]
            i += 1
```

## 计数排序(Counting Sort)

为了解决第一个问题，我们简单地连接一个链到每个直接访问数组索引处，就像hashing。当多个项目有相同key时，我们将它们存储到与它们的key相关联的链中。重要的是，这个算法是稳定的：有相同key的项目，以与输入相同的顺序，出现在输出。因此，我们选择链（支持队列接口的序列）来保证有序，插入到队列尾部，以它们被插入的顺序返回项目。

```python
def counting_sort(A):
    u = 1 + max([x.key for x in A])
    D = [[] for i in range(u)]
    for x in A:
        D[x.key].append(x)
    i = 0
    for chain in D:
        for x in chain:
            A[i] = x
            i += 1
```

计数排序花费$\mathcal{O}(u)$时间来初始化直接访问数组的链，$\mathcal{O}(n)$时间来插入所有元素，$\mathcal{O}(u)$时间扫描直接访问数组，返回项目。因此算法以$\mathcal{O}(n+u)$时间运行。当$u=\mathcal{O}(n)$，计数排序以线性时间运行，但这次允许重复key。

计数排序另外一种实现，仅记录每个索引处有多少key，然后仅移动每个项目一次，而不是上面的实现：移动它们到链中，然后放回去。下面的实现，通过累加，计算出每个项目最终的索引位置。

```python
def counting_sort(A):
    u = 1 + max([x.key for x in A])
    D = [0] * u
    for x in A:
        A[x.key] += 1
    for k in range(1, u):
        D[k] += D[k-1]
    for x in list(reverse(A))
        A[D[x.key] - 1] = x
        D[x.key] -= 1
```

现在如果我们想对更大整数范围内的key排序。我们的策略是把整数key分成几部分，然后对每个部分排序。为了实现它，我们将需要一个排序策略来排序元组。

## 元组排序

假设我们想对元组排序，每个包含多个不同key(举例：x.k1,x.k2,x.k3,...)，因此根据key的顺序，排序是字典式的（k1比k2更重要，k2比k3更重要，等待）。那么元组排序使用一个稳定的排序算法作为子方法，来重复地排序对象，首先根据最不重要的key，然后第二最不重要的key，一直到最重要的key，因此字典式地排序对象。元组排序与电子表格根据不同列的多行排序相似。然而，元组排序仅在这种情况下正确：上一轮顺序保持在下一轮中。特别地，元组排序需要子排序算法是稳定的。

## 基数排序

现在，为了提高依然能线性排序的整数集范围，当以n为基时，我们把每个整数拆分成多个n 的指数，它的数字序列代表每给项目key。如果整数是非负数，且集合中最大的整数是u，那么这个基数n将有$\lceil\log_nu\rceil$个数字。我们可以把这些数字表示为元组，并用元组排序对它们进行排序，用计数排序，从最不重要的数字到最重要的数字进行排序。这个元组排序和计数排序的结合称为基数排序。如果集合中最大整数$u\le n^c$，那么基数排序运行时间为$\mathcal{O}(nc)$。如果c为常量，那么基数排序也以线性时间运行。

```python
def radix_sort(A):
    n = len(A)
    u = 1 + max([x.key for x in A])
    c = 1 + (u.bit_length() //  n.bit_length())
    class Obj: pass
    D = [Obj() for a in A]
    for i in range(n):
        D[i].digits = []
        D[i].item = A[i]
        high = A[i].key
        for j in range(c):
            high, low = divmod(high, n)
            D[i].digits.append(low)
    for i in range(c):
        for j in range(n):
            D[j].key = D[j].digits[i]
        counting_sort(D)
    for i in range(n):
        A[i] = D[i].item
```

## 练习

1）使用基底为10的基数排序，对下面整数排序

(329, 457, 657, 839, 436, 720, 355) → (329, 355, 436, 457, 657, 720, 839)

取c=3，基底为10，则每个数都能转化为一个3元组，即(百位, 十位, 个位)，然后进行排序

2）描述一个线性算法，来对取值范围$[-n^2,...,n^3]$的n个数进行排序

对每个数加$n^2$，每个数成为了正数，使用基数排序，输出的每个元素减$n^2$

3）描述一个线性时间算法来对n个字符串排序，每个字符串有k个英文字符

使用元组排序，通过从右向左的计数排序重复对字符串排序，使用整数$\{0,...,25\}$来代表英文字母。有k轮计数排序，每轮花费$\Theta(n+26)=\Theta(n)$时间，因此算法以$\Theta(nk)$时间运行。运行时间是线性的，因为输入尺寸为$\Theta(nk)$