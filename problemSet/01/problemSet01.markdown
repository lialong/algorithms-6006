# 1-1 函数的渐近性（asymptotic behavior）

每个包含5个函数的集合，对它们进行排序，若序列中$f_a$出现在$f_b$之前，那么$f_a=\mathcal{O}(f_b)$。如果$f_a=\mathcal{O}(f_b)$，且$f_b=\mathcal{O}(f_a)$，意味着：$f_a和f_b$可以出现在任意顺序，表明可以用花括号将$f_a和f_b$围到一个集合中。举例，如果函数是：$f_1=n，f_2=\sqrt{n}，f_3=n+\sqrt{n}$，正确的答案是：$(f_2,\{f_1,f_3\})或(f_2,\{f_3,f_1\})$。

注意：$a^{b^c}代表a^{(b^c)}，并非(a^b)^c$。$\log代表\log_2$，除非一个不同的底被明确地说明。Stirling近似估算可以帮助比较阶乘。

 a)

$f_1=\log(n^n),f_2=(\log n)^n,f_3=\log(n^{6006}),f_4=(\log n)^{6006},f_5=\log(\log(6006n))$

$f_5,f_3,f_4,f_1,f_2$

 b)

$f_1=2^n,f_2=6006^n,f_3=2^{6006^n},f_4=6006^{2^n},f_5=6006^{n^2}$

$f_1,f_2,f_5,f_4,f_3$

c)

$f_1=n^n,f_2=\binom{n}{n-6},f_3=(6n)!,f_4=\binom{n}{n/6},f_5=n^6$

Sterling’s近似法：

$n!=\sqrt{2\pi n}(\dfrac{n}{e})^n(1+\Theta(\dfrac{1}{n}))$

$\{f_2,f_5\},f_4,f_1,f_3$

 d)

$f_1=n^{n+4}+n!,f_2=n^{7\sqrt n},f_3=4^{3n\log n},f_4=7^{n^2},f_5=n^{12+1/n}$

$f_5,f_2,f_1,f_3,f_4$

# 1-2 给定一个支持序列操作的数据结构D

1）D.build(x)以$\mathcal{O}(n)$时间

2）D.insert_at(i, x) 和D.delete_at(i)，每个都是$\mathcal{O}(\log n)$时间

当操作执行时，n个项目存储在D。描述算法，用提供的低级操作，实现下面高级操作。下面的每个操作，应该以$\mathcal{O}(k\log n)$时间执行。delete_at 返回删掉的项目。

(a) reverse(D, i, k)：反转D中，始于索引i，k个项目的顺序（上边界索引为 i+k-1 ）。

```python
def reverse(D, i, k):
    if k < 2:
        return
    x2 = D.delete_at(i + k - 1)
    x1 = D.delete_at(i)
    D.insert_at(i, x2)
    D.insert_at(i + k - 1, x1)
    reverse(D, i + 1, k - 2)
```

(b) move(D, i, k, j): 移动始于索引i的D中k个项目，以原有顺序，放到索引为 j 的项目前面。假设$i \leq j \le i+k$，不成立

```python
def move(D, i, k, j):
    if k < 1
        return
    x = D.delete_at(i)
    if j > i
        j = j - 1
    D.insert_at(j, x)
    j = j + 1
    if i > j
        i = i + 1
    move(D, i, k - 1, j)
```

# 1-3 Binder Bookmarks

Sisa Limpson是一个非常条理的二年级学生，她的所有课程笔记，整理为一页一页的，存在一个3环装订器。如果她有n页笔记在她的装订器，首页为索引0，最后一页为索引n-1。当学习时，Sisa经常重排笔记。为了帮助重新组织，她有两个书签，A和B，帮她记录装订器中的位置。

描述一个数据库来记录Sisa装订器的页，支持下面的操作，当操作发生时，有n个页在装订器中。假设在任意shift、move操作发生前，两个书签放置在装订器中。A总是比B有更小的索引。每个操作，声明运行时间为最坏情形的，还是摊还的。

build(X)

用迭代器X中的页，以$\mathcal{O}(|X|)$时间初始化数据库

---

place_mark(i, m)

把书签$m\in\{A,B\}$，放到索引 i 和索引 i+1之间，以$\mathcal{O}(n)$时间

---

read_page(i)

返回索引 i 处的页，以$\mathcal{O}(1)$时间

---

shift_mark(m, d)

书签$m\in\{A,B\}$，当前在索引为 i 的页前面，移动它到索引为 i+d 的页前面，$d\in\{-1,1\}$，以$\mathcal{O}(1)$时间

---

move_page(m)

获取当前处于书签$m\in\{A,B\}$前面的页，移动它到另外一个书签前面，以$\mathcal{O}(1)$时间

---

有多种可能的解法。首先注意问题声明，要求常量时间来 read_page(i) 操作，那只可能用基于数组的实现来支持，链表方式是不正确的。另外注意到：直到两个书签被放置，我们简单地存储所有页到一个尺寸为n的静态数组，因为没有操作会改变页序列，直到书签被放置。我们提出一个解法，概括了我们课上讨论的动态数组。另外一种常见的解法，可以减少为使用两个动态数组（一个以书签A为结尾、一个以书签B为结尾），加上一个基于数组的双端队列（如Problem Session 1中描述），来存储书签A和B中的页。

对于我们的方式，在两个书签放置后，我们将存储n页到一个尺寸为3n的静态数组S，无论何时build(X)或place_mark(i, m)被调用，我们可以$\mathcal{O}(n)$时间完整重建（n=|X|）。为了构建S：

* 放置子序列$P_1$在S开始：从索引0到书签A

* 跟着n个空数组位置

* 跟着子序列$P_2$，位于书签A和B之间

* 跟着n个空数组位置

* 跟着子序列$P_3$，从书签B到索引n-1

我们将保持“分隔”，$P_1,P_2,P_3$连续存储在S，它们之间有非0数量的空数组槽。我们也用4个符号保存4个索引：$a_1$指向$P_1$末尾，$a_2$指向$P_2$开始，$b_1$指向$P_2$结束，$b_2$指向$P_3$开始。

* 如果i<n，$n_1=|P_1|=a_1+1$，那么页在P1，我们返回页 S[i]

* 否则，如果$n_1\leq i\leq n_1+n_2$，$n_2=|P_2|=(b_1-a_2+1)$，那么页在$P_2$，我们返回页$S[a_2+(i-n_1)]$

* 否则，$i\gt a_1+n_2$，那么页在$P_3$，我们返回页$S[b2+(i-n_1-n_2)]$

只要存储索引的$a_1，a_2，b_1，b_2$保存着，这个算法就会返回正确的页，并且某些数学操作、单数组索引查找，以最坏情形$\mathcal{O}(1)$时间返回。

为了支持shift_mark(m, d)，移动处于索引$(a_1,a_2,b_1,b_2)$的页到索引位置$(a_2-1,a_1+1,b_2-1,b_1+1)$。这个算法保证了数据结构，因此是正确的，并以$\mathcal{O}(1)$时间运行，基于一个数组索引查找、一个索引写。注意，这个操作不会改变$P_1、P_2、P_3$之间的空间，因此操作的执行时间是最坏情形。

为了支持 move_page(m)，移动索引$(a_1,b_1)$处的相关页到索引位置$(b_1+1,a_1+1)$。如果执行这个移动打破了隔断（比如$(a_1,a_2)$或$(b_1,b_2)$变得相邻），如同上面描述的，重建整个数据结构。这个算法保存了数据结构的不变性，因此是正确的。注意这个算法：重建时，两个相邻段之间的空间是关闭的；重建完后，两个相邻的段之间有n个空位置。最多每次move_page操作，两个相邻段之间的额外空间会改变。因此，这个操作每n次操作，花费$\mathcal{O}(n)$时间，这个操作以分摊$\mathcal{O}(1)$时间执行。

# 1-4 双向链表

lecture2中，我们描述了一个单向链表，在本问题中，你将实现一个双向链表，支持另外一些常量时间操作。双向链表的每个节点x持有一个x.prev，指向序列中它前面的节点，另外，x.next指向序列中它后面的节点。一个双向链表L持有一个指针L.tail，指向序列尾部。另外，L.head，指向序列首部。对于这个问题，双向链表没有保存它的长度。

---

(a)给定一个上面描述的双向链表，描述算法来实现下面的序列操作，每个$\mathcal{O}(1)$时间

insert_first(x)，insert_last(x)，delete_first()，delete_last()

以下是支持请求操作的算法描述，这些算法每个都执行固定数量的任务，因此无需正确性论证。每个以$\mathcal{O}(1)$时间重新链接常量的指针、构建一个单独的节点。

insert_first(x)：构建一个新的双向链表节点a来存储x。如果双向链表是空的（例如，head和tail没有链接节点），那么把链表中的head和tail链接到a。否则，链表有一个头节点b，因此让a的next指针指向b，b的prev指针指向a，设置链表的head指向a。

insert_last(x)：构建一个新的双向链表节点a来存储x。如果双向链表是空的（例如，head和tail没有链接节点），那么把链表中的head和tail链接到a。否则，链表有一个尾节点b，因此让a的prev指针指向b，b的next指针指向a，设置链表的tail指向a。

delete_first(x)：这个方法，仅在链表至少包含一个节点时有意义，因此假设链表有一个头节点。从链表头，展开并存储项目x。然后设置head指向节点a（由head节点的next指针指向）。如果a不是一个节点，那么我们从链表中移除了最后一个项目，因此设置tail为None（head已经设为了None）。否则，设置新head的prev指针为None。然后返回x。

delete_last(x)：这个方法，仅在链表至少包含一个节点时有意义，因此假设链表有一个尾节点。从链表尾，展开并存储项目x。然后设置tail指向节点a（由tail节点的prev指针指向）。如果a不是一个节点，那么我们从链表中移除了最后一个项目，因此设置head为None（tail已经设为了None）。否则，设置新tail的next指针为None。然后返回x。

---

(b) 给定双向链表L两个节点$x_1和x_2$，$x_1$在$x_2$之前，描述一个常量时间的算法来移除$x_1$到$x_2$（包含）之间的所有节点，并将它们作为一个新的双向链表返回。

以$\mathcal{O}(1)$时间构建一个新的空链表$L_2$，设置它的head和tail为$x_1、x_2$。展开这个子链表，$x_1$为head、$x_2$为tail时必须注意。如果$x_1$是L的head，设置L的新head为节点a（$x_2$的next指针指向的节点），否则，设置$x_1$的prev指向的节点，其next指针指向a。相似得，如果$x_2$是L的尾部，设置L的新尾部为节点b（由x1的prev指针指向的节点），否则，设置$x_2$的next指针指向的节点，其prev指针指向b。

这个算法直接从$x_1$到$x_2$（包含）移除节点，因此是正确的，以$\mathcal{O}(1)$时间重新链接常量个指针。

(c) 给定节点x来自双向链表$L_1$、双向链表$L_2$，描述一个常量时间算法，将$L_2$splice到$L_1$中。splice操作之后，$L_1$应该包含之前在另外链表中的所有节点，并且$L_2$应该空的。

首先，让$x_1$和$x_2$为$L_2$的头和尾节点，$x_n$为x的next指针指向的节点（可能为None）。我们可以从$L_2$中移除所有节点，通过设置它的head和tail为None。然后splice节点，首先设置$x_1$的prev指针为x，并设x的next指针为$x_1$。相似得，设置$x_2$的next指针指向$x_n$。如果$x_n$是None，那么设置$x_2$为L的新tail；否则，设置$x_n$的prev指针指向$x_2$。

这个算法从$L_2$中直接插入节点到$L$，因此是正确的，以$\mathcal{O}(1)$时间执行，重新链接常量指针。

(d) 用提供的模板，实现Doubly_Linked_List_Seq类中的操作。不要更改Doubly_Linked_List_Node类。你可以从网站下载包含一些测试用例的代码模板。

```python
class Doubly_Linked_List_Seq:
    def insert_first(self, x):
        new_node = Doubly_Linked_List_Node(x)
          if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_last(self, x):
        new_node = Doubly_Linked_Node(x)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def delete_first(self):
        assert self.head
        x = self.head.item
        self.head = self.head.next
        if self.head is None:    self.tail = None
        else:    self.head.prev = None
        return x
    
    def delete_last(self):
        assert self.tail
        x = self.tail.item
        self.tail = self.tail.prev
        if self.tail is None:    self.head = None
        else:    self.tail.next = None
        return x
    
    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        L2.head = x1
        L2.tail = x2
        if x1 == self.head:    self.head = x2.next
        else:    x1.prev.next = x2.next
        if x2 == self.tail:    self.tail = x1.prev
        else:    x2.next.prev = x1.prev
        x1.prev = None
        x2.next = None
        return L2

    def splice(self, x, L2):
        xn = x.next
        x1 = L2.head
        x2 = L2.tail
        L2.head = None
        L2.tail = None
        x1.prev = x
        x.next = x1
        x2.next = xn
        if xn:    xn.prev = x2
        else:    self.tail = x2
```