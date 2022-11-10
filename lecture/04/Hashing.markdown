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

电脑中的绝大多数操作，仅允许常量逻辑分叉，像代码中的if语句。然而，你电脑上允许非常量分叉因子的操作：以常量时间随机访问任意内存地址。
