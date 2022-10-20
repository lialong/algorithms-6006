# 1-1函数的渐进性

对于下面5个函数集合中每一个，对它们进行排序。如果在序列中，$f_a$出现在$f_b$之前，那么$f_a=\mathcal{O}(f_b)$。如果$f_a=\mathcal{O}(f_b)$且$f_b=\mathcal{O}(f_a)$，意味着$f_a$和$f_b$可以任何顺序出现，可以用花括号把$f_a和f_b$围起来表明这种情况。例如，如果多个函数为：

$f_1=n，f_2=\sqrt{n}，f_3=n+\sqrt{n}$

正确的答案是：$(f_2,\{ f_1 , f_3 \} )或(f_2,\{ f_3 , f_1 \} )$

a) $f_1=(logn)^{2019}，f_2=n^2log(n^{2019})，f_3=n^3，f_4=2.019^n，f_5=nlogn$

$f_1,f_5,f_2,f_3,f_4$

b) $f_1=2^n,f2=n^3,f_3=\binom{n}{n/2},f_4=n!,f_5=\binom{n}{3}$

$\{f_2,f_5\},f_3,f_1,f_4$

# 1-2队列基本操作

 给定一个数据结构D，支持4个 first/last 序列操作：

D.insert_first(x)，D.delete_first()，D.insert_last(x)，D.delete_last()

每个操作都是$\mathcal{O}(1)$，描述算法：用低级操作方法来实现下面高级操作。

删除操作返回删除的元素。

(a) swap_ends(D):以$\mathcal{O}(1)$复杂度交换序列中第一个和最后一个元素。

first = D.delete_first()

end = D.delete_last()

D.insert_first(end)

D.insert_last(first)

(b)shift_left(D,k):以$\mathcal{O}(k)$复杂度把前k个元素按顺序移动到序列末尾，移动完后，之前序列中的第k个元素成为末尾，之前序列中的第k+1个元素成为序列之首。

for(int i=0; i < k; i++) {

    tmp = D.delete_first();

    D.insert_last(tmp)

}

# 1-3双端队列操作

动态数组可以实现一个序列接口，支持最坏情形$\mathcal{O}(1)$时间索引（根据角标i找到对应元素），以及从数组后面插入、删除item是可变常量时间（插入n个item，时间为$\mathcal{O}(n)）$。然而在动态数组前面插入和删除，并非足够有效的，因为每个entry必须移动来保持序列所有entry的有序性，花费线性时间。

另一方面，链表数据结构，在两端都可以最坏情形$\mathcal{O}(1)$支持插入、删除操作，但代价是线性时间查找。

我们可以两个好处都占：设计一个数据结构来存储一系列的item，支持最坏情形$\mathcal{O}(1)$时间索引查找，以及可摊还$\mathcal{O}(1)$时间在两端插入和删除。你的数据结构应该使用$\mathcal{O}(n)$空间来存储n个item。

有多种可能的解法。一种解法：使用两个栈（stack）来实现dequeue（双端队列），需要关注的是：从空栈中弹出（pop），向满栈中压入（push）。一个可选择的方式是：将队列元素存储到数组中间，而不是前面，无论何时重建（rebuild），都在首尾留有线性数量的额外槽（slot），保证仅会每n次操作用线性时间重建（rebuild）。

例如，无论何时重新分配空间来存储n个元素（item），把它们拷贝到一个长度m=3n的数组中部。为了插入、删除一个序列头部、尾部的元素，以常量时间在任意端添加、删除元素。如果插入时没有空槽（slot）存在，那么自从上次重建（rebuild）至少线性数量插入必然已经发生，因此我们可以负担得起重建数组。如果移除一个元素，让比例n/m小于1/6，那么自从上次重建（rebuild）至少m/6=$\Omega(n)$个移除一定已经发生，因此我们也可以负担得起重建数组。

昂贵的线性时间重建之间，线性数量的操作确保每次动态操作花费最多$\mathcal{O}(1)$时间。为了支持常量时间的数组索引，我们保存索引i：数组最左边的元素位置，以及数组存储元素数量n，对于每次更新以常量时间（最坏情形）来维持。为了访问存储在队列的$j^{th}$元素，确保 i+j<n，以常量时间（最坏情形）返回数组容器i+j处的元素。

# 1-4 Jen & Berry

课间休息时，Jen开着她的冰激淋小车到当地小学。所有孩子冲到她卡车前排队。Jen承载的学生数量（有2n个）溢出了，因此她叫了她的合伙人Berry，带来他的冰淇淋车帮她解脱。Berry很快到达，停在学生队伍的另一端。他为队伍最后的学生提供售卖，但其他学生反对：”最后的学生应该是最后面，这不公平“。

学生决定最公平的方式是纠正现状，把队伍的后半段（离Jen最远的n个孩子）反向排序，然后排到Berry的卡车，因此原始队伍的最后一名孩子，成为了Ben队伍中的最后一名孩子，原始队伍第$(n+1)^{st}$个孩子成为Berry的首个顾客。

（a）给定一个包含2n孩子姓名的链表，按照Jen的卡车前面形成的原始队列（首个节点包含队伍首个孩子的姓名），描述一个$\mathcal{O}(n)$时间复杂度的算法，来更改链表，反转list后半段顺序。操作期间，你的算法应该不产生任何新的链表节点，或实例化任意新的非常量尺寸数据结构。

解：以3步反序list中后半段node节点：

*找到序列中$n^{th}$节点a（Jen队伍的最后）

*从$(n+1)^{st}$节点b到$(2n)^{th}$节点c遍历节点x，改变x的next指针，指向原始序列中x前的节点

*修改a的next指针指向c，b的next指针指向null

找$n^{th}$节点需要从list头部遍历next指针n-1次，可以通过简单循环以$\mathcal{O}(n)$时间完成。我们可以通过减半list尺寸（保证是偶数）来计算n。

为了改变序列后半段的next指针，我们可以保存指向当前节点x、x前面节点$x_p$的指针，初始化b和a。然后记录x之后的节点为$x_n$，重新链接x指向$x_p$（x前面的节点，时间复杂度$\mathcal{O}(1)$），我们可以改变当前节点为$x_n$，前驱节点为x，保存后驱需要的属性用于重新链接（relink）。重复n次，以$\mathcal{O}(n)$时间重新链接（relink）序列后半段所有n节点。

最后，当算法遍历list时，通过记住节点a、b、c，意味着：改变头部异常的next指针，反向list后半段花费$\mathcal{O}(1)$，致使一个$\mathcal{O}(n)$时间复杂度的算法。

（b）写一个python函数 reorder_students(L) 实现你的算法

解：

```python
class Node:
    def __init__(self, name: str):
        self.name = name
        self.next = None

class LinkedList:
    def __init__(self, head: Node):
        self.head = head

def get_list(num):
    head = Node(0)
    pre = head
    for i in range(1, num):
        node = Node(i)        
        pre.next = node
        pre = node
    list = LinkedList(head)
    list.size = num
    return list

def print_list(L):
    node = L.head
    for _ in range(0, L.size):
        print(node.name)
        node = node.next        

def reorder_students(L):
    n = L.size//2
    a = L.head
    for _ in range(1, n):
        a = a.next
    b = a.next
    x_p,x = a,b
    for _ in range(0, n):
        x_n = x.next
        x.next = x_p
        x_p, x = x, x_n        
    a.next = x_p
    b.next = None


if __name__ == "__main__":
    list = get_list(10);
    print_list(list)
    print("---------------------------")
    reorder_students(list)
    print_list(list)
```