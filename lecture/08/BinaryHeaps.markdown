# 一、优先队列接口

* 记录一些项目，快速地访问/移除最重要的
  
  * 例：有限带宽的路由器，必须优先某些信息
  
  * 例：操作系统内核中的进程调度
  
  * 例：离散事件模拟（下一件事何时发生）
  
  * 例：图算法（接下来的课程中）

* 通过key有序的项目=优先，因此是集合接口（不是序列接口）

* 对集合特定操作子集进行了优化：
  
  * build(X)，由可迭代的X构建优先队列
  
  * insert(x)，添加项目x到数据结构
  
  * delete_max()，移除并返回拥有最大key的存储项目
  
  * find_max()，返回拥有最大key的存储项目

* 通常对最大或最小做出优化，而非全部

* 聚焦于insert和delete_max操作：build可以重复地insert；find_max可以是insert(delete_max())

# 二、优先队列排序

* 任何优先队列数据结构可以翻译为排序算法：
  
  * build(A)，按输入顺序，一个一个地插入项目
  
  * 重复地delete_min（或delete_max()）来决定（反向）顺序

* 所有艰难的工作发生在数据结构中

* 运行时间是：$T_{build}+n*T_{delete\_max}\le n*T_{insert}+n*T_{delete\_max}$
  
  我们已经看到的一些排序算法，可以被视作优先队列排序：

![](https://raw.githubusercontent.com/lialong/algorithms-6006/main/lecture/08/1.PNG)

# 三、优先队列：集合AVL树

* 集合AVL树支持insert(x)，find_min()，find_max()，delete_min()，delete_max()花费$\mathcal{O}(\log n)$

* 因此优先队列排序花费$\mathcal{O}(n\log n)$
  
  * 这源自lecture 7的AVL排序

* 可以通过子树新增变量，加速find_min()和find_max()为耗时$\mathcal{O}(1)$

* 但这个数据结构是复杂的，结果排序是非in-place的

* 是否存在一个更简单的数据结构用于优先队列，并且是$\mathcal{O}(n\log n)$ 时间复杂度的in-place排序？存在，二项堆和堆排序

* 在序列数据结构（数组）之上，实现集合数据结构，使用我们学过的二叉树

# 四、优先队列：数组

* 存储项目到一个无序动态数组

* insert(x)：追加x到最后，花费摊还$\mathcal{O}(1)$

* delete_max()：花费$\mathcal{O}(n)$找到最大的，交换最大的到最后，然后删除

* insert是快的，但delete_max是慢的

* 优先队列排序是选择排序！（加上一些拷贝）

# 五、优先队列：有序数组

* 存储项目到有序动态数组

* insert(x)：在末尾追加x，花费$\mathcal{O}(n)$交换到有序的位置

* delete_max()：从末尾删除花费摊还$\mathcal{O}(1)$

* 优先队列排序是插入排序！（加上一些拷贝）

* 我们可以从两个极端的数组优先队列中找到折中？

# 六、数组作为一个完全的二叉树

* 想法：数组表示完全二叉树