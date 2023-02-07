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
  
  * 首次提出的平衡方式为AVL树

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
    
    ![](http://cdn-qy.zjw.net/logo/lll/1dfcb74d2e5ecd07a0fb5bb45171983b.png@!f_200x200)