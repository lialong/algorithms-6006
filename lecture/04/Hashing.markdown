# 一、回顾

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
</table>
</div>

想要更快的查找以及动态操作。我们能让find(k)比$\theta(logn)$更快？

# 二、比较模型

在本模型中，假定算法仅可以通过比较进行区分

可比较项目：黑盒，仅支持两两比较

比较是：<、<=、>、>=、=、!=，输出是二进制：true或false

目标：存储一组n个可比较项目，支持find(k)操作

# 三、决策树

任何算法可被视作操作执行的决策树

一个内部节点代表一个二元比较，分叉到true或false

对于比较算法，决策树是二叉的

叶子代表算法终止，导致一个算法输出

根到叶子的路径代表算法对于输入的执行

每个算法的输出至少需要一个叶子，因此查询需要>=n+1个叶子

# 四、比较查询下边界

什么是比较查询算法最坏情形运行时间

运行时间>= 比较次数>=任意根到叶子的路径的最大长度>=树的高度

$\ge$n个节点的二叉树的最小高度是多少？

完整二叉树最小高度是多少（除了最后一行，其他行都是满的）

高度$\ge \lceil lg(n+1)\rceil - 1=\Omega(logn)，$因此任意比较排序的运行时间是$\Omega(logn)$

有序数组实现这个边界

有$\theta(n)$个叶子、最大分支因子b的树的高度为$\Omega(log_bn)$

为了更快，需要一个操作：允许常量分支因子

# 五、直接访问数组

利用Word-RAM$\mathcal{O}(1)$时间随机访问索引，线性分支因子

给项目独一无二的整数key：k，{0,...,k-1}，在数组索引k处，存储项目

用一个数组索引关联一个目标

如果key适合机器字，$u\le2^w$，最坏情形的$\mathcal{O}(1)$查找、动态操作

6.006：假设输入数字/字符串符合word，除非长度显示参数化

计算机内存中的任何东西都是二进制整数，要么是64位地址

但空间$\mathcal{O}(u)$，如果$n<<u$，这也是很坏的

举例：如果key是10字母名称，所有可能的名字，$26^{10}=17.6TB$空间

我们如何可以用更少的空间？

# 六、哈希

如果n<<u，映射keys到更小的范围m=$\theta(n)$，并使用更小的直接访问数组

哈希函数：h(k):\{0,...,u-1}->{0,...,m-1}

直接映射数组称为哈希表，h(k)称为k的hash

如果m<<u，根据抽屉理论(pigeonhole principle)，没有hash函数能保证单射(injective)

总是存在keys：a和b，h(a)=h(b)->冲突

不能存储两个项目在相同索引，那么存到哪？

 要么存到数组其他地方（开放寻址）复杂的分析，常见且实用

存储到其他支持动态集合接口数据结构（链）

# 七、链表

存储冲突到另外的数据结构（链表）

如果keys分发到索引处，链表尺寸为：n/m=n/$\Omega(n)$=$\mathcal{O}(1)$

如果链表有$\mathcal{O}(1)$尺寸，所有操作花费$\mathcal{O}(1)$时间

如果不是如此，一些项目可能映射到相同位置，h(k)=constant，链尺寸是$\theta(n)$

需要好的hash函数！那么什么是好的hash函数

# 八、哈希函数

除法（bad）：$h(k)=(k\ mod\ m)$

当keys均匀分布时很好

m要避免存储keys的相似性

远离2和10的幂的大素数是合理的

python使用它的某个版本，附带一些其他混合

若u>>n，每个hash函数将有一些输入集，它将创建一个$\mathcal{O}(n)$尺寸的链

不使用固定的hash函数，随机地选择一个

universal（good，theoretically）：$h_{ab}(k)=(((ak+b)mod\ p)mod\ m)$

Hash Family $H(p,m)=\{h_{ab}|a,b\in\{0,...,p-1\},a\neq0\}$

固定的素数p>u，a和b从{0,...,p-1}中选出

H是一个universal family：$\Pr\limits_{h \in H}\{h(k_i)=h(k_j)\} \le 1/m\ \ \forall k_i\neq k_j \in\{0,...,u-1\}$

为什么universality是有用的？暗含了短链的长度！

$X_{ij}$标志随机变量$h\in H：如果h(k_i)=h(k_j),X_{ij}=1;否则X_{ij}=0$

$h(k_i)$处链的长度是随机变量：$X_i=\sum_jX_{ij}$

链在$h(k_i)$处的期望尺寸

$E\{X_i\}=E\{\sum\limits_jX_{ij}\}=\sum\limits_jE\{X_{ij}\}\\=1+\sum\limits_{j\neq i}E\{X_{ij}\}=1+\sum\limits_{j\neq i}(1)Pr\{h(k_i)=h(k_j)\}+(0)Pr\{h(k_i)+h(k_j)\} \\\le1+\sum\limits_{j\neq i}1/m=1+(n-1)/m$

因为$m=\Omega(n)，负载因子\alpha=n/m=\mathcal{O}(1)，因此\mathcal{O}(1)是符合期望的$

# 九、动态

如果n/m远大于1，为新尺寸m用新随机选择的哈希函数进行重建（rebuild）

像动态数组那样做同样的分析，花费可以被一些动态操作分摊

因此哈希表能够，以所期望的摊还$\mathcal{O}(1)$时间，实现动态集合操作

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

# 十、详述（recitation）

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
</table>
</div>

我们已经学习了如何使用一个有序数组来实现一个集合接口，查询操作是有效的，但动态操作是缺乏有效的。重提一下：$\theta(\log n)的增长比起\theta(n)更接近\theta(1)$，有序数组提供更好的性能。编程中最常见的操作之一是：查找某个你正存着的东西，例如：find(k)。find比$\theta(\log n)$更快，这可能么？如果我们对项目仅能做的是：比较它们的顺序，那么答案是不可能。

## 比较模型

计算中的比较模型，是操作一组可比较的对象。这些对象可被视作黑盒，仅支持一组二元布尔操作（比较）：$<,\le,>,\ge,=,\neq$。每个操作把两个对象视作输入，输出一个布尔值，要么Ture、要么False，取决于元素的相对顺序。操作n个项目的查询算法，将返回一个与输入key相等的存储项目，若没有这个项目存在，则返回无项目。在本部分，我们假设每个项目有一个唯一key。

如果二元比较，是仅有的，区分存储项目和查询key的方式，那么比较查询算法可被视作一个固定的二叉决策树，代表算法的所有执行可能，每个节点代表：算法执行比较。在执行期间，算法沿着从根开始的路径，向树下走。对给定的任意输入，比较排序算法将首先做一些比较，树根处的比较。依赖这次比较的结果，计算将处理两个子节点之一中的比较。算法重复地比较，直到抵达叶子节点（算法终止，为算法返回一个输出）。必定有一个叶子对应算法每个可能的输出。对查询来说，有n+1个可能的输出，n个项目以及无项目被找到的结果，

因此必定至少有n+1个叶子位于决策树。最坏情形的比较次数（一定是由比较查询算法得出的），就是决策树算法的高度，根到叶子最长路径的长度。

练习：证明n节点树的最小高度：$\lceil \lg(n+1)\rceil-1=\Omega(\log n)$

答案：高度为h的二叉树，节点数量最多为：$n\le T(h)=2^{h+1}-1,因此h\ge (\lg(n+1)-1)$。

高度为0的树有1个节点，因此$T(0)=1$，base case满足声明。高度为h、最多节点数量的树，一定有最多数量的节点在它的两个子树，因此$T(h)=2T(h-1)+1$，取代T(h)，得出$2^{h+1}-1=2(2^h-1)+1$，得证。

一个有n+1个叶子的树，有n个以上节点，那么高度至少是$\Omega(\log n)$。因此用于区分n个项目的最小比较次数至少是$\Omega(\log n)$，任何比较查询算法的最坏运行时间至少是$\Omega(\log n)$!因此有序数组和平衡的BST，能以计算比较模型，近似最优地支持find(k)。

比较是非常局限性的，因为每个执行的操作，在决策树中，最多导致常数分叉因子。比较拥有分叉因子2是没关系的，任意固定常量的分叉因子，将导致一个至少有$\Omega(\log n)$高度的决策树。如果我们不限制为比较，也就有了快于$\mathcal{O}(\log n)$查询的可能。更特殊的，如果我们可以使用操作：允许大于常量$\omega(1)$的分叉因子，那么我们的决策树会更扁，得到一个更快的算法。

## 直接访问数组

电脑中的绝大多数操作，仅允许常量逻辑分叉，像代码中的if语句。然而，你电脑上允许非常量分叉因子的操作：以常量时间随机访问任意内存地址。这个特殊操作允许一个算法决策树用巨大的分叉因子（如同你电脑里的空间那么大）来分叉。为了利用这个操作，我们定义一个数据结构（称为直接访问数组），这是一个正常的静态数组，用每个数组索引位置来关联一个语义：特别地是，任何有key为k的项目x，将被存在数组索引k处。这个声明，仅当项目keys是整数时有意义。幸运的是，在计算机中，内存中的任何事物可以被关联到整数上，例如：它的值是一系列的位或是内存地址，所以从现在起，我们将仅考虑整数keys。

现在假设我们想存储n个项目，每个关联一个唯一的整数key（范围是，0到u-1）。我们可以存储项目到一个长度为u的直接访问数组，如果数组槽i存在项目的话，那它包含一个与整数i相关联的项目。为了找到key为整数i的项目，一个查询算法可以简单地查看数组插槽i，来以最坏常量时间对查询做出响应。然而，这个数据结构上的顺序操作将会非常慢：我们不能在直接访问数组，保证哪里是首部、尾部、或next元素，因此我们不得不花费u时间来做排序操作。

最坏情形：基于存储空间消耗常量时间查找：对范围内所有可能的key，直接访问数组必须有一个对应的槽。当u比要存储的项目数量大很多时，存储一个直接访问数组可能是浪费的，在现代机器上甚至是不可能的。举例，假定你想用直接访问数组，支持10字母名字的集合find(k)操作。可能名字的空间将会是$u\approx26^{10}\approx9.5\times10^{13}$；表示该长度的位数组将需要17.6TB存储空间。我们如何解决这个障碍？答案是哈希！

```python
class DirectAccessArray:
    def __init__(self, u):    self.A = [None] * u
    def find(self, k):    return self.A[k]
    def insert(self, x):    self.A[x.key] = x
    def delete(self, k):    self.A[x.key] = None
    def find_next(self, k):
        for i in range(k, len(self.A)):
            if A[i] is not None:
                return A[i]
    def find_max(self):
        for i in range(len(self.A) - 1, -1, -1):
            if A[i] is not None:
                return A[i]
    def delete_max(self):
        for i in range(len(self.A) - 1, -1, -1):            
            x = A[i]
            if x is not None:
                A[i] = None
                return x
```

## 哈希（hashing）

当仅用线性$\mathcal{O}(n)$空间，且n<<u，能从直接访问数组中获得性能成效么？可能的答案是：存储项目到更小的动态直接访问数组，$m=\mathcal{O}(n)$个槽，而不是u，根据存储项目数量，像动态数组一样增长、收缩。为了做到这样，我们需要一个函数，它映射项目keys到直接访问数组的不同槽位，$h(k):\{0,...,u-1\} \rightarrow \{0,...,m-1\}$。我们称这个函数为哈希函数或哈希映射，更小的直接访问数组被称为哈希表，$h(k)$是整数key k的哈希值。如果哈希函数在你存储的n个keys上是单射的，不会有两个keys，映射到直接访问数组相同的索引，那么我们将能够支持最坏情形常量时间的查询，哈希表表现得如同更小作用域m的直接访问数组。

不幸地，如果可能keys的空间大于数组索引的数量，列入m<u，那么根据抽屉理论（pigeonhole principle），任何哈希函数映射u个可能keys到m索引，必然映射多个keys到相同数组索引。如果两个项目关联着keys k1和k2，哈希到相同索引，例如$h(k_1)=h(k_2)$，我们称：k1和k2的哈希冲突了。如果不能提前知道什么keys被存储，那么这是不可能的：你选择的哈希函数完全避开冲突。如果更小的直接访问数组哈希表，仅能每个索引存储一个项目，当冲突发生时，我们将冲突项目存到哪？要么我们将冲突存储在相同直接访问数组的其他地方，要么把冲突存到其他地方（不在直接访问数组内）。第一个策略称为开放寻址法，这是绝大多数哈希表真正实现的，但这种策略很难分析。我们将采取第二个策略（拉链法）。

## 拉链法（chaining）

拉链法是一个冲突解决策略，冲突keys独立于原始哈希表存储。每个哈希表索引持有一个指向拉链的指针，单独的支持动态集合接口的数据结构，特殊操作：find(k)，insert(x)和delete(k)。使用链表或动态数组实现拉链是常见的，只要每次操作不超过线性时间就是可以的。插入项目x到哈希表，简单地在索引h(x.key)处的拉链上插入x；从哈希表中find或delete一个key k，简单地在索引h(k)处的拉链上查找、删除k。

完美！我们想让拉链变得较小，因为如果我们的拉链仅持有常量个项目，那么动态集合操作将以常量时间运行。假设我们不幸地选了哈希函数，我们想存储的所有keys有相同的索引位置，在同一个拉链中。那么拉链将有线性尺寸，意味着动态集合操作会花费线性时间。好的哈希函数将尝试最小化这种冲突的频率，以便于最小化任意拉链尺寸。怎么算一个好的hash函数？

## 哈希函数（hash functions）

除法散列法（division method，bad）：最简单的映射：尺寸为u的整数域映射到更小的尺寸m，简单地让key除以m，取余数：$h(k)=(k\ mod\ m)$，或者在python中，k%m。如果你正在存的keys均匀地分布在域中，除法散列法将在哈希索引上，均匀地分发项目，因此我们期望拉链有小尺寸、高性能。然而，如果所有项目除以m后有同样的余数，那么这个哈希函数将是糟糕的。我们数据结构的性能，应独立于我们存储的keys。

全域哈希（universal hash，good）：足够大的key域u，每个哈希函数对某组n个输入是不友好的。然而，通过随机地从大类哈希函数中选择我们的哈希函数，能够基于哈希表性能实现好的期望边界。期望是，我们选择的哈希函数，独立于输入。这不是对可能输入keys域的期望。一个性能良好的哈希函数族：

$H(m,p)=\{h_{ab}(k)=(((ak+b)\ mod\ p)\ mod\ m)\ a,b\in\{0,...,p-1\}and\ a\neq0\}$

p是大于key域u的素数。通过选择具体的a、b值，明确这个族中的某个hash函数。这个哈希函数族是全域（universal）的：对于任意两个keys，当使用来自全域族中随机选择的哈希函数时，它们哈希值冲突的可能性不会大于1/m。

$\Pr\limits_{h\in H}\{h(k_i)=h(k_j)\}\le 1/m，\forall k_i \neq k_j\in\{0,...,u-1\}$

如果我们知道一个哈希函数族是全域的，那么我们能得到任意拉链尺寸的期望上边界，期望源于我们从家族中选择的哈希函数。让$X_{ij}$表示随机变量，若$k_i和k_j$在选定的哈希函数上冲突，那么值为1，否则值为0。用随机变量代表哈希到索引$h(k_i)$的项目数量，将会是$X_i=\sum_jX_{ij}，k_j来自\{k_0,...,k_{n-1}\}$。哈希到位于$h(k_i)$处，拉链的keys期望数量为：

$E{X_i}=E{\sum\limits_jX_{ij}}=\sum\limits_jE{X_{ij}}=1+\sum\limits_{j\neq i}E{X_{ij}}\\=1+\sum\limits_{j\neq i}(1)Pr\{h(k_i)=h(k_j)\}+(0)Pr\{h(k_i)+h(k_j)\}\\ \le1+\sum\limits_{j\neq i}1/m=1+(n-1)/m$

如果哈希表的尺寸对于存储项目数量来说至少是线性的，$m=\Omega(n)$，任意拉链的期望尺寸将是$1+(n-1)/\Omega(n)=\mathcal{O}(n)$，一个常量。因此用一个从全域族中随机选择的哈希函数来实现哈希表，冲突部分用拉链解决，将以期望的常量时间执行动态集合操作，独立于输入keys。为了保持$m=\mathcal{O}(n)$，插入和删除操作需要你重建直接访问数组到一个不同尺寸，选择新哈希函数，并重新插入所有项目到哈希表。这可以用与动态数组相同的方式来完成，导致动态操作摊还边界。

```python
class Hash_Table_Set:
    def __init__(self, r = 200):
        self.chain_set = Set_from_Seq(Linked_List_Seq)
        self.A = []
        self.size = 0
        self.r = r
        self.p = 2**31 - 1
        self.a = randint(1, self.p - 1)
        self._compute_bounds()
        self._resize(0)

    def __len__(self):    return self.size
    def __iter__(self):
        for X in self.A:
            yield from X
    def build(self, X):
        for x in X: self.insert(x)

    def _hash(self, k, m):
        return ((self.a * k) % self.p) % m

    def _compute_bounds(self):
        self.upper = len(self.A)
        self.lower = len(self.A) * 100*100 // (self.r*self.r)

    def _resize(self, n):
        if (self.lower >= n) or (n >= self.upper):
            f = self.r // 100
            if self.r % 100:    f += 1
            m = max(n, 1) * f
            A = [self.chain_set() for _ in range(m)]
            for x in self:
                h = self._hash(x.key, m)
                A[h].insert(x)
            self.A = A
            self._compute_bounds()

    def find(self, k):
        h = self._hash(k, len(self.A))
        return self.A[h].find(k)

    def insert(self, x):
        self._resize(self.size + 1)
        h = self._hash(x.key, len(self.A))
        added = self.A[h].insert(x)
        if added:    self.size += 1
        return added

    def delete(self, k):
        assert len(self) > 0
        h = self._hash(k, len(self.A))
        x = self.A[h].delete(k)
        self.size -= 1
        self._resize(self.size)
        return x

    def find_min(self):
        out = None
        for x in self:
            if (out is None) or (x.key < out.key):
                out = x
        return out

    def find_max(self):
        out = None
        for x in self:
            if (out is None) or (x.key > out.key):
                out = x
        return out

    def find_next(self, k):
        out = None
        for x in self:
            if x.key > k
                if (out is None) or (x.key < out.key):
                    out = x
        return out

    def find_prev(self, k):
        out = None
        for x in self:
            if x.key < k
                if (out is None) or (x.key > out.key):
                    out = x
        return out

    def iter_order(self):
        x = self.find_min()
        while x:
            yield x
            x = self.find_next(x.key)
```

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

## 练习

给定一个未排序的数组$A=[a_0,...,a_{n-1}]$，包含n个正整数，重复性问题：数组中两个整数有相同的值。

1）描述一个暴力的最坏情形$\mathcal{O}(n^2)$时间的算法来解决“重复性问题”

遍历数组中所有整数对：$\binom{n}{2}$，并且以$\mathcal{O}(1)$时间检查它们是否相等

2）描述一个最坏情形$\mathcal{O}(n\log n)$时间的算法来解决“重复性问题”

以最坏情形$\mathcal{O}(n\log n)$时间复杂度（例如使用归并排序）对数组进行排序，然后扫描有序数组，若$\mathcal{O}(n)$相邻对有相同值，则返回

3）描述一个期望为$\mathcal{O}(n)$时间复杂度的算法来解决“重复性问题”

哈希n个整数中每一个到一个哈希表中（使用链、全域哈希族中随机选择一个哈希函数），插入花费$\mathcal{O}(1)$时间。

4）若$k<n且a_i\le k,所有a_i \in A$，描述一个最坏情形$\mathcal{O}(1)$时间的算法来解决”重复性问题“。

如果k<n，重复性总是存在，根据抽屉原则。

5）如果$n\le k且a_i\le k,所有a_i \in A$，描述一个最坏情形$\mathcal{O}(k)$时间的算法来解决”重复性问题“。

将n个整数的每个插入到一个长度为k的直接访问数组，这将花费最坏情形$\mathcal{O}(k)$时间来实例化，每次插入操作最坏情形$\mathcal{O}(1)$时间。当尝试插入时，如果一个整数已经存在于数组索引处，那么表明”重复性“存在。
