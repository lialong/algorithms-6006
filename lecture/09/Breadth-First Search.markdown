# 一、新单元：图

* Quiz 1包含lecture01到lecture08，关注数据结构和排序

* 今天开始新单元，lecture09-lecture14，关注图算法

# 二、图应用

* 图无处不在

* 任何网络系统都存在有向连接图

* 比如：路网、计算机网络、社交网络

* 任何离散系统的状态空间都可以用过渡图表示

* 比如：puzzle & games like Chess, Tetris, Rubik’s cube

* 比如：应用流，声明

# 三、图定义

![](https://raw.githubusercontent.com/lialong/algorithms-6006/main/lecture/09/1.png)

* 图$G=(V,E)$是一组点V和一组顶点的对$E\subseteq V\times V$

* 有向边是有序对，比如，$(u,v)，u,v \in V$

* 无向边是无序对，比如，$\{u,v\}，u,v\in V$，比如：$(u,v)和(v,u)$

* 在这个类中，我们假设所有图是简单的：
  
  * 边是去重的，比如(u,v)仅在E（尽管(v,u)可能出现）中出现一次，并且
  
  * 边是非重复点的组合，比如：$u\ne v，(u,v)\in E$
  
  * 简单暗示着：$|E|=\mathcal{O}(|V|^2)$，因为无向：$|E|=\mathcal{O}(|V|^2)$，有向：$|E|=\mathcal{O}(2|V|^2)$

# 四、相邻集合

* $u\in V，u的出向相邻：Adj^+(u)=\{v\in V|(u,v)\in E\}$

* $u\in V，u的入向相邻：Adj^-(u)={v\in V|(u,v)\in E}$

* 顶点u的出度，$u\in V，deg^+(u)=|Adj^+(u)|$

* 顶点u的出度，$u\in V，deg^-(u)=|Adj^-(u)|$

* 对于无向图，$Adj^-(u)=Adj^+(u)，deg^-(u)=deg^+(u)$

* 删除上标默认是出向，比如，$Adj(u)=Adj^+(u)，deg(u)=deg^+(u)$

# 五、图的表达

* 为了存储图$G=(V,E)$，我们需要存储外向边$Adj(u)，u\in V$

* 首先，需要一个集合数据结构$Adj$来映射u到$Adj(u)$

* 然后对于每个u，需要存储$Adj(u)$到其他数据结构——邻接表

* 通常对Adj使用直接访问数组或哈希表，因为想通过顶点快速查找

* 通常对每个Adj(u)使用数组或链表，因为通常只需要迭代

* 通用表达：$Adj尺寸为\Theta(|V|)，每个Adj(u)尺寸为\Theta(deg(u))$

* 因为由handshaking lemma得知$\sum_{u\in V}deg(u)\le2|E|$，图存储空间为$\Theta(|V|+|E|)$

* 因此，对于图算法，线性时间意味着$\Theta(|V|+|E|)$，与图尺寸呈线性

# 六、举例

* 例1和例2假设顶点标记为$\{0,1,...,|V|-1\}$，因此可以对Adj使用直接访问数组，存储Adj(u)到数组。例3对Adj使用哈希表。