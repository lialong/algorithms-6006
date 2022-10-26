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
        <td>顺序（order）</td>
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
