# 2-1解决递归

以两种方式推断下列递归的答案：通过递归树、主定理。答案应该包含最贴切的上下边界（递归允许）。假设$T(1)\in\theta(1)$

（a）$T(n)=2T(\frac{n}{2})+\mathcal{O}(\sqrt{n})$

根据主定理：$T(n)=\Theta(n)$

（b）$T(n)=8T(\frac{n}{4})+\mathcal{O}(n\sqrt{n})$

根据主定理：$T(n)=\Theta(n^\frac{3}{2}\log n)$

（c）$T(n)=T(\frac{n}{3})+T(\frac{n}{4})+\Theta(n)，假设对于所有a<b，T(a)<T(b)$

根据主定理：$T(n)=\Theta(n)$

# 2-2查找石头

萨诺斯是一个超级恶棍，在银河系间寻找一个古老而强大的神器，名为：通灵石。不幸地是，她不知道石头在哪个行星上。宇宙由无数颗行星组成，每个由一个唯一的正数标识。在每个行星上都有一个神谕，经过一番劝说，神谕会告诉萨诺斯，通灵石是否在行星上，它的行星标识严格高于他们自己的行星标识。面见宇宙中的每个神谕将花费永久，因此萨诺斯想快速地找到通灵石。假设通灵石在行星k上，描述一个算法（通过面试至多$\mathcal{O}(\log k)$个神谕），来帮助萨诺斯找到通灵石。

首先来看：如果我们可以找到一个x行星，x>k（x并不远大于k，$x=\Theta(k)$），那么就可行了，随着从1到x-1二分查找行星，将通过遍历至多$\mathcal{O}(\log x)=\mathcal{O}(\log k)$个神谕找到k的值。那么剩下的是找到这个行星x。

为了找到x，指引萨诺斯遍历行星$2^i$，始于$i=0$，直到$x=2^i$上的神谕告知萨诺斯：x>k。因为x是首个$2^i>k$的行星，那么x/2<k，x<2k=$\Theta(k)$，符合预期。为了到达行星$x=2^i$，萨诺斯面见$i=\lceil \log_2k \rceil=\Theta(\log k)$个神谕，因此为了找到k，这个算法正如期望的那样，至多面见$\mathcal{O}(\log k)$个神谕。

# 2-3Collage Collating

Fodoby是一家为创意人士订制软件工具的公司。他们的最新软件，Ottoshop，通过允许他们在单个文档中叠加图片，来帮助用户制作拼贴。描述一个数据库来追踪给定文档中的图片，它支持以下操作：

（1）make_document()：构建一个不包含图片的空文档

（2）import_image(x)：将带有唯一整数ID x的图片加到文档顶部

（3）display()：以从底到顶的顺序，返回文档图片id的数组

（4）move_below(x, y)：把ID为x的图片移动到ID为y的图片下面

操作（1）应该以最坏情形$\mathcal{O}(1)$时间执行，操作（2）和（3）应该每个以最坏情形$\mathcal{O}(n)$时间执行，操作（4）应该以最坏情形$\mathcal{O}(\log n)$时间执行，n是操作时文档中包含图片的数量。

这个数据库需要我们保存一个外部有序的图片序列，但也支持基于它们ID的内部查找。因此我们将实现一个数据库，结合了序列结构（一个存储图片ID的双向链表）和集合结构（存储键值对$(x,v_x)$以x的值排序的数组，x是图片的ID，$v_x$是一个指向包含x的链表节点的指针）。为了实现make_document，简单地初始化一个空链表L和一个空有序数组S，每个以$\mathcal{O}(1)$时间。这个操作没有输出，它是正确的。

为了实现import_image(x)，以节点$v_x$添加x到L的头部，用时$\mathcal{O}(1)$时间，并添加$(x,v_x)$到S，用时$\mathcal{O}(n)$。代理这些数据结构，确保x被添加到序列L头部，S现在包含$(x,v_x)$，并在插入后保持有序。

为了实现display()，通过遍历L中的项目，构建并返回一个数组，可以用$\mathcal{O}(n)$时间完成。

为了实现move_below(x, y)，使用二分查找，找到S中的键值对$(x,v_x)$和$(y,v_y)$，每个用时$\mathcal{O}(\log n)$。通过重链（relink）指针，然后我们可以从L中以$\mathcal{O}(1)$时间移除节点$v_x$，并在节点$v_y$后插入，也用时$\mathcal{O}(1)$。这是一个在双向链表中重链指针的方法：

```python
def relink(S, vx, vy):
    if vx.prev: vx.prev.next = vx.next
    else:    S.head = vx.next
    if vx.next: vx.next.prev = vx.prev
    else:    S.tail = vx.prev
    vx.prev = vy
    vx.next = vy.next
    if vy.next: vy.next.prev = vx
    else:    S.tail = vx
    vy.next = vx
```

# 2-4Brick Blowing

Porkland是一个由猪组成的社区，它们居住在从东向西延申的街道一边，排成一排的n个房子里。对猪来说是不幸的，这个狼非常擅长吹倒猪舍，这得益于从西向东的大风。如果狼向东吹向包含b块砖的房子，房子将会倒塌，它东边低于b块砖的房子都会倒塌。对于Porkland中的每个房子，狼想知道它的破坏情况，例如：从西向东吹向它后，倒塌房子的数量。

（a）假设n=10，从西向东Porkland中每个房子的砖数是：[34,57,70,19,48,2,94,7,63,75]。计算这个实例中：Porkland每个房子的损坏。

[4, 5, 6, 3, 3, 1, 4, 1, 1, 1]

（b）Porkland房子是特殊的，要么1）东边没有邻居，要么2）它东边的邻居至少有和它一样的砖。给定一个数组，包含Porkland中每个房子的砖数，描述一个$\mathcal{O}(n)$时间复杂度算法，来返回Porkland中每个房子的破坏，Porkland只有一个房子是非特殊的。

保存一个数组D，拥有于输入数组H相同的尺寸，用来存储破坏数，D的$i^{th}$个项目是一个代表破坏数的整数。在$i^{th}$房子添加破坏数，以$\mathcal{O}(1)$时间在D[i]处加数。当风吹到时，因为每个房子本身会毁坏，以$\mathcal{O}(n)$时间初始化D中每个元素为1，使用下面算法计算其他破坏数。

如果Porkland仅一个房子是非特殊的，意味着子数组A（从最西边的房子到h，单调递增），从$(h+1)^{th}$到最东边的房子也是如此。我们可以通过线性扫描用$\mathcal{O}(n)$时间找到h。子数组B中任意房子的破坏数为1，因为到东边的房子，没有更少的砖，因此它们的值被正确地初始化了。

那么剩下的是：计算A中房子的破坏数。使用双指算法，一个索引 i 始于A的起始处，另一个索引 j 位于B的起始处。重复下面的过程，直到$i=|A|$：如果$j<|B|$且房子A[i]比B[j]有更多的砖，那么j++；否则把 j 加到D[i]处的破坏数上，并且i++。当$i+j=|A|+|B|=n$时，循环终止，每次迭代 i+j 增1。因为每次迭代的工作是$\mathcal{O}(1)$，所以这个算法以$\mathcal{O}(n)$时间执行。

为了证明：这个算法正确地计算了A中每个房子的破坏数，我们首先证明：上面的循环在每次迭代开始时，保证：$A[i]>B[k]，k\in\{0,...,j-1\}$。这个属性表明：算法为A中每个房子，正确地计算破坏数：当$A[i]\le B[j]$时，算法更新A[i]的破坏数，因此该声明表明：A[i]以东，比其有更少砖的房子是：$H=\{B[k]|k\in\{0,...,j-1\}\}，|H|=j$。因此房子A[i]处的破坏数是$D[i]=j+1$。

为了证明这个声明，我们推断当$i+j=0$时，这个声明时true，因为k的可能值集合为空。现在为推断做出假设：声明在 i+j 时成立。

如果$A[i]>B[j]$，那么j++保证成立。因为$A[i]>B[k]，k\in\{0,...,j-1\}$。

可选择地，如果$A[i]\le B[j]$，那么i++，也保证了推断假设，因为$A[i+1]>A[i]$，证明声明。

（c）给定一个数组，包含porkland中每个房子中砖的数量，描述一个$\mathcal{O}(n\log n)$时间算法来返回porkland每个房子的破坏数。

我们更改归并排序来记录破坏数（每次merge前，发生在每个子数组中房子之间）。因为我们将从原始位置，移动H中砖的数量，我们将用元组$H[i]=(b_i,i)$取代每个砖数量，用来记录哪个房子与$b_i$相关。

像（b）那样，初始化一个 破坏数 数组D为1。递归排序、记录破坏数（发生在H前半部分房子之间），对H后半部分同样这么做。接下来使用（b）中的$\mathcal{O}(n)$时间算法来计算破坏数（前半部分房子和后半部分房子之间），然后使用归并排序的归并步骤，以$\mathcal{O}(n)$时间将两个有序“半边”结合成一个有序数组。因为（b）和归并都花费$\mathcal{O}(n)$时间，所以这个算法的递归和归并排序一样，都花费$\mathcal{O}(n\log n)$执行时间。

现在，通过推断子数组的尺寸，我们证明这个算法：正确地记录了给定子数组中，每个房子与子数组中其他房子的破坏数。当子数组尺寸为1，该子数组中，房子间的破坏数确定为1，且初始化步骤记录了它。可选择地，假设对于所有$k<n$声明都是true。通过推断，算法正确地记录了子数组前半部分房子间的所有破坏数，以及后半部分房子间所有破坏数。剩下的就是：记录左半部分与右半部分房子之间的破坏数。

幸运地，因为前后两部分子数组是有序的，（b）中的算法准确地记录了那些破坏数。使用归并排序中的归并步骤的排序保证了这点。

归并步骤和（b）部分的算法都是双指算法，从两个子数组起始处遍历。我们在（d）中的实现利用了这点，记录归并排序中归并步骤的破坏数，而不是单独地。

（d）写一个python函数get_damages来实现你的算法。

```python
def get_damages(H):
    D = [1 for _ in H]
    H2 = [(H[i], i) for i in range(len(H))]
    def merge_sort(A, a = 0, b = None):
        if b is None:    b = len(A)
        if 1 < b - a:
            c = (a + b + 1) // 2
            merge_sort(A, a, c)
            merge_sort(A, c, b)
            i, j, L, R = 0, 0, A[a:c], A[c:b]
            while a < b
                if (j >= len(R)) or (i < len(L) and L[i][0] <= R[j][0])
                    D[L[i][1]] += j
                    A[a] = L[i]
                    i += 1
                else:
                    A[a] = R[j]
                    j += 1
                a += 1
    merge_sort(H2)
    return D
```