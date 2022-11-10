# 一、集合接口（L03-L08）

| 类型            | 方法                                                                     |                                                                              |
| ------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 容器（container） | build(x)<br>len()                                                      | 给定一个可迭代的X，通过X中的项目构建集合<br>返回存储项目的数量                                           |
| 静态（static）    | find(k)                                                                | 返回键为key的项目                                                                   |
| 动态（dynamic）   | insert(x)<br>delete(k)                                                 | 添加x到集合（如果已经存在，取代值为x.key的项目）<br>移除并返回键为key的项目                                 |
| 顺序（order）     | iter_ord()<br>find_min()<br>find_max()<br>find_next(k)<br>find_prev(k) | 以键值顺序挨个返回存储的项目<br>返回拥有最小键的项目<br>返回拥有最大键的项目<br>返回比k大的最小键项目<br>返回比k小的最大键项目<br> |

以任意顺序把项目存到数组中，可以实现一个集合（不是特别有效）

按key升序存储项目允许：

更快找到最大/最小值（数组开头、结尾）

通过二分查找更快查找：$\mathcal{O}(logn)$

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
        <td colspan=2>顺序（order）</td>
    </tr>
    <tr>
        <td>build(x)</td>
        <td>find(k)</td>
        <td>insert(x)<br>delete(x)</td>
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

但如何构建有效地构建有序数组？

# 二、排序

给定一个有序数组，我们可以二分查找来构造一个有效的集合数据结构

输入：静态数组A

输出：静态数组B，排序组合后的A

    组合：有相同元素、不同顺序的数组

    排序：$B[i − 1] ≤ B[i]，i \in \{1, . . . , n\}$

举例：[8,2,4,9,3] -> [2,3,4,8,9]

如果覆盖A，那么排序是破坏性的（destructive），不会产生新数组B，而是有序版本的A

如果使用$\mathcal{O}(1)$额外空间，那么排序是就地的（in place），就地意味着破坏性，$in place \subseteq destructive$

# 三、全排序（Permutation Sort）

有n!个A的排列组合，至少其中1个是有序的

对于每种排列组合，检查是否有序：$\theta(n)$

例子：[2,3,1]->{[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]}

```python
def permutation_sort(A):
    '''Sort A'''
    for B in permutations(A):    # O(n!)
        if is_sorted(B)          # O(n)
            return B             # O(1)
```

permutation_sort分析：

    经case分析，这是正确的：尝试所有可能（暴力）

    运行时间：$\Omega(n!\cdot n)$，这是指数级的

# 四、解决递归（solving recurrence）

置换（substitution）：猜测一个方案，用代表函数替代，递归成立

递归树（recurrence tree）：画一个树代表递归调用，所有节点计算求和

主定理（master theorem）：解决一些递归的公式（R03）

# 五、选择排序（selection sort）

找到前A[:i+1]最大的数，交换到A[i]

递归排序前A[:i]

举例：[8,2,4,9,3],[8,2,4,3,9],[3,2,4,8,9],[2,3,4,8,9]

```python
def selection_sort(A, i = None):              # T(i)
    '''Sort A[:i+1]'''
    if i is None: i = len(A) - 1              # O(1)
    if i > 0:                                 # O(1)
        j = prefix_max(A, i)                  # S(i)
        A[i], A[j] = A[j], A[i]               # O(1)
        selection_sort(A, i - 1)              # T(i - 1)

def prefix_max(A, i):                         # S(i)
    '''Return index of maximum in A[:i+1]'''
    if i > 0                                  # O(1)
        j = prefix_max(A, i - 1)              # S(i - 1)
        if A[i] < A[j]:                       # O(1)
            return j                          # O(1)
    return i                                  # O(1)
```

prefix_max分析：

基本情形：i=0，数组有1个元素，因此最大索引为i

归纳：假设i时正确，最大的要么是A[:i]中最大的、要么是A[i]，任意情形返回正确索引

$S(1) = \theta(1),S(n)=S(n-1)+\theta(1)$

    取代：$S(n)=\theta(n)，cn=\theta(1)+c(n-1) =>1=\theta(1)$

    递归树：n个节点的链，每个节点处有$\theta(1)$工作量，$\sum_{i=0}^{n-1}=\theta(n)$

selection_sort分析：

基本情形：对于i=0，数组有一个元素，因此是有序的

归纳：假设i时正确，有序输出的最后一个数是数组中最大的数，算法把它放在了那，那么根据归纳A[:i]是有序的

$T(1) = \theta(1),T(n)=T(n-1) + \theta(n)$

    取代：$T(n)=\theta(n^2)，cn^2=\theta(n)+c(n-1)^2=>c(2n-1)=\theta(n)$

    递归树：n个节点的链，每个节点处有$\theta(n)$工作量，$\sum_{i=0}^{n-1}=\theta(n^2)$

# 六、插入排序（insertion sort）

递归排序前A[:i]

排序前A[:i+1]，假设前A[:i]被重复交换进而有序

举例：[8,2,4,9,3],[2,8,4,9,3],[2,4,8,9,3],[2,4,8,9,3],[2,3,4,8,9]

```python
def insertion_sort(A, i = None):            # T(i)
    '''Sort A[:i+1]'''
    if i is None: i = len(A) - 1            # O(1)
    if i > 0                                # O(1)
        insertion_sort(A, i - 1)            # T(i - 1)
        insert_last(A, i)                   # S(i)


def insert_last(A, i):                      # S(i)
    '''Sort A[:i+1] assuming sorted A[:i]'''
    if i > 0 and A[i] < A[i - 1]:           # O(1)
        A[i], A[i - 1] = A[i - 1], A[i]     # O(1)
        insert_last(A, i - 1)               # S(i - 1)
```

insert_last分析：

基本情形：对于i=0，数组有一个元素，因此是有序的

归纳：假设i时成立，如果A[i] >= A[i - 1]，数组是有序的。否则交换最后两个元素，允许我们通过归纳对A[:i]排序

$S(1)=\theta(1),S(n)=S(n-1)+\theta(1)=>S(n)=\theta(n)$

insertion_sort分析：

基本情形：对于i=0，数组有一个元素因此是有序的

归纳：假设i时成立，根据归纳算法排序A[:i]，然后insert_last正确地排序（正如上面证明的那样）

$T(1)=\theta(1),T(n)=T(n-1)+\theta(n)=>T(n)=\theta(n^2)$

# 七、归并排序（merge sort）

递归排序前半部分和后半部分（可能假设是2的指数）

归并排序，把两个半边合成一个有序list

举例：[7,1,5,6,2,4,9,3], [1, 7, 5, 6, 2, 4, 3, 9], [1, 5, 6, 7, 2, 3, 4, 9], [1, 2, 3, 4, 5, 6, 7, 9]

```python
def merge_sort(A, a = 0, b = None):                    # T(b - a = n)
    '''Sort A[a:b]'''
    if b is None: b = len(A)                           # O(1)
    if 1 < b - a                                       # O(1)
        c = (a + b + 1) // 2                           # O(1)
        merge_sort(A, a, c)                            # T(n / 2)
        merge_sort(A, c, b)                            # T(n / 2)
        L, R = A[a:c], A[c:b]                          # O(n)
        merge(L, R, A, len(L), len(R), a, b)           # S(n)

def merge(L, R, A, i, j, a, b):                        # S(b - a = n)
    '''Merge sorted L[:i] and R[:j] into A[a:b]'''
    if a < b:                                          # O(1)
        if (j <= 0) or (i > 0 and L[i-1] > R[j-1]):    # O(1)
            A[b - 1] = L[i - 1]                        # O(1)
            i = i -1                                   # O(1)
        else:                                          # O(1)
            A[b - 1] = R[j - 1]                        # O(1)
            j = j - 1                                  # O(1)
        merge(L, R, A, i, j, a, b - 1)                 # S(n - 1)
```

merge分析：

基本情形：对于n=0，数组为空，完全正确

归纳：假设n时正确，A[r]必须是剩下的L、R前面的中最大的数，因此他们是有序的，找出后面满足元素中最大的。剩下的根据归纳被合并。

$S(0)=\theta(1),S(n)=S(n-1)+\theta(1)=>S(n)=\theta(n)$

merge_sort分析：

基本情形：对于n=1，数组没有元素，因此是有序的

归纳：假设k<n时正确，根据归纳，算法把更小的一半进行排序，然后merge方法将两部分归并成一个有序数组

$T(1)=\theta(1),T(n)=2T(n/2)+\theta(n)$

取代：假设$T(n)=\theta(nlogn),cnlogn=\theta(n)+2c(n/2)log(n/2)=>cnlog(2)=\theta(n)$

递归树：二叉树有深度：$log_2n$，叶子：n，level i有$2^i$个节点，每个节点需要$\mathcal{O}(n/2^i)$工作，总共$\sum_{i=0}^{log_2n}(2^i)(n/2^i)=\sum_{i=0}^{log_2n}n=\theta(n)$

# 八、详述（recitation）

回想在recitation2中，我们将Set接口简化为Sequence接口（我们用一个模拟另外一个）。这直接由数组提供Set数据结构（尽管很简陋）。

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
</table>
</div>

我们想做地更好，我们将花费5节lecture/recitation，来尝试精准地实现它。获取一个更快的集合，最简单的方式之一是：把我们的项目存储到一个有序数组中，有最小key的项目出现在头部（index 0），有最大key的项目出现在尾部。我们能简单地二分查找来找key，且支持有序操作。这对于动态操作仍然不太好（在数组中插入、删除时，items仍然需要被移动），但通过他们的key找items是更快的！首先，我们如何获取一个有序数组呢？

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
        <td>有序数组</td>
        <td>?</td>
        <td>logn</td>
        <td>n</td>
        <td>1</td>
        <td>logn</td>
    </tr>
</table>
</div>

```python
class Sorted_Array_Set:
    def __init__(self):    self.A = Array_Seq()    #O(1)
    def __len__(self):     return len(self.A)      #O(1)
    def __iter__(self):    yield from self.A       #O(n)
    def iter_order(self):  yield from self         #O(n)

    def build(self, X):                            #O(?)
        self.A.build(X)
        self._sort()

    def _sort(self):
        ??                                         #O(?)

    def _binary_search(self, k, i, j):             #O(log n)
        if i >= j:    return i
        m = (i + j) // 2
        x = self.A.get_at(m)
        if x.key > k:    return self._binary_search(k, i, m - 1)
        if x.key < k:    return self._binary_search(k, m + 1, j)
        return m

    def find_min(self):                            #O(1)
        if len(self) > 0:    return self.A.get_at(0)
        else:    return None

    def find_max(self):
        if len(self) > 0:    return self.A.get_at(len(self) - 1)
        else:    return None

    def find(self, k):                             # O(log n)
        if len(self) == 0    return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key == k:    return x
        else:    return None

    def find_next(self, k):
        if len(self) == 0:    return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key > k:    return x
        if i + 1 < len(self):    return self.A.get_at(i+1)
        else:    return None

    def find_prev(self, k):
        if len(self) == 0:    return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key < k:    return x
        if i > 0:    return self.A.get_at(i - 1)
        else:    return None

    def insert(self, x):
        if len(self.A) == 0:
            self.A.insert_first(x)
        else:
            i = self._binary_search(x.key, 0, len(self.A) - 1)
            k = self.A.get_at(i).key
            if k == x.key:
                self.a.set_at(i, x)
                return False
            if k > x.key:    self.A.insert_at(i, x)
            else:    self.A.insert_at(i, x)
        return True

    def delete(self, k):
        i = self._binary_search(k, 0, len(self.A) - 1)
        assert self.A.get_at(i).key == k
        return self.A.delete_at(i)
```

## 排序（Sorting）

对可比较项目构成的数组A进行升序排序，是众多计算问题中的常见子任务。插入排序和选择排序是常见的少量项目排序算法，因为它们易于理解和实现。两个算法都是递增的，它们保存、增长一个有序的项目子集，直到所有项目有序。它们之间的不同是细微的：

选择排序，保存、增长一个子集，最大的i个项目有序地处于其中

选择排序，保存、增长一个子集，前i个项目是有序的

## 选择排序（Selection Sort）

这是选择排序的python实现。已经让处于子数组A[i+1:]中的最大项目有序，算法重复地扫描数组，找出尚未排序的最大的项目，并使其与项目item[i]交换。正如从代码中看到的，选择排序会需要$\Omega(n^2)$次比较，但最坏情形下最多执行$\mathcal{O}(n)$次交换。

```python
def selection_sort(A):
    for i in range(len(A) - 1, 0, -1):
        m = i
        for j in range(i)
            if A[m] < A[j]:
                m = j
        A[m], A[i] = A[i], A[m]
```

## 插入排序（Insertion Sort）

这是插入排序的python实现。已经让子数组A[:i]有序，算法重复地交换项目A[i]与其左侧，直到左侧项目不再大于A[i]。正如可在代码中看到的那样，最坏情形下，插入排序需要$\Omega(n^2)$次比较、$\Omega(n^2)$次交换。

```python
def insertion_sort(A):
    for i in range(1, len(A)
        j = i
        while j > 0 and A[j] < A[j - 1]:
            A[j - 1], A[j] = A[j], A[j - 1]
            j = j - 1
```

## in-place和stability

插入排序和选择排序都是就地算法，意味着它们每个，可以用常量额外空间被实现。执行在数组上的仅有操作是比较，以及成对元素之间的交换。插入排序是稳定的，意味着：拥有相同值的项目，将以与输入数组相同顺序，出现在排序中。通过比较，选择排序实现是非稳固的。例如：输入(2,1,1')会产生输出(1`,1,2)。

## 归并排序

在本课中，我们介绍归并排序(merge sort)，一个用于排序更大数量项目的更快算法。这个算法是递归排序数组左半部分和右半部分，然后以线性时间归并两半部分。归并排序的递归关系是$T(n)=2T(n/2)+\theta(n)$，得到$T(n)=\theta(nlogn)$。比起次方，$\theta(nlogn)$渐近增长率是更接近线性的，正如$logn$指数性慢于n。特别地，$logn$增长慢于任意$n^\epsilon(\epsilon>0)$。

```python
def merge_sort(A, a = 0, b = None):
    if b is None
        b = len(A)
    if 1 < b - a
        c = (a + b + 1) // 2
        merge_sort(A, a, c)
        merge_sort(A, c, b)
        L, R = A[a:c], A[c:b]
        i, j = 0, 0
        while a < b:
            if (j > = len(R)) or (i < len(L) and L[i] < R[j]):
                A[a] = L[i]
                i = i + 1
            else:
                A[a] = R[j]
                j = j + 1
            a = a + 1
```

当组合两个半边时，归并排序使用线性数量的临时存储，因此它并非in-place。已经存在算法执行归并，不使用额外空间，这个实现比起归并排序算法更复杂。归并排序是否是稳固的，取决于归并时实现如何打破绑定。上面的实现是非稳固的，但它用小小的改变可以变得稳固。

## 递归

有3个解决递归的主要方法：

取代：猜测一个答案，代入递归表达式

递归树：画一颗树，代表递归、节点处的求和运算。这是一个非常通用的方法，也是至今我们在课上用到过的。

主定理：解决大量递归的通用公式，它是有用的，但也是难以被记住的。

主定理提供一种解决递归关系的方式，递归调用通过常量因子降低问题尺寸。给定递归关系：$T(n)=aT(n/b)+f(n)，T(1)=\theta(1)$，分支因子a>=1，问题尺寸减少因子b>1，以及渐近性非负函数$f(n)$，主定理通过比较$f(n)$和$a^{log_bn}=n^{log_ba}$（递归树底部叶子数量）。当$f(n)$渐进式增长快于$n^{log_ba}$，每级要做的工作几何减少，因此工作由根部控制；当$f(n)$增长更慢，每级要做的工作几何增长，工作由叶子控制。当它们的增长率是可比较的，工作平摊在树的$\mathcal{O}(logn)$叶子上。

$T(n)=\theta(n^{log_ba})，条件：f(n)=\mathcal{O}(n^{log_ba-\epsilon}),\epsilon>0 \\T(n)=\theta(n^{log_ba}log^{k+1}n)，条件：f(n)=\mathcal{O}(n^{log_ba}log^kn),k>=0 \\T(n)=\theta(f(n))，条件：f(n)=\mathcal{O}(n^{log_ba+\epsilon}),\epsilon>0且af(n/b)<cf(n)，0<c<1$

主定理采用一个更简单的形式，当f(n)是多项式，递归：$T(n)=aT(n/b)+\theta(n^c)$

$T(n)=\theta(n^{log_ba}),c<log_ba,叶子支配$

$T(n)=\theta(n^clogn),c=log_ba,整个树支配$

$T(n)=\theta(n^c),c>log_ba,根支配$

特殊情形直接由取代法证明（这可以在recitation中完成）。为了应用主定理（或更简单的特殊情形），你应该说明哪种情形适用，并且表示：你的递归关系满足相关case的所有条件。甚至有更强的公式来解决递归，但我们不在本课使用。

## 习题

写一个递归用于二分查找并解决它

$T(n)=T(n/2)+\mathcal{O}(1)$

$T(n)=\mathcal{O}(\log n)$，符合情形2

-----------------------------------------------------------

$T(n)=T(n-1)+\mathcal{O}(1)$

$T(n)=\mathcal{O}(n)$，长度为n的链，每个节点$\mathcal{O}(1)$

---

$T(n)=T(n-1)+\mathcal{O}(n)$

$T(n)=\mathcal{O}(n^2)$，长度为n的链，高度为k时，每个节点$\mathcal{O}(k)$工作

---

$T(n)=2T(n-1)+\mathcal{O}(1)$

$T(n)=\mathcal{O}(2^n)$，高度为n的二叉树，每个节点$\mathcal{O}(1)$工作

---

$T(n)=T(2n/3)+\mathcal{O}(1)$

$T(n)=\mathcal{O}(\log n)$，长度为$log_{3/2}(n)$的链，每个节点$\mathcal{O}(1)$工作

---

$T(n)=2T(n/2)+\mathcal{O}(1)$

$T(n)=\mathcal{O}(n)$，高度为$log_2n$的二叉树，每个节点$\mathcal{O}(1)$工作

---

$T(n)=T(n/2)+\mathcal{O}(n)$

$T(n)=\mathcal{O}(n)$，长度为$log_2n$的链，高度为k时，每个节点$\mathcal{O}(2^k)$工作

---

$T(n)=2T(n/2)+\mathcal{O}(nlogn)$

$T(n)=\mathcal{O}(nlog^2n)$）（主定理的特殊情形不适用，因为nlogn不是多项式），高度为$log_2n$的二叉树，高度为k时，每个节点$\mathcal{O}(k*2^k)$工作

---

$T(n)=4T(n/2)+\mathcal{O}(n)$

$T(n)=n^2$，高度$log_2n$的4叉树，高度为k时，每个节点$\mathcal{O}(2^k)$工作
