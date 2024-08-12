# 4-1 序列旋转

下面是一个序列AVL树T。执行操作T.delete_at(8)，该操作期间，每次旋转操作执行完后，画出该树。

![](https://raw.githubusercontent.com/lialong/algorithms-6006/main/problemSession/04/1.png)

# 4-2 Fick Nury

Fick Nury领导n名超级英雄组成了精英团队——复仇者联盟。他听说：超人Sanos正在一个遥远星球上制造麻烦，需要他决定是否与她对抗。Fick对复仇者们进行调研，并编写了一个调查结果表，每个调查结果是一个元组，对应复仇者的名字以及对于该话题的观点。观点+s意味着他们对于对抗Sanos的力度为s，然而观点-s意味着他们反对对抗Sanos的力度为s。Fick想生成一个列表，包含log个复仇者的名字（他们有着最有力的观点），因此他可以和他们见面讨论。假设这些包含调查的记录是只读访问控制的，因此任何计算必须写到另外的内存。

 (a) 描述一个$\mathcal{O}(n)$时间的算法来生成Fick的列表

解：构建一个最大优先队列，包含所有的复仇者（带着他们的名字）。优先队列至多存储n个复仇者，因此应该花费不大于$\mathcal{O}(n)$的空间。每个复仇者$r_i$带着观点$s_i$，形成$(|S_i|,i)$，保证key唯一性。然后删除意愿最强烈的复仇者$\log n$次，并返回结果，这个算法的运行时间是$B(n)+(\log n)*D$，$B(n)$是构建尺寸为n的优先队列花费的时间，D是删除最大值的时间。我们可以通过使用二叉最大堆作为我们的优先队列，来实现期望的运行时间，因为构建花费$\mathcal{O}(n)$，删除花费摊还$\mathcal{O}(\log n)$。

(b) 现在假设Fick的电脑仅允许写最多$\mathcal{O}(\log n)$空间，描述一个$\mathcal{O}(n\log \log n)$时间算法来生成Fick的列表。

解：构建一个最小优先队列，包含列表中前$\log n$复仇者的观点（包含他们的名字）。每个复仇者$r_i$，带着观点$s_i$，形成$(|s_i|,i)$让key唯一。然后对剩下的复仇者，重复下面过程，维持不变性：处理完复仇者i之后，前i个中$\log n$个有最强烈观点的复仇者包含在优先队列，当i=n时问题解决。（1）从优先队列中删除最小的复仇者r*（2）比较r*的key和$i^{th}$复仇者$r_i$的key（3）将较大的插入到优先队列。如果$r_i<r^*$，那么$r_i$小于优先队列中的每个复仇者，因此不在前$\log n$。可选择地，如果$r^*<r_i$，那么$r_i$大于迄今为止找到的$k^{th}$大的点。在任意情形，添加较大的到优先队列，维持不变性。在所有情形中，优先队列最多存储最大的$\log n$个复仇者，因此占用不大于$\mathcal{O}(\log n)$的空间。这个算法的运行时间是$B(\log n)+(n-\log n)*(I+D)$,$B(\log n)$是构建尺寸$\log n$优先队列的时间，I和D是插入和删除的时间。因此我们可以使用集合AVL树或最小堆作为我们的优先队列，实现$\mathcal{O}(n\log\log n)$运行时间，至多使用$\mathcal{O}(\log n)$空间。

# 4-3 SCLR

Stormen, Ceiserson, Livest, and Rein四个学者，写了一本有关计算机科学书方面非常受欢迎的书，众所周知：SCLR。他们在办公室中找到了前k版本，想把他们线下拍卖用于慈善。拍卖会中的每个投标都有一个唯一整数：投标id，可以对单个复制品竞标某个正整数金额（在整个拍卖会期间，可能增加或减少）。描述一个数据库，支持下面操作，假设n是执行该操作时，数据库中竞标者的数量。对于每个操作，标注你的运行时间是：最坏/期望/摊还。

new_bid(d, b)，对竞标b记录一个新的竞标者ID d，$\mathcal{O}(\log n)$

update_bid(d, b)，更新b的已存在的竞标者ID d的竞标，$\mathcal{O}(\log n)$

get_revenue()，返回从开卖至今，来自k个最高竞拍者的收入，$\mathcal{O}(1)$

解：首先看操作update_bid，需要找到、更改竞标者（给定ID）的竞标，因此维护一个字典，包含竞标者（key为竞标者ID，称作竞标者字典）。哈希表或集合AVL树可以实现这个目的，使用哈希表，对前两个操作来说，将产生摊还期望运行时间。

我们也将需要记录已存在竞标的顺序：在任意给定时间，特别是k个最高的和。为了实现它，维护两个优先队列：一个最小优先队列，包含k个最大的竞标，一个最大优先队列，包含剩下的n-k个竞标。因为我们需要$\mathcal{O}(\log n)$性能在优先队列的插和删上，所以我们可以使用集合AVL树或二叉堆来实现优先队列，前两个操作使用二叉堆将产生摊还运行时间。

为了找到每个在优先队列中的竞标者，我们在竞标字典（指针指向优先队列中的竞标，比如AVL节点或二叉堆的索引）中存储每个竞标者。我们将假定集合AVL树用于实现竞标者字典和优先队列。另外，维护最小优先队列的竞标之和B，以至于我们可以在常量时间内返回。

为了实现new_bid(d,b)，从最小优先队列中移除最小的投标$b'$，对应竞标者ID为$d'$，花费$\mathcal{O}(\log n)$，根据它的竞标金额$b'$降低B。然后比较$b$和$b'$。在迄今为止看到的k个最高竞标中哪个是更高的，哪个不是，插入更高的到最小优先队列，花费$\mathcal{O}(\log n)$，根据竞标增加B。将较小的写入到最大优先队列，也花费$\mathcal{O}(\log n)$。另外，添加d到竞标字典，指向它优先队列中的竞标位置，更新与竞标者$d'$相关的指针，每个花费$\mathcal{O}(\log n)$。这个方法维持目前数据结构的不变性，最坏情形耗费$\mathcal{O}(\log n)$。

为了实现update_bid(d, b)，找到已存在的竞标者d的竞标，在优先队列（使用竞标者字典）中的位置，花费$\mathcal{O}(\log n)$，然后把它从优先队列中移除，也耗费$\mathcal{O}(\log n)$。如果最小优先队列仅有k-1个竞标，从最大优先队列中移除最大的，并把它插入到最小优先队列，花费$\mathcal{O}(\log n)$。当这么做时，重新计算B（花费$\mathcal{O}(1)$），更新指针花费$\mathcal{O}(\log n)$。现在有ID d的竞标者已经移除，我们可以把它当作一个新竞标者（拥有更新后的竞标）重新插入它，使用上面的new_bid插入。这个操作执行常量次$\mathcal{O}(\log n)$时间复杂度的调用，因此这个操作最坏情形运行时间$\mathcal{O}(\log n)$。

为了实现get_revenue()，简单地返回B中存储的值，花费最坏情形$\mathcal{O}(1)$。

# 4-4 Receiver Roster

教练Bell E. Check正在尝试找出哪个足球接球手放到她的首发阵容。每次比赛，Coach Bell想从能力（过往比赛平均分）最高的接球手开始，但遇到了麻烦，因为她的数据是不完整的，尽管实习生经常从新老比赛中添加或纠正数据。每个接球手有一个唯一的正整数标识，每场比赛由一个唯一的整数时间。描述一个数据库，支持以下操作，每个以最坏情形$\mathcal{O}(\log n)$时间，n是执行该操作时数据库中的比赛场数。假设n总是大于球队中的接球手数量。

record(g,r,p)，为游戏g，球员r，记分p

clear(g,r)，移除球员r，在游戏g中的任何记录

ranked_receiver(k)，返回能力第k高的球员

解：首先，观察到：操作需要为接球手（给定球员号）找、改记录，花费$\mathcal{O}(\log n)$，因此维护一个字典（包含由球员号确定唯一性的接球手，称之为球员字典）。因为我们需要实现最坏情形$\mathcal{O}(\log n)$的执行时间，我们不能负担起哈希表期望的能力，因此我们用集合AVL树实现字典。

对每个接球手，我们将需要通过比赛ID找到并更新他们的比赛，因此对球员字典中每个接球手，我们将维护一个指向他们自身集合AVL树的指针，接球手比赛以比赛ID为键（称之为接球手的比赛字典）。用每个接球手的比赛字典，我们将维护进行过的比赛数量，迄今为止，已经获得的总分。我们可以从他们的比赛数和得分，比较两个球员之间的能力。

最终，为了找到第k高能力的接球手，我们维护一个单独的基于接球手的集合AVL树（以能力为键），为每个点增加它的子树尺寸（称之为能力树）。我们在lecture中展示了如何维护子树尺寸，花费$\mathcal{O}(1)$，因此我们可以维护这个新增变量。球员字典中的每个点，将保存一个指向能力树中节点（对应该球员）的指针。因为我们所有数据结构用集合AVL树，集合操作执行时间为最坏情形$\mathcal{O}(\log n)$。

为了实现record(g, r, p)，在球员字典中，找到球员r的比赛字典D，花费$\mathcal{O}(\log n)$。如果比赛g在D中，更新它的分数为p，花费$\mathcal{O}(\log n)$，更新存在r的比赛字典中的总分，花费$\mathcal{O}(1)$。否则，插入游戏g的记录到D中，花费$\mathcal{O}(\log n)$，更新比赛数量以及总分，花费$\mathcal{O}(1)$。r的能力会发生改变，因此在能力树中找到与r对应的节点，从树中移除接球手的能力，更新它的能力，然后重新插入到树中，共计$\mathcal{O}(\log n)$。这个操作保持了我们数据结构最坏情形$\mathcal{O}(\log n)$。

为了实现clear(g, r)，像之前那样，在球员字典中，找到球员r的比赛字典D，并移除g（假设它存在）。与上面相同，维持比赛数量和总分，更新能力树，总共最坏情形$\mathcal{O}(\log n)$。

为了实现ranked_receiver(k)，在能力树中，通过使用子树尺寸变量，找到第k高能力：如果点的右子树是k或者更大，那么递归地在右子树查找；如果点的右子树尺寸为k-1，那么返回当前节点；否则，点的右子树尺寸是$k'<k-1$，递归节点左子树，找到子树第k高能力的球员。这个递归算法仅会沿着树向下，因此它执行时间为最坏情形$\mathcal{O}(\log n)$。

# 4-5 Warming Weather

Gal Ore是研究气候的科学家。作为她研究的一部分，她经常需要查询，历史特定时期地球观测到的最高温度，基于一个增长的测量集合（她经常收集、添加）。假设温度和日期是整数（表示一个一致分辨率的值）。实现一个数据库支持下面操作，帮助Gal有效地评估这段时间 的查询。

record_temp(t, d)，在日期d记录温度t

max_in_range(d1, d2)，返回日期d1和d2之间，观测到的最大温度

为了解决这个问题，我们将存储温度到一个AVL树（二叉搜索树，以date作为key），每个节点A存储了A.item，有日期属性A.item.key和温度属性A.item.temp

(a) 为了帮助评估期望范围内的查询，我们将对每个节点新增变量：A.max_temp，存在A子树中的最大温度；A.min_date和A.max_date，A子树中存储的最小、最大日期。描述一个$\mathcal{O}(1)$时间算法来计算这些节点A上的新增变量，假设A子树上的所有其他节点都已经正确地增加。

解：这些新增变量可以通过下面算法以$\mathcal{O}(1)$时间计算。

A.max_temp可以通过采取A.item.temp、A.left.max_temp、A.right.max_temp中的最大值。

A.min_date：如果A有左子节点，去A.left.min_date，否则取A.item.key

A.max_date：如果A有右子节点，去A.right.max_date，否则取A.item.key

(b) 如果子树至少包含1个测量值位于日期范围内，1个测量值位于范围外，那么子树与日期范围部分重叠。给定一个日期范围，证明：对于任意二叉搜索树（包含测量值，以日期为key），树中至多一个点，其左右子树都与日期范围部分重叠。

解：如果一个节点，它的左右子树都与日期范围部分重叠，我们说这个节点在范围上分叉。这个问题要求我们证明：二叉搜索树中至多一个节点在给定范围上分叉。首先，观察到：任何分叉的节点，都在范围内；否则范围不是连续的。假设两个不同的点p和q在范围$(d_1,d_2)$上分叉。让x是p和q的最低公共祖先。因为p和q都在范围内，那么x也在，因为按遍历顺序，x在p和q之间。p和q中，至少有一个不是x，因此不失一般性，假设p不是x，p在x的左子树中。p和x都在范围内，但p的右子树按遍历顺序在p和x之间，却包含不在范围内的key，这是矛盾的。

\(c\) 让subtree_max_in_range(A, d1, d2)是日期d1到d2（包含d1、d2）之间，存储在节点A的子树中的最大温度，如果范围内不存在测量值，返回None。假设树已经像part(a)中那样新增了变量，描述一个递归算法来计算subtree_max_in_range(A, d1, d2)。如果h是A的子树的高度，当A部分重叠该范围时，你的算法应该以$\mathcal{O}(h)$时间运行；否则耗时$\mathcal{O}(1)$。

解：给定节点A和范围$[d1,d2]$，A子树中存储的最大温度测量值，要么是节点本身的温度，要么在A的左右子树。因为我们已经新增了变量最大、最小日期（每个节点的子树中），我们可以评估A中日期。

1，与范围不相交，((A.max_date < d1) 或 (d2 < A.min_date))

2，包含在范围内，d1 <= A.min_date 且 A.max_date <= d2

3，否则与范围部分重叠

通过常数次比较，花费$\mathcal{O}(1)$。在case(1)中，子树中没有测量值处于该范围，因此我们可以返回None，耗时$\mathcal{O}(1)$。在case(2)中，子树中所有测量值处于该范围内，因此我们可以返回A.max_temp，通过新增变量，耗时$\mathcal{O}(1)$。最终，在case(3)中，为A子树中每个点，递归计算范围内的最大温度，并返回它们和A中温度的最大值（因为A上的温度一定在范围内）。

这个算法花费至多$\mathcal{O}(h)$。观察到：part(b)中的声明，确保除了一个case(3)的点，子树中的递归调用，将花费$\mathcal{O}(1)$。因此递归调用的图形，将会是至多两个路径（从根到树中另外点）的联合，沿着路径，至多触碰$\mathcal{O}(h)$个点，每个点至多做$\mathcal{O}(1)$工作。

(d) 描述一个数据库，实现操作record_temp(t, d)、max_in_range(d1, d2)，每个花费最坏情形$\mathcal{O}(\log n)$，n是执行该操作时，数据库中日期的数量。

解：存储测量值到集合AVL树（键为日期）。像part(a)中那样，在树中新增变量，基于子节点的新增变量，每个点处可以花费$\mathcal{O}(1)$维持，不会影响其他AVL树操作的运行时间。为了实现record_temp(t, d)，检查看日期d是否已经在树中了。如果已经在了，从树中删除该测量值，并保持两个测量值中较大的温度。在任意情形，插入新的测量到树中，花费最坏情形$\mathcal{O}(\log n)$。这个过程维持不变性：存储在日期d处的温度，是该天最高的温度记录。

为了实现max_in_range(d1, d2)，我们通过简单地返回subtree_max_in_range(T.root, d1, d2)降级为part\(c\)，T.root是树的根节点。由(c)可知这个算法是正确的，并且最坏情形耗时$\mathcal{O}(\log n)$，因为集合AVL树的高度为$\mathcal{O}(\log n)$。

(e) 在python类Temperature_DB（继承提供的Set_AVL_Tree）中实现你的数据库；你将只需实现上面的part(a)和part\(c\)。

```python
from Set_AVL_Tree import BST_Node, Set_AVL_Tree

class Measurement:
	def __init__(self, temp, date):
		self.key = date
		self.temp = temp

	def __str__(self): return "%s,%s" % (self.key, self.temp)

class Temperature_DB_Node(BST_Node):
	def subtree_update(A):
		super().subtree_update()
		A.max_temp = A.item.temp
		A.min_date = A.max_date = A.item.key
		if A.left:
			A.min_date = A.left.min_date
			A.max_temp = max(A.max_temp, A.left.max_temp)
		if A.right:
			A.max_date = A.right.max_date
			A.max_temp = max(A.max_temp, A.right.max_temp)

    def subtree_max_in_range(A, d1, d2):
        if (A.max_date < d1 or d2 < A.min_date): return None
        if (d1 <= A.min_date) && (A.max_date <= d2): return A.max_temp
        t = None
        if d1 <= A.item.key <= d2:
            t = A.item.temp
        if A.left:
            t_left = A.left.subtree_max_in_range(d1, d2)
            if t_left:
                if t: t=max(t, t_left)
                else: t=t_left
        if A.right:
            t_right = A.right.subtree_max_in_range(d1, d2)
            if t_right:
                if t: t=max(t, t_right)
                else: t=t_right
        return t

class Temperature_DB(Set_AVL_Tree):
    def __init__(self):
        super().__init__(Temperature_DB_Node)

    def record_temp(self, t, d):
        try:
            m = self.delete(d)
            t = max(t, m.temp)
        except: pass
        self.insert(Measurement(t, d))

    def max_in_range(self, d1, d2):
        return self.root.subtree_max_in_range(d1, d2)
```
