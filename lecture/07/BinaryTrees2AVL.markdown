# 一、上次与今日目标

<div>
<table>
    <tr>    
        <td rowspan=3>序列数据结构</td>
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
        <td>二叉树</td>
        <td>n</td>
        <td>h</td>
        <td>h</td>
        <td>h</td>
        <td>h</td>
    </tr>
    <tr>
        <td>AVL树</td>
        <td>n</td>
        <td>logn</td>
        <td>logn</td>
        <td>logn</td>
        <td>logn</td>
    </tr>
</table>
</div>

<div>
<table>
    <tr>    
        <td rowspan=3>集合数据结构</td>
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
        <td>二叉树</td>
        <td>nlogn</td>
        <td>h</td>
        <td>h</td>
        <td>h</td>
        <td>h</td>
    </tr>
    <tr>
        <td>AVL树</td>
        <td>nlogn</td>
        <td>logn</td>
        <td>logn</td>
        <td>logn</td>
        <td>logn</td>
    </tr>
</table>
</div>

# 二、高度平衡

* 如何维持高度$h=\mathcal{O}(\log n)$，n为树中节点的数量

* 在动态操作中维持树的高度为$\mathcal{O}(\log n)$的二叉树称为平衡的
  
  * 有多种平衡方式（红黑树、伸展树SplayTree、2-3Tree）
  
  * 首次提出平衡策略的是AVL树

# 三、旋转（Rotations）

* 需要降低树的高度，而不改变遍历顺序，因此我们表示相同序列的项目

* 保留遍历顺序时，如何改变树的结构？旋转！

```mermaid
graph TB;
    D-->B;
    D-->E;
    B-->A;
    B-->C;
```

```mermaid
graph TB;
    B-->A;
    B-->D;
    D-->C;
    D-->E;
```

图1 rotate_right(\<D\>) 得到图2、图2 rotate_left(\<B\>) 得到图2

* 旋转重新链接$\mathcal{O}(1)$指针更改树结构、维持遍历顺序

# 四、Rotations Suffice

* 声明：$\mathcal{O}(n)$次旋转可以转换二叉树为任意其他二叉树（拥有相同遍历顺序）

* 证明：按遍历顺序重复执行最后可能的右旋；结果树为经典的链表。每次旋转最后节点的深度增加1。最终链中最后节点的深度为$n-1$，因此最多执行n-1次旋转。反向旋转得到目标树

* 通过使用$\mathcal{O}(n)$次旋转，可以维持高度平衡来完全平衡二叉树，但很慢

* 每次操作，我们将耗时$\mathcal{O}(\log n)$维持树的平衡

# 五、AVL树：高度平衡

* AVL树维持高度平衡（也称作AVL属性）
  
  * 如果左、右子树高度最多相差1，那么节点是高度平衡的
  
  * 让节点的偏斜为右子树高度减左子树高度
  
  * 如果它的偏斜为-1、0、1，那么节点是高度平衡的

---

* 声明：拥有高度平衡节点的二叉树，高度为$h=\mathcal{O}(\log n)，比如n=2^{\Omega(h)}$

* 证明：任意高度为h的树，最少节点$F(h)=2^{\Omega(h)}$
  
  F(0)=1，F(1)=2，F(h)=1+F(h-1)+F(h-2) >= 2F(h-2) => $F(h)\ge2^{h/2}$

---

* 假设从高度平衡树中添加或删除叶子导致不平衡
  
  * 仅叶子祖先的子树高度改变或歪曲
  
  * 改变高度仅为1，因此倾斜幅度$\le$2
  
  * 点子：从叶子到根，修复祖先的高度平衡
  
  * 重复地再平衡（高度不平衡的）最低祖先

* 本地再平衡：给定二叉树节点\<B\>：
  
  * 倾斜为2且
  
  * \<B\>子树的每个其他节点是高度平衡的，
  
  * \<B\>的子树可以通过一次或2次旋转达到高度平衡
  
  * （之后，\<B\>的高度将等于或小于之前的高度）

* 证明：
  
  * 因为B的倾斜是2，所以\<B\>的右子树\<F\>存在
  
  * case1:\<F\>的倾斜是0、或case2：\<F\>的倾斜是1
    
    * 在\<B\>上执行左旋
    
    ![](https://raw.githubusercontent.com/lialong/algorithms-6006/main/lecture/07/1.png)
    
    * 让h=height(\<A\>)，那么height(\<G\>)=h+1，并且height(\<D\>)是h+1(case1)或h(case2)
    * 旋转后：
      * \<B\>的倾斜要么是1(case1)，要么是0(case2)，因此\<B\>是高度平衡的
      * \<F\>的倾斜是-1或0，因此\<F\>是高度平衡的
      * 子树的高度之前是h+3，之后为h+3(case1)、h+2(case2)
  
  * case3：\<F\>的倾斜是-1，因此\<F\>的左子节点\<D\>存在
    
    * 在\<F\>上执行右旋，然后在\<B\>上执行左旋
    
    ![](https://raw.githubusercontent.com/lialong/algorithms-6006/main/lecture/07/2.png)
    
    * 让h=height(\<A\>)。那么height(\<G\>)=h，height(\<C\>)和height(\<E\>)是h或h-1
    * 旋转后：
      * \<B\>的倾斜是0或-1，因此\<B\>的高度是平衡的
      * \<F\>的倾斜是0或1，因此\<F\>的高度是平衡的
      * \<D\>的倾斜是0，因此D是高度平衡的
      * 子树的高度之前是h+3，那么之后是h+2

* 全局再平衡：从高度平衡树T中添加或删除一个叶子生成树T'。然后T‘可以使用至多$\mathcal{O}(\log n)$次旋转转换成一个高度平衡树T''

* 证明：
  
  * 仅受影响叶子的祖先，T'比T有不同的高度
  
  * 受影响叶子至多$h=\mathcal{O}(\log n)$个祖先（它的子树可能已经改变）
  
  * 让\<X\>为最低的高度不平衡祖先（倾斜度是2）
  
  * 如果一个叶子加到T：
    
    * 插入增加\<X\>的高度，因此是不平衡的case2或case3
    
    * 旋转降低子树的高度：1次旋转后平衡
  
  * 如果叶子从T中移除：
    
    * 删除使\<X\>子节点的高度降低1，并非\<X\>，因此不平衡
    
    * 可能让\<X\>的高度降低1；\<X\>的父级可能变不平衡
    
    * 因此可能不得不再平衡\<X\>的每个祖先，但至多它们中的h=$\mathcal{O}(\log n)$个

* 因此，在插入/删除之后，仅使用$\mathcal{O}(\log n)$次旋转就可以维持高度平衡

* 但需要我们评估$\mathcal{O}(\log n)$个节点是否是高度平衡的

# 六、计算高度

* 如何得知节点\<X\>是高度平衡的？计算子树的高度！

* 如何计算节点\<X\>的高度？直接的算法：
  
  * 递归地计算\<X\>左右子树的高度
  
  * 两个高度中的最大值加1
  
  * 运行时间为$\Omega(n)$，因为我们在每个节点上递归

* 点子：在每个节点处增加其子树的高度

* 在动态操作期间，我们必须随着树改变形状维持扩展

* 在每个节点的子树改变时，重新计算子树的扩展
  
  * 对在旋转操作中重新链接的点进行更新，花费$\mathcal{O}(1)$，祖先不改变
  
  * 通过向上遍历树，更新插入/删除节点的所有祖先，花费$\mathcal{O}(h)$

# 七、扩充二叉树的步骤

* 通常，用子树属性P来扩充二叉树，你必须：
  
  * 声明子树属性P(\<X\>)，你想在每个节点\<X\>处存储它
  
  * 展示如何花费$\mathcal{O}(1)$,从\<X\>的孩子的扩展中计算P(\<X\>)

* 那么存储的属性P(\<X\>)可以被维持，不会改变动态操作的消耗

# 八、应用：序列

* 对于序列二叉树，我们需要知道子树尺寸

* 插入/删除叶子，这是简单的，但现在需要处理旋转

* 子树的尺寸是一个子树属性，因此可以通过扩展进行维持
  
  * 可以通过孩子的尺寸来计算，把孩子尺寸相加，并加1

# 九、总结

* AVL树，对所有集合操作，实现花费$\mathcal{O}(\log n)$，除了构建:$\mathcal{O}(n\log n)$，遍历:$\mathcal{O}(n)$

* AVL树，对所有序列操作，实现花费$\mathcal{O}(\log n)$，除了构建:$\mathcal{O}(n)$，遍历:$\mathcal{O}(n)$

# 十、应用：排序

* 任意集合数据结构定义了一个排序算法：构建(重复地插入)、遍历

* 举例：lecture5中的直接访问数组

* AVL排序是一个新的$\mathcal{O}(n\log n)$时间复杂度的排序算法

# 十一、Recitation

## 平衡的二叉树

之前，我们讨论二叉树作为一个通用数据结构，用于存储项目，不会限制树的最大高度。最终目的变为：保持我们的树平衡，如果高度为$\mathcal{O}(\log n)$，n节点的树是平衡的。那么所有我们上次讨论的花费$\mathcal{O}(h)$时间的操作，将仅花费$\mathcal{O}(\log n)$。

有许多种方式，在插入和删除时，来维持二叉树的平衡（红黑树、B-树、2-3树、伸展树等等）。最早（可能也是最简单的）的方式称作AVL树。AVL树上的每个节点都是高度平衡的（满足AVL属性），高度平衡节点的左右子树，其高度最多相差1。另外的表达，定义斜率为：右子树的高度-左子树的高度，空子树的高度为-1。若它的斜率是-1、0、1，那么这个节点是高度平衡的。若树的每个节点是高度平衡的，则树是高度平衡的。高度平衡是好的，因为它意味着平衡。

### 练习

高度平衡的二叉树是平衡的

解法：平衡意味着：h=$\mathcal{O}(\log n)$。等价得，平衡意味着logn以$\Omega(h)$为下界，因此$n=2^{\Omega(h)}$。如果我们可以展示，高度平衡树的最小的节点数，至少为h指数次方，那么它必定是平衡的。让F(h)为任意高度平衡树(高度为h)的最少节点。那么F(h)满足以下递归：

F(h)=1+F(h-1)+F(h-2)>=2F(h-2)

因为根的子孙的子树应该也包含最少的节点。基于基础情形，高度平衡树(高度为0)的最少节点为1，F(0)=1，高度平衡树(高度为1)的最少节点为2，F(1)=2。那么这个递归的下边界为：

$F(h)>=2^{h/2}=2^{\Omega(n)}$

## 旋转

当我们对树添加或删除节点时，可能：我们的树将变得不平衡。我们想要改变树的结构，而不改变它的遍历顺序，希望我们能让树的结构更平衡。我们能用局部操作——旋转，改变树的结构。子树发生的旋转，看起来就像下面的两个配置，花费$\mathcal{O}(1)$更改节点之间的连接，从一个配置转换为另外一个配置。

![](http://raw.githubusercontent.com/lialong/algorithms-6006/main/lecture/07/3.png)

这个操作保留了树的遍历顺序，但却改变了子树\<A\>、\<E\>中所有节点的深度。接下来，我们将使用旋转来保证：插入或删除一个节点后，平衡树仍然维持平衡。

```python
def subtree_rotate_right(D):
    assert D.left
    B, E = D.left, D.right
    A, C = B.left, B.right
    D, B = B, D
    D.item, B.item = B.item, D.item
        B.left, B.right = A, D
    D.left, D.right = C, E
    if A: A.parent = B
    if E: E.parent = D
    # B.subtree_update()
    # D.subtree_update()

def subtree_rotate_left(B):
    assert B.right
    A, D = B.left, B.right
    C, E = D.left, D.right
    B, D = D, B
    B.item, D.item = D.item, B.item
    D.left, D.right = B, E
    B.left, B.right = A, C
    if A: A.parent = B
    if E: E.parent = D
    # B.subtree_update()
    # D.subtree_update()
```

## 维持高度平衡

假设我们有一个高度平衡的AVL树，我们通过添加或删除叶子，执行单个插入或删除操作。要么结果树仍然是高度平衡的，要么叶子上的改变，至少让树上的1个节点的倾斜大于1。特别地，这些节点（位于叶子更改后子树发生改变的树中）是叶子的祖先（至多$\mathcal{O}(h)$），因此它们是仅有的，斜率发生改变（从至多1到至多2）。正如lecture中展示的那样，通过一个简要的case分析，给定一个子树，它的根斜率为2，子树中其他节点是高度平衡的，我们可以通过至多两次旋转恢复子树平衡。因此为了再平衡整个树，沿着叶子向根走，能够再平衡路径上的每个节点，总共至多执行$\mathcal{O}(\log n)$次旋转。详细的证明列在lecture笔记中，此处不再重复。如果学生想看完整的扩展，那么证明也可以在recitation中回顾一下。下面是实现lecture中再平衡算法的代码。

```python
def skew(A):
    return height(A.right) - height(A.left)

def rebalance(A):
    if A.skew() == 2:
        if A.right.skew() < 0:
            A.right.subtree_rotate_right()
            A.subtree_rotate_left()
    elif A.skew() == -2:
        if A.left.skew() > 0:
            A.left.subtree_rotate_left()
        A.subtree_rotate_right()

def maintain(A):
    A.rebalance()
    A.subtree_update()
    if A.parent: A.parent.maintain()
```

不幸地是，无法有效地评估节点斜率，来决定是否需要执行旋转，因为计算一个节点的高度，天然地花费子树尺寸的线性时间。下面的代码递归地计算子树\<A\>中每个节点的高度，因此至少花费$\mathcal{O}(n)$。

```python
def height(A):
    if A is None: return -1
    return 1 + max(height(A.left), height(A.right))
```

最坏情形下，再平衡需要我们检查至少$\Omega(\log n)$高度，因此如果我们想再平衡树，至多花费$\mathcal{O}(\log n)$，我们需要能够花费$\mathcal{O}(1)$评估节点的高度。不是我们每次需要它的时候计算节点高度，我们将通过扩展加速计算：特别地，每个点存储、维护了它自己子树的高度。那么我们处于该点时，评估它的高度就像读取它存储的值一样简单，花费$\mathcal{O}(1)$。然而，当树的结构发生改变时，我们将需要更新、并重算节点（高度发生改变）的高度。

```python
def height(A):
    if A:    return A.height
    else:    return -1

def subtree_update(A):
    A.height = 1 + max(height(A.left), height(A.right))
```

R06中的动态操作，我们让注释的代码，在每个节点更新时（它的子树在插入、删除、旋转时）发生调用。一个再平衡插入或删除操作，仅在至多$\mathcal{O}(\log n)$节点处调用subtree_update，基于节点子孙存储的扩展，更新一个节点花费至多$\mathcal{O}(1)$来重算扩展，那么扩展可以花费$\mathcal{O}(\log n)$在再平衡时被维持。

总的来说，扩展背后的想法是：在每个节点处存储额外的信息，以便于信息可以在未来被快速查询。你已经在PS1中做了一些扩展，你用一个向后的指针扩展单链表，使其更快地评估节点的前驱。为了用子树属性P(\<X\>)来扩展二叉树的节点，你需要：

* 清晰地定义\<X\>子树的什么属性对应P(\<X\>)

* 展示如何从\<X\>子孙的扩展中，花费$\mathcal{O}(1)$计算P(\<X\>)

如果你可以做到，那么你将能存储并维持每个节点处的属性，不会影响再平衡插入/删除的运行时间$\mathcal{O}(\log n)$。我们已经展示了如何遍历二叉树，并执行插入、删除，每个花费$\mathcal{O}(h)$，维持了高度平衡，因此$h=\mathcal{O}(\log n)$。现在我们最终准备好了实现一个有效地序列和集合。

## AVL平衡二叉树实现

```python
def height(A):
    if A:    return A.height
    else:    return -1

class Binary_Node:
    def __init__(A, x):
        A.item = x
        A.left = None
        A.right = None
        A.parent = None
        A.subtree_update()

    def subtree_update(A):
        A.height = 1 + max(height(A.left),height(A.right))

    def skew(A):
        return height(A.right) - height(A.left)

    def subtree_iter(A):
        if A.left:    yield from A.left.subtree_iter()
        yield A
        if A.right:    yield from A.right.subtree_iter()

    def subtree_first(A):
        if A.left:    return A.left.subtree_first()
        else:         return A

    def subtree_last(A):
        if A.right:    return A.right.subtree_last()
        else:         return A

    def successor(A):
        if A.right:    return A.right.subtree_first()
        while A.parent and (A is A.parent.right)
            A = A.parent
        return A.parent

    def predecessor(A):
        if A.left:    return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A = A.parent

    def subtree_insert_before(A, B):
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B, A
        else:
            A.left, B.parent = B, A
        A.maintain()

    def subtree_insert_after(A, B):
        if A.right:
            A = A.right.subtree_first()
        else:
            A.right, B.parent = B, A
        A.maintain()

    def subtree_delete(A):
        if A.left or A.right:
            if A.left:    B = A.predecessor()
            else:         B = A.successor()
            A.item, B.item = B.item, A.item
            return B.subtree_delete()
        if A.parent:
            if A.parent.left is A:    A.parent.left = None
            else:                     A.parent.right = None
            A.parent.maintain()
        return A

    def subtree_rotate_right(D):
        assert D.left
        B, E = D.left, D.right
        A, C = B.left, B.right
        D, B = B, D
        D.item, B.item = B.item, D.item
        B.left, B.right = A, D
        D.left, D.right = C, E
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()

    def subtree_rotate_left(B):
        assert B.right
        A, D = B.left, B.right
        C, E = D.left, D.right
        B, D = D, B
        B.item, D.item = D.item, B.item
        D.left, D.right = B, E
        B.left, B.right = A, C
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()

    def rebalance()
        if A.skew() == 2:
            if A.right.skew() < 0:                
                A.right.subtree_rotate_right()
            A.subtree_rotate_left()
        elif A.skew() == -2:
            if A.left.skew() > 0:
                A.left.subtree_rotate_left()
            A.subtree_rotate_right()

    def maintain(A):
        A.rebalance()
        A.subtree_update()
        if A.parent: A.parent.maintain()
```

## 应用：集合

使用我们新的Binary_Node（维持了平衡）定义，R06中Binary_Tree_Set的实现立刻支持所有这些操作花费$h=\mathcal{O}(\log n)$，除了build(X)和iter()，分别花费$\mathcal{O}(n\log n)$、$\mathcal{O}(n)$。这个数据结构正是常说的AVL树，但我们将称之为Set AVL。

## 应用：序列

为了用二叉树实现一个序列接口，我们使用树的遍历顺序，以序列顺序存储项目。现在我们需要一个快速的方式来找到序列中的第i个项目，因为遍历花费$\mathcal{O}(n)$。如果我们知道多少个项目存储在我们的左子树中，我们可以将正在查找的index和该size做比较，在恰当的边上递归。为了有效地计算子树size，我们将树中每个节点的子树size作为一个扩展。节点的size可以被以常量时间计算，将子孙size相加，再加1。

```python
class Size_Node(Binary_Node):
    def subtree_update(A):
        super().subtree_update()
        A.size = 1
        if A.left:    A.size += A.left.size
        if A.right:    A.size += A.right.size

    def subtree_at(A, i):
        assert 0 <= i
        if A.left:         L_size = A.left.size
        else:              L_size = 0
        if i < L_size:     return A.left.subtree_at(i)
        elif i > L_size:   return A.right.subtree_at(i - L_size - 1)
        else:              return A
```

一旦我们能够花费$\mathcal{O}(\log n)$找到平衡二叉树中第i个节点，序列接口中的剩余操作可以使用二叉树操作直接实现。通过R06中的第一个练习，我们可以从输入序列花费$\mathcal{O}(n)$构建这样一个树。我们称这个数据结构为Sequence AVL。

序列和集合接口的实现都可以在以下页面找到。我们已经做了一个CoffeeScript Balanced Binary Tree虚拟化：[Binary Search Trees](https://codepen.io/mit6006/pen/NOWddZ)

```python
class Seq_Binary_Tree(Binary_Tree):
    def __init__(self):    super().__init__(Size_Node)

    def build(self, X):
        def build_subtree(X, i, j):
            c = (i + j) // 2
            root = self.Node_Type(X[c])
            if i < c:
                root.left = build_subtree(X, i, c - 1)
                root.left.parent = root
            if c < j:
                root.right = build_subtree(X, c + 1, j)
                root.right.parent = root
            root.subtree_update()
            return root
        self.root = build_subtree(X, 0, len(X) - 1)
        self.size = self.root.size

    def get_at(self, i):
        assert self.root
        return self.root.subtree_at(i).item

    def set_at(self, i, x):
        assert self.root
        self.root.subtree_at(i).item = x

    def insert_at(self, i, x):
        new_node = self.Node_Type(x)
        if x == 0:
            if self.root:
                node = self.root.subtree_first()
                node.subtree_insert_before(new_node)
            else:
                self.root = new_node
        else:
            node = self.root.subtree_at(i - 1)
            node.subtree_insert_after(new_node)
        self.size += 1

    def delete_at(self, i):
        assert self.root
        node = self.root.subtree_at(i)
        ext = node.subtree_delete()
        if ext.parent is None: self.root = None
        self.size -= 1
        return ext.item

    def insert_first(self, x): self.insert(0, x)
    def delete_first(self): self.delete_at(0)
    def insert_last(self, x): self.insert_at(len(self), x)
    def delete_last(self): self.delete_at(len(self)-1)        
```

## 练习1

通过一个一个地插入选中的学生，生成一个序列或集合AVL树（平衡二叉搜索树）。如果任意节点高度不平衡，再平衡它的所有祖先。这里是一个序列AVL树样例，可能是有指导性的（记得随着更改树，更新子树高度和尺寸）。

```python
T = Seq_Binary_Tree()
T.build([10,6,8,5,1,3])
T.get_at(4)
T.set_at(4, -4)
T.insert_at(4, 18)
T.insert_at(4, 12)
T.delete_at(2)
```

![](https://raw.githubusercontent.com/lialong/algorithms-6006/main/lecture/07/4.png)

## 练习2

维持一个n位的序列，支持两个操作，每个都是$\mathcal{O}(\log n)$时间复杂度。

* flip(i)：flip索引i处的位

* count_ones_upto(i)：到索引i处，值为1的个数。

解法：维持一个序列树，存储bit作为项目，每个节点A处新增：A.subtree_ones，表明子树中1的数量。我们可以花费$\mathcal{O}(1)$从它子节点存储的该值，来维持这个变量。

```python
def update(A):
    A.subtree_ones = A.item
    if A.left:
        A.subtree_ones += A.left.subtree_ones
    if A.right:
        A.subtree_ones += A.right.subtree_ones
```

为了实现flip(i)，使用subtree_node_at(i)找到第i个节点A，flip存储在A.item中的bit。然后更新A以及A的每个祖先（通过沿着树向上）的变量subtree_ones，花费$\mathcal{O}(\log n)$。

为了实现count_ones_upto(i)，我们将首先定义基于子树的递归函数：subtree_count_ones_upto(A, i)，它返回节点A子树中1的数量（A子树内至多索引i）。然后count_ones_upto(i)对应等价为subtree_count_ones_to(T.root, i)。因为每个递归调用，至多在子节点上生成1次递归调用，操作花费$\mathcal{O}(\log n)$。

```python
def subtree_count_ones_upto(A, i):
    assert 0 <= i < A.size
    out = 0
    if A.left:
        if i < A.left.size:
            return subtree_count_ones_upto(A.left, i)
        out += A.left.subtree_ones
        i -= A.left.size
    out += A.item
    if i > 0:
        assert A.right
        out += subtree_count_ones_upto(A.right, i - 1)
    return out
```