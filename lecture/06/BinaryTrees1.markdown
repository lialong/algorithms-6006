# 一、之前与新目标

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
    <tr>
        <td>目标</td>
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
        <td>n(期望)</td>
        <td>1(期望)</td>
        <td>1(期望、分摊)</td>
        <td>n</td>
        <td>n</td>
    </tr>
    <tr>
        <td>目标</td>
        <td>nlogn</td>
        <td>logn</td>
        <td>logn</td>
        <td>logn</td>
        <td>logn</td>
    </tr>
</table>
</div>

# 二、如何达到？二叉树？

* 基于指针的数据结构（像链表）可以实现最坏情形性能

* 二叉树是基于指针的数据结构，每个节点有三个指针

* 节点表示：node.{item,parent,left,right}

* 示例

```mermaid
graph TB;
    A-->B;
    A-->C;
    B-->D;
    B-->E;
    D-->F;
```

<div>
<table>
    <tr>    
        <td>node</td>
        <td>&ltA&gt</td>
        <td>&ltB&gt</td>
        <td>&ltC&gt</td>
        <td>&ltD&gt</td>    
        <td>&ltE&gt</td>
        <td>&ltF&gt</td>
    </tr>
    <tr>    
        <td>item</td>
        <td>A</td>
        <td>B</td>
        <td>C</td>
        <td>D</td>
        <td>E</td>
        <td>F</td>
    </tr>
    <tr>    
        <td>parent</td>
        <td>--</td>
        <td>&ltA&gt</td>
        <td>&ltA&gt</td>
        <td>&ltB&gt</td>
        <td>&ltB&gt</td>    
        <td>&ltD&gt</td>
    </tr>
    <tr>    
        <td>left</td>
        <td>&ltB&gt</td>
        <td>&ltD&gt</td>
        <td>-</td>
        <td>&ltF&gt</td>
        <td>-</td>    
        <td>-</td>
    </tr>
    <tr>    
        <td>right</td>
        <td>&ltC&gt</td>
        <td>&ltE&gt</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>    
        <td>-</td>
    </tr>
</table>
</div>

# 三、术语

* 树的根节点没有父节点（\<A\>）

* 树的叶子节点没有子节点（\<C\>、\<E\>、\<F\>）

* 定义节点\<X\>（位于根节点为\<R\>的树中）的depth(\<X\>)，为\<X\>到\<R\>路径的长度

* 定义节点\<X\>的height(\<X\>)，是以\<X\>为根的子树中，任意节点的最大depth

* 方法：对于根高度为h，设计操作以$\mathcal{O}(h)$时间运行，保持$h=\mathcal{O}(\log n)$

* 二叉树固有的顺序：他的遍历顺序
  
  - 节点<X>左子树中每个节点先于\<X\>
  
  - 节点<X>右子树中每个节点晚于\<X\>

* 通过起始于根节点的递归算法，以遍历顺序列举节点
  
  - 递归列举左子树，列举本身，然后递归列举右子树
  
  - 以$\mathcal{O}(n)$时间运行，因为列举每个节点耗费$\mathcal{O}(1)$
  
  - 举例：遍历顺序：（\<F\>、\<D\>、\<B\>、\<E\>、\<A\>、\<C\>）

* 现在遍历顺序与存储项目无关

* 之后，为遍历顺序分配语义，用来实现 Sequence/Set 接口

# 四、树导航

* 以遍历顺序找出节点\<X\>子树的首个节点（最后节点，跟它是对称的）
  
  - 如果\<X\>有左子节点，递归地返回左子树的首个节点
  
  - 否则，\<X\>是首个节点，因此返回它
  
  - 运行时间是$\mathcal{O}(h)$，h是树的高度
  
  - 举例：\<A\>的子树的首个节点是\<F\>

* 以遍历顺序找出节点\<X\>的后驱节点（前驱节点，跟它是对称的）
  
  - 如果\<X\>有右子树，返回右子树的首个节点
  
  - 否则，返回\<X\>的最低祖先，且\<X\>在它的左子树
  
  - 运行时间是$\mathcal{O}(h)$，h是树的高度
  
  - 举例：后驱，\<B\>对应\<E\>，\<E\>对应\<A\>，C对应None

# 五、动态操作

* 通过单个项目改变树（仅添加或删除叶子）
  
  - 以遍历顺序在另外一个节点之后（之前是对称的），添加一个节点
  
  - 从树中移除一个项目

* 以遍历顺序，在节点\<X\>之后新增节点\<Y\>
  
  - 如果\<X\>没有右子节点，让\<Y\>成为\<X\>的右子节点
  
  - 否则，让\<Y\>成为\<X\>后继节点（不能有左子节点）的左子节点
  
  - 运行时间为$\mathcal{O}(h)$，h是树的高度

* 举例：以遍历顺序，在节点\<E\>之前新增节点\<G\>

```mermaid
graph TB;
    A-->B;
    A-->C;
    B-->D;
    B-->E;
    D-->F;
    E-->G;
```

* 举例：以遍历顺序，在节点\<A\>之后新增节点\<H\>

```mermaid
graph TB;
    A-->B;
    A-->C;
    B-->D;
    B-->E;
    C-->H;
    E-->G;    
    D-->F;
```

* 从\<X\>的子树中删除节点\<X\>的项目
  
  - 如果\<X\>是一个叶子，从父节点中拆除并返回
  
  - 否则，\<X\>有子节点
    
    - 如果\<X\>有左子树，与\<X\>的前驱节点交换项目并递归
    
    - 否则，\<X\>有右子树，与\<X\>的后继节点交换项目并递归
  
  - 运行时间为$\mathcal{O}(h)$，h是树的高度
  
  - 举例：移除\<F\>（叶子节点）

```mermaid
graph TB;
    A-->B;
    A-->C;
    B-->D;
    B-->E;
    C-->H;
    E-->G;    
```

- 举例：移除\<A\>（非叶子节点，所以首先交换到叶子）

```mermaid
graph TB;
    E-->B;
    E-->C;
    B-->D;
    B-->G;
    C-->H;
    G-->A;
```

```mermaid
graph TB;
    E-->B;
    E-->C;
    B-->D;
    B-->G;
    C-->H;
```

# 六、应用：集合

* 集合二叉树（又名二叉查找树——BST），遍历顺序按key的升序
  
  - 与BST属性等价：对每个节点，左子树的每个key$\le$节点key$\le$右子树的每个key

* 在\<X\>的子树中找到key为k的节点，花费$\mathcal{O}(h)$，就像二分查找
  
  - 如果k小于\<X\>处的key，递归左子树（或者返回None）
  
  - 如果k大于\<X\>处的key，递归右子树（或者返回None）
  
  - 否则，返回存储在\<X\>处的项目

* 其它集合操作是相似形式，看recitation  

# 七、应用：序列

* 序列二叉树：遍历顺序是序列顺序

* 我们如何以遍历顺序找到子树的$i^{th}$个节点？这个操作称为subtree_at(i)

* 迭代整个遍历顺序，但这是坏的，$\mathcal{O}(n)$

* 然而，如果我们可以耗费$\mathcal{O}(1)$计算子树的尺寸，那么可以耗费$\mathcal{O}(h)$时间解决
  
  - 检查左子树的尺寸$n_L$，并与i相比
  
  - 如果$i<n_L$，递归左子树
  
  - 如果$i>n_L$，递归右子树，$i'=i-n_L-1$
  
  - 否则，$i=n_L$，你已经达到期望的节点

* 通过增长，在节点处保存每个节点子树的尺寸  
  
  - 添加node.size成员变量到node
  
  - 当添加新叶子时，对于所有祖先a添加+1到a.size，花费$\mathcal{O}(h)$
  
  - 当删除叶子时，对于所有祖先a添加-1到a.size，花费$\mathcal{O}(h)$

* 序列操作直接从快速subtree_at(i)操作开始

* build(X)花费$\mathcal{O}(nh)$，但可以耗费$\mathcal{O}(n)$完成，看recitation

# 八、至今

<div>
<table>
    <tr>    
        <td rowspan=3>集合数据结构</td>
        <td colspan=5>操作，最坏情形O</td>    
    </tr>
    <tr>
        <td>容器（container）</td>
        <td>静态（static）</td>
        <td>动态（dynamic）</td>
        <td colspan=2>顺序（order）</td>
    </tr>
    <tr>
        <td>build(x)</td>
        <td>find(k)<br>set_at(i, x)</td>
        <td>insert(x)<br>delete(x)</td>
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
        <td>目标</td>
        <td>nlogn</td>
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
        <td rowspan=3>序列数据结构</td>
        <td colspan=5>操作，最坏情形O</td>    
    </tr>
    <tr>
        <td>容器（container）</td>
        <td>静态（static）</td>
        <td colspan=3>动态（dynamic）</td>
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
        <td>目标</td>
        <td>n</td>
        <td>logn</td>
        <td>logn</td>
        <td>logn</td>
        <td>logn</td>
    </tr>
</table>
</div>

# 八、下次

* 插入、删除后，保持二叉树平衡

* 减少$\mathcal{O}(h)$运行时间为$\mathcal{O}(logn)$，通过$h=\mathcal{O}(logn)$

# 九、Recitation

## 二叉树

二叉树是一个二节点树（连接无环图）：linked node容器，与链表节点类似，右常量个成员变量：

* 指向项目（存储在node中）的指针

* 指向父节点（可能是None）的指针

* 指向左子节点（可能是None）的指针

* 指向右子节点（可能是None）的指针

```python
class Binary_Node:
    def __init__(A, x):
        A.item = x
        A.left = None
        A.right = None
        A.parent = None
        # A.subtree_update()
```

为什么二叉节点称为二叉？实际上，二叉节点可以被连接到3个其它节点（它的父节点、左子节点、右子节点），不止2个。然而，我们将区分节点的父、子节点，因此我们称节点为二叉，基于节点拥有的子节点数量。

二叉树有一个节点，它是树的根节点：树中仅有的，无父节点的节点。树中所有其它节点，通过遍历父指针可以到达树（包含所有节点）的根部。从节点\<X\>到根节点，遍历父指针经过的这组节点，称作树中\<X\>的祖先。子树（根节点为\<R\>）中节点\<X\>的深度，为\<X\>到\<R\>的路径长度。节点\<X\>的高度，是以\<X\>为根的子树中，任意节点深度的最大值。如果节点没有子节点，它称为叶子。

为什么我们想把项目存到二叉树中？链表的麻烦在于：一些链表节点，需要从list开头，跳跃$\mathcal{O}(n)$次指针，因此抵达它花费$\mathcal{O}(n)$。相对地，正如我们早期recitation中已经看到，这是可能的：n个节点构建一个二叉树，以便于没有节点从根节点开始，跳跃花费超过$\mathcal{O}(\log n)$，比如，存在二叉树，高度为对数。二叉树结构的强大之处在于：如果我们可以保持树的高度较低，比如$\mathcal{O}(\log n)$，仅对树执行（运行时间与树的高度相近）的操作，那么这些操作耗费$\mathcal{O}(h)=\mathcal{O}(\log n)$，比$\mathcal{O}(n)$更接近$\mathcal{O}(1)$。

## 遍历顺序

二叉树中的节点，有着天然的顺序（基于客观事实），我们可以区分一个子节点是左子节点、还是右子节点。我们定义二叉树的遍历顺序基于以下潜在的特征：

* 节点\<X\>左子树中每个节点，遍历顺序中，在\<X\>之前

* 节点\<X\>右子树中每个节点，遍历顺序中，在\<X\>之后

给定一个二叉节点\<A\>，通过递归列举\<A\>左子树中节点、列举\<A\>本身、递归列举\<A\>右子树中节点，我们可以列出\<A\>子树中的节点。这个算法运行时间$\mathcal{O}(n)$，因为每个递归的节点

执行常量次工作。

```python
def subtree_iter(A):
    if A.left:    yield from A.left.subtree_iter()
    yield A
    if A.right:   yield from A.right.subtree_iter()
```

现在，存储的项目与树的遍历顺序，没有语义联系。下次，我们将为遍历顺序，提供两个不同的语义含义，其中之一将致使序列接口的有效实现，另外一个将致使集合接口的有效实现。但现在，我们只想操作树时，保留遍历顺序。

## 树导航

给定一个二叉树，有效地按遍历顺序导航节点是有用的。可能是最直接的操作：找出给定节点子树中，按遍历顺序首先/最后出现的节点。为了找到首个节点，简单地向左遍历（如果左子树存在）。这个操作花费$\mathcal{O}(h)$，因为递归的每一步向树的下方移动。找出子树的最后一个节点是对称的。

```python
def subtree_first(A):
    if A.left:     return A.left.subtree_first()
    else:          return A

def subtree_last(A):
    if A.right:    return A.right.subtree_last()
    else:          return A
```

给定一个二叉树中的节点，它也是有用的：按遍历顺序找出下个节点，比如节点的后继节点，或者遍历顺序的前一个节点：前驱节点。为了找到节点\<A\>的后继节点，如果\<A\>有右子树，那么那么\<A\>的后继节点是，右子树的首个节点。否则，\<A\>的后继节点不存在\<A\>的子树中，因此我们遍历树，找到\<A\>的最低祖先（\<A\>在祖先的左子树中）。

第一种情形，算法仅沿着树向下找后继节点，因此它运行耗时$\mathcal{O}(h)$。第二种情形，算法只会沿着树向上去找后继节点，因此它运行耗时也是$\mathcal{O}(h)$。前驱算法是对称的。

```python
def successor(A):
    if A.right:    return A.right.subtree_first()
    while A.parent and (A is A.parent.right):
        A = A.parent
    return A.parent

def predecessor(A):
    if A.left:    return A.right.subtree_last()
    while A.parent and (A is A.parent.left):
        A = A.parent
    return A.parent
```

## 动态操作

如果我们想添加或删除二叉树中的项目，我们必须注意保持树中其它项目的遍历顺序。为了以遍历顺序，在给定节点\<A\>之前插入一个节点\<B\>，\<A\>要么有左子树、要么没有。如果\<A\>没有左子树，我们可以简单地把\<B\>当作\<A\>的左子节点添加上。否则，如果\<A\>有左子节点，我们可以把\<B\>当作\<A\>左子树最后一个节点的右子节点添加上。任意一种情形，算法每步沿着树向下，因此算法运行耗时$\mathcal{O}(h)$。在节点之后插入，是对称的。

```python
def subtree_insert_before(A, B):
    if A.left:
        A = A.left.subtree_last()
        A.right, B.parent = B, A
    else:
        A.left, B.parent = B, A
    # A.maintain()

def subtree_insert_after(A, B):
    if A.right:
        A = A.right.subtree_first()
        A.left, B.parent = B, A
    else:
        A.right, B.parent = B, A
    # A.maintain()
```

为了从二叉树中删除包含在给定节点中项目，基于存储项目的节点是否为叶子，存在两种情形。如果节点为叶子，我们可以简单地从节点的父节点上清除子节点指针，并返回该节点。可选择地，如果节点并非叶子，我们可以拿节点的项目，与节点的后继、前驱节点的项目交换，沿着树向下，直到叶子中的项目可以被移除。因为交换仅发生在沿着树向下时，这个操作耗时也是$\mathcal{O}(h)$。

```python
def subtree_delete(A):
    if A.left or A.right:
        if A.left:   B = A.predecessor()
        else:        B = A.successor()
        A.item, B.item = B.item, A.item
        return B.subtree_delete()
    if A.parent:
        if A.parent.left is A:   A.parent.left = None
        else:                    A.parent.right = None
        # A.parent.maintain()
    return A
```

## 二叉树完整实现

```python
class Binary_Node:
    def __init__(A, x):
        A.item = x
        A.left = None
        A.right = None
        A.parent = None
        # A.subtree_update()

    def subtree_iter(A):
        if A.left:    yield from A.left.subtree_iter()
        yield A
        if A.right:   yield from A.right.subtree_iter()

    def subtree_first(A):
        if A.left:    return A.left.subtree_first()
        else:         return A

    def subtree_last(A):
        if A.right:   return A.right.subtree_last()
        else:         return A

    def successor(A):
        if A.right:   return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent

    def predecessor(A):
        if A.left:   return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent

    def subtree_insert_before(A, B):
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B, A
        else:
            A.left, B.parent  = B, A
        # A.maintain()

    def subtree_insert_after(A, B):
        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent  = B, A
        else:
            A.right, B.parent = B, A

    def subtree_delete(A):
        if A.left or A.right:
            if A.left: B = A.predecessor()
            else:      B = A.successor()
            A.item, B.item = B.item, A.item
            return B.subtree_delete()
        if A.parent:
            if A.parent.left is A: A.parent.left = None
            else:                  A.parent.right = None
        return A
```

## 顶级数据结构

迄今为止，我们已经定义的所有操作都包含在Binary_Tree类中，因此它们可以应用到任意子树。现在我们可以定义一个通用二叉树数据结构，它存储一个指向根的指针，以及它存储项目的数量。我们可以用少量额外操作实现相同操作，来让根和尺寸跟着变化。

```python
class Binary_Tree:
    def __init__(T, Node_Type = Binary_Node):
        T.root = None
        T.size = 0
        T.Node_Type = Node_Type

    def __len__(T):    return T.size
    def __iter__(T):
        if T.root:
            for A in T.root.subtree_iter():
                yield A.item
```

## 练习

给定一个项目数组$A=(a_0,...,a_{n-1})$，描述一个$\mathcal{O}(n)$时间算法来构建一个二叉树T，包含在A中的项目，\(1\)存储在$i^{th}$（按T的遍历顺序）节点中的项目是$a_i$，(2)T的高度是$\mathcal{O}(\log n)$。

解：通过存储中间项目到根节点来构建T，然后递归构建剩余的左、右两半部分到左右子树。由遍历顺序的定义可知，这个算法满足属性(1)，属性(2)：因为高度大致为$H(n)=1+H(n/2)$。这个算法执行时间$\mathcal{O}(n)$，因为每个节点每次递归执行常量工作。

```python
def build(X):
    A = [x for x in X]
    def build_subtree(A, i, j):
        c = (i + j) // 2
        root = self.Node_Type(A[c])
        if i < c:
            root.left = build_subtree(A, i, c - 1)
            root.left.parent = root
        if c < j:
            root.right = build_subtree(A, c + 1, j)
            root.right.parent = root
        return root
    self.root = build_subtree(A, 0, len(A)-1)
```

---

证明以下迭代过程以遍历顺序返回树的节点，耗时$\mathcal{O}(n)$

```python
def tree_iter(T):
    node = T.subtree_first()
    while node:
        yield node
        node = node.successor()
```

解：这个过程遍历树的每个边两次，一次沿树向下，一次向上。因为树中边的数量比点的数量少1，遍历耗时$\mathcal{O}(n)$。

## 应用：集合

为了使用二叉树实现集合接口，我们使用树的遍历顺序来存储项目（按key升序排列）。这个属性通常被称作：二叉查找树属性，节点左子树中的key小于节点中的key，节点右子树中的key大于节点中的key。查找包含查询key的节点（或没有节点包含该key），可以通过沿着树向下完成，递归到恰当的边。

解：通过一个个插入选中的学生项目，生成一个集合二叉树（二叉查找树），然后一个个查找、删除选中学生的key。

```python
class BST_Node(Binary_Node):
    def subtree_find(A, k):
        if k < A.item.key
            if A.left:     return A.left.subtree_find(k)
        elif k > A.item.key:
            if A.right:    return A.right.subtree_find(k)
        return None

    def subtree_find_next(A, k):
        if A.item.key <= k:
            if A.right:    return A.right.subtree_find_next(k)
            else:          return None
        elif A.left:
            B = A.left.subtree_find_next(k)
            if B:          return B
        return A

    def subtree_find_prev(A, k):
        if A.item.key >= k:
            if A.left:    return A.left.subtree_find_prev(k)
            else:         return None
        elif A.right:
            B = A.right.subtree_find_prev(k)
            if B:         return B
        return A

    def subtree_insert(A, B):
        if B.item.key < A.item.key:
            if A.left:    A.left.subtree_insert(B)
            else:         A.subtree_insert_before(B)
        elif B.item.key > A.item.key:
            if A.right:   A.right.subtree_insert(B)
            else:         A.subtree_insert_after(B)
        else:    A.item = B.item
```

```python
class Set_Binary_Tree(Binary_Tree):
    def __init__(self): super().__init__(BST_Node)

    def iter_order(self): yield from self

    def build(self, X):
        for x in X: self.insert(x)

    def find_min(self):
        if self.root:    return self.root.subtree_first().item

    def find_max(self):
        if self.root:    return self.root.subtree_last().item

    def find(self, k):
        if self.root:
            node = self.root.subtree_find(k)
            if node:    return node.item

    def find_next(self, k):
        if self.root:
            node = self.root.subtree_find_next(k)
            if node:    return node.item

    def find_prev(self, x):
        if self.root:
            node = self.root.subtree_find_prev(k)
            if node:    return node.item

    def insert(self, x):
        new_node = self.Node_Type(x)
        if self.root:
            self.root.subtree_insert(new_node)
            if new_node.parent is None: return False
        else:
            self.root = new_node
        self.size += 1
        return True

    def delete(self, k):
        assert self.root
        node = self.root.subtree_find(k)
        assert node
        ext = node.subtree_delete()
        if ext.parent is None: self.root = None
        self.size -= 1
        return ext.item
```