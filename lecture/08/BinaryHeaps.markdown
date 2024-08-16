# 一、优先队列接口

* 记录一些项目，快速地访问/移除最重要的
  
  * 例：有限带宽的路由器，必须优先某些信息
  
  * 例：操作系统内核中的进程调度
  
  * 例：离散事件模拟（下一件事何时发生）
  
  * 例：图算法（接下来的课程中）

* 通过key有序的项目=优先，因此是集合接口（不是序列接口）

* 对集合特定操作子集进行了优化：
  
  * build(X)，由可迭代的X构建优先队列
  
  * insert(x)，添加项目x到数据结构
  
  * delete_max()，移除并返回拥有最大key的存储项目
  
  * find_max()，返回拥有最大key的存储项目

* 通常对最大或最小做出优化，而非全部

* 聚焦于insert和delete_max操作：build可以重复地insert；find_max可以是insert(delete_max())

# 二、优先队列排序

* 任何优先队列数据结构可以翻译为排序算法：
  
  * build(A)，按输入顺序，一个一个地插入项目
  
  * 重复地delete_min（或delete_max()）来决定（反向）顺序

* 所有艰难的工作发生在数据结构中

* 运行时间是：$T_{build}+n*T_{delete\_max}\le n*T_{insert}+n*T_{delete\_max}$
  
  我们已经看到的一些排序算法，可以被视作优先队列排序：

![](https://raw.githubusercontent.com/lialong/algorithms-6006/main/lecture/08/1.PNG)

# 三、优先队列：集合AVL树

* 集合AVL树支持insert(x)，find_min()，find_max()，delete_min()，delete_max()花费$\mathcal{O}(\log n)$

* 因此优先队列排序花费$\mathcal{O}(n\log n)$
  
  * 这源自lecture 7的AVL排序

* 可以通过子树新增变量，加速find_min()和find_max()为耗时$\mathcal{O}(1)$

* 但这个数据结构是复杂的，结果排序是非in-place的

* 是否存在一个更简单的数据结构用于优先队列，并且是$\mathcal{O}(n\log n)$ 时间复杂度的in-place排序？存在，二项堆和堆排序

* 在序列数据结构（数组）之上，实现集合数据结构，使用我们学过的二叉树

# 四、优先队列：数组

* 存储项目到一个无序动态数组

* insert(x)：追加x到最后，花费摊还$\mathcal{O}(1)$

* delete_max()：花费$\mathcal{O}(n)$找到最大的，交换最大的到最后，然后删除

* insert是快的，但delete_max是慢的

* 优先队列排序是选择排序！（加上一些拷贝）

# 五、优先队列：有序数组

* 存储项目到有序动态数组

* insert(x)：在末尾追加x，花费$\mathcal{O}(n)$交换到有序的位置

* delete_max()：从末尾删除花费摊还$\mathcal{O}(1)$

* 优先队列排序是插入排序！（加上一些拷贝）

* 我们可以从两个极端的数组优先队列中找到折中？

# 六、数组作为一个完全的二叉树

* 想法：数组表示完全二叉树，除最大深度外，深度i处有$2^i$个点，所有点左对齐。

![](https://raw.githubusercontent.com/lialong/algorithms-6006/main/lecture/08/2.PNG)

* 等价地，完全二叉数阅读顺序：从根到叶子、从左到右

* 数组和完全二叉树的双射

![](https://raw.githubusercontent.com/lialong/algorithms-6006/main/lecture/08/3.PNG)

* 对应n个元素数组的完全二叉树高度为$\lceil \lg n \rceil$，因此是平衡二叉树

# 七、隐式完全二叉树

* 完全二叉树结构可以是隐式的，而非存储指针

* 根在索引0处

* 通过索引算式计算相邻点：left(i)=2i+1,right(i)=2i+2,parent(i)=$\lfloor \frac {i-1}{2} \rfloor$

# 八、二叉堆

* 想法：更大的元素在树中高度更高，仅局部如此

* 节点i处最大堆属性：$Q[i]\ge Q[j],j\in\{left(i),right(i)\}$

* 最大堆是一个数组：所有节点满足最大堆属性

* 声明：在最大堆中，对于subtree(i)中所有节点j，每个节点i满足$Q[i]\ge Q[j]$

* 特别地，最大项目在最大堆的根部

# 九、堆插入

* 追加新项目x到数组末尾，耗费摊还$\mathcal{O}(1)$，生成它的下个叶子i（按读顺序）

* max_heapify_up(i)：与parent交换，直到满足最大堆属性
  
  * 检测$Q[parent(i)]\ge Q[i]$（parent(i)处最大堆属性的一部分）
  
  * 如果不是，交换Q[i]和Q[parent(i)]，递归max_heapify_up(parent(i))

* 正确性：
  
  * 最大堆属性保证所有节点>=子节点
  
  * 如果必须交换，Q[parent(i)]满足同样的保证，而非Q[i]

* 运行时间：树的高度，因此是$\Theta(\log n)$

# 十、堆删除最大

* 仅可以轻松地从动态数组中移除最后的项目，但最大的key是树的根

* 因此把根节点（i=0处的项目）与最后的项目（n-1处）交换

* max_heapify_down(i)：将根与更大的子节点交换，直到满足最大堆属性
  
  * 检查是否$Q[i]\ge Q[j],j \in \{left(i),right(i)\}$（位于i处的最大堆属性）
  
  * 如果不是，Q[i]和Q[j]进行交换（$j\in\{left(i),right(i)\}$，有最大key的项目），并递归调用max_heapify_down(j)

* 正确性：
  
  * 最大堆属性保证所有节点>=子节点
  
  * 如果必须交换，Q[j]满足同样的保证，而非Q[i]

* 运行时间：树的高度，因此是$\Theta(\log n)$

# 十一、堆排序

* 添加最大堆到优先队列排序，给我们一个新的排序算法

* 运行时间是$\mathcal{O}(n\log n)$，因为每个insert和delete_max花费$\mathcal{O}(\log n)$

* 对于这个排序算法，通常包含两个提升

# 十二、in-place优先队列排序

* 最大堆Q是一个更大数组A的前缀，记录共有多少项目在堆中

* $|Q|$初始时为0，最终为$|A|$（插入完），然后再次为0（删除后）

* insert()吸收数组中下个项目（位于索引$|Q|$处）到堆

* delete_max()将最大的项目移到最后，然后通过降低$|Q|$来废弃它

* 数组in-place优先队列排序是选择排序

* 有序数组in-place优先队列排序是插入排序

* 二叉最大堆in-place优先队列排序是堆排序

# 十三、线性构建堆

* 插入n个项目到堆中，i从0到n-1调用max_heapify_up(i)（根下降）：

最坏情形交换：$\sum_{i=0}^{n-1}depth(i)=\sum_{i=0}^{n-1}\lg i=\lg(n!)\ge(n/2)\lg(n/2)=\Omega(n\lg n)$

* 将整个数组当作一个完全二叉树，i从n-1到0调用max_heapify_down(i)（叶子上升）：

最坏情形交换：$\sum_{i=0}^{n-1}height(i)=\sum_{i=0}^{n-1}(\lg n-\lg i)=\lg \frac{n^n}{n!}=\Theta(\lg \frac{n^n}{\sqrt n(n/e)^n})=\mathcal{O}(n)$

* 因此可以花费$\mathcal{O}(n)$构建堆

* 没有加速堆排序的性能（$\mathcal{O}(n\log n)$）

# 十四、序列AVL树优先队列

* 其他线性构建时间的对数数据结构，序列AVL树

* 以任意顺序（插入顺序）存储优先队列项目到序列AVL树

* 维持最大新增变量：node.max=指向node子树中拥有最大key的节点，这是一个子树属性，因此花费常量复杂度

* find_min()和find_max()花费$\mathcal{O}(1)$

* delete_min和delete_max花费$\mathcal{O}(\log n)$

* build(A)花费$\mathcal{O}(n)$

* 与二叉堆有相同的边界

# 十五、Set和Multiset

* 我们的集合接口假定没有重复key，我们可以使用这些集合实现Multiset，允许项目有重复key
  
  * 集合中的每个项目是一个序列（比如链表），存储了有同一个key的多个项目

* 实际上，除了这个方法，二叉堆和AVL树可以直接处理重复key的项目（比如delete_max删除有最大key的所有项目），注意使用<=，而不是集合AVL树中的<

# 十六、Recitation

## 优先队列

优先队列为至少3种排序算法提供了通用框架，不同数据结构实现方式不同。

<div>    
<table>
    <tr>    
        <td>算法</td>
        <td>数据结构</td>
        <td>插入</td>
        <td>抽取</td>
        <td>总计</td>
    </tr>
    <tr>
        <td>选择排序</td>
        <td>数组</td>
        <td>O(1)</td>
        <td>O(n)</td>
        <td>O(n^2)</td>
    </tr>
    <tr>
        <td>插入排序</td>
        <td>有序数组</td>
        <td>O(n)</td>
        <td>O(1)</td>
        <td>O(n^2)</td>
    </tr>
    <tr>
        <td>堆排序</td>
        <td>二叉堆</td>
        <td>O(logn)</td>
        <td>O(logn)</td>
        <td>O(nlogn)</td>
    </tr>
</table>
</div>

python代码实现这些优先队列。抽象基类有优先队列的接口，维护一个内部数组A，实现insert(x)和delete_max()（后者本身不正确，但对子类有用）。

```python
class PriorityQueue:
    def __init__(self):
        self.A = []

    def insert(self, x):
        self.A.append(x)

    def delete_max(self):
        if len(self.A) < 1:
            raise IndexError('pop from empty priority queue')
        return self.A.pop()

    @classmethod
    def sort(Queue, A):
        pq = Queue()
        for x in A:
            pq.insert(x)
        out = [pq.delete_max() for _ in A]
        out.reverse()
        return out
```

共享的、跨实现的，是排序方法，给定insert和delete_max的实现。排序简化为数组上的2个循环：一个插入所有元素，另一个以反向顺序弹出数组连续最大值。

## 数组堆

我们在之前recitation中展示选择排序和归并排序。现在是优先队列视角的实现。如果你展开本代码的组织，你将得到与之前呈现相同的代码。

```python
class PQ_Array(PriorityQueue):
    # PriorityQueue.insert already correct: appends to end of self.A
    def delete_max(self):
        n, A, m = len(self.A), self.A, 0
        for i in range(1, n):
            if A[m].key < A[i].key:
                m = i
        A[m], A[n-1] = A[n-1], A[m]
        return super().delete_max()
```

```python
class PQ_SortedArray(PriorityQueue):
    # PriorityQueue.delete_max already correct: pop from end of self.A
    def insert(self, *args):
        super().insert(*args)
        i, A = len(self.A) - 1, self.A
        while 0 < i and A[i].key < A[i-1].key:
            A[i], A[i-1] = A[i-1], A[i]
            i -= 1
```

我们使用*args允许insert接收1个参数或0个参数；in-place生成优先队列时，我们将需要后者功能。

## 二叉堆

下个实现基于二叉堆，利用完全二叉树（对数高度）来提升性能。这些函数所做的大部分工作都由下面的max_heapify_up和max_heapiify_down封装。

```python
class PQ_Heap(PriorityQueue):
    def insert(self, *args):
        super().insert(*args)
        n, A = self.n, self.A
        max_heapify_up(A, n, n-1)

    def delete_max(self):
        n, A = self.n, self.A
        A[0], A[n] = A[n], A[0]
        max_heapify_down(A, n, 0)
        return super().delete_max()
```

之前我们定义了max_heapify操作，我们需要函数来计算parent和child索引（给定索引代表树中节点，它的根是数组中首个元素）。在这个实现中，如果计算的索引超出数组边界，返回输入索引。总是返回有效数组索引，而不是抛出错误，可以帮助简化未来代码。

```python
def parent(i):
    p = (i - 1) // 2
    return p if 0 < i else i

def left(i, n):
    l = 2 * i + 1
    return l if l < n else i

def right(i, n):
    r = 2 * i + 2
    return r if r < n else i
```

这是最大堆所作工作的核心。假设除了节点A[i]，A[:n]所有节点满足最大堆属性，使这些函数易于维护最大堆属性。

```python
def max_heapify_up(A, n, c):
    p = parent(c)
    if A[p].key < A[c].key:
        A[c], A[p] = A[p], A[c]
        max_heapify_up(A, n, p)

def max_heapify_down(A, n, p):
    l, r = left(p, n), right(p, n)
    c = l if A[r].key < A[l].key else r
    if A[p].key < A[c].key:
        A[c], A[p] = A[p], A[c]
        max_heapify_down(A, n, c)
```

## $O(n)$构建堆

使用最大堆优先队列重复插入，花费$\sum_{i=0}^nlogi=logn!=O(nlogn)$。我们可以用线性时间构建最大堆，如果整个数组可访问。方法是：按反向层级顺序构建堆，从叶子到根，所有处理过的节点维持最大堆属性（通过每个节点运行max_heapify_down）。作为优化，我们注意到数组后半部分都是叶子，因此我们无需对它们执行max_heapify_down。

```python
def build_max_heap(A):
    n = len(A)
    for i in range(n // 2, -1, -1):
        max_heapify_down(A, n, i)
```

可见这个过程花费$O(n)$而不是$O(nlogn)$，我们显式地使用累加计算上边界。推导中，我们使用斯特林公式（Stirling’s approximation）：$n!=\Theta(\sqrt{n}(n/e)^n)$。

$T(n)<\sum_{i=0}^n(logn-logi)=log(\frac{n^n}{n!})=O(log(\frac{n^n}{\sqrt{n}(n/e)^n}))=O(log(e^n/\sqrt{n}))=O(nloge-log\sqrt{n})=O(n)$

使用这个线性方法构建最大堆，不会影响堆排序性能，因为delete_max删除n中每个元素花费$O(logn)$。但对初始化写入n个项目到空堆来说，这确实是更有效的方法。

## In-Place堆

为了堆排序是in-place（也是为了恢复选择排序、插入排序的in-place属性），我们可以更改基类PriorityQueue，取整个数组A，维护队列在A的前n个元素中（$n<=len(A)$）。insert函数不再接收值用于插入；而是插入已经存储在A[n]的元素，将其合并成为更大队列。相似地，delete_max不会返回值，它仅仅是在缩小它尺寸前，放置它的输出到A[n]。这个方式，仅对这种情形起作用：在n个delete_max之前进行n个insert操作，正如优先队列排序。

```python
class PriorityQueue:
    def __init__(self, A):
        self.n, self.A = 0, A

    def insert(self):
        if not self.n < len(self.A):
            raise IndexError('insert into full priority queue')
        self.n += 1

    def delete_max(self):
        if self.n < 1:
            raise IndexError('pop from empty priority queue')
        self.n -= 1

    @classmethod
    def sort(Queue, A):
        pq = Queue(A)
        for i in range(len(A)):
            pq.insert()
        for i in range(len(A)):
            pq.delete_max()
        return pq.A
```

这个新基类用于任意子类（PQ_Array,PQ_SortedArray,PQ_Heap）的排序。前2个排序算法更接近原始的选择排序和插入排序，最后的算法通常指的是堆排序。