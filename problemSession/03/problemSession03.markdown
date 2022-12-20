# 3-1 Hash It Out

使用哈希函数$h(k)=(11k+4)\mod 9$，插入整数keys A=[67, 13, 49, 24, 40, 33, 58]到尺寸为9的哈希表。冲突应该通过链来解决，冲突被存储在链的尾部。画一个所有key被插入完后的哈希表图。

h(A)=[3,3,3,7,3,7,3]

0:

1:

2:

3:67->13->49->40->58

4:

5:

6:

7:24->33

8:

# 3-2 哈希序列(Hash Sequence)

哈希表不止对实现集合操作有用；它们也可用于实现序列（集合、序列接口定义在lecture 02）！给定一个哈希表，描述如何当作黑盒使用它（仅使用它的集合操作），来实现序列接口：

* build(A)，以期望$\mathcal{O}(n)$时间运行

* get_at和set_at，以期望$\mathcal{O}(1)$时间运行

* insert_at和delete_at，以期望$\mathcal{O}(n)$时间运行

* 四个动态first/last操作每个以分摊的、期望的$\mathcal{O}(1)$时间运行

使用一个哈希表H实现序列操作，把序列项目x存储在对象b（有b.key、b.val=x），我们将存储这些拥有键的对象到哈希比表中。我们也保存哈希表中最小的key s，为了维持不变式，n个存储项目有keys $(s,...,s+n-1)$，序列中的第i个项目存储在key为 s+i 的对象中。

为了实现build(A)，对于$A=(x_0,...,x_{n-1})$每个项目$x_i$，构成它的有键对象b，$b.key=i$进行初始化，最坏情形$\mathcal{O}(1)$时间；以期望的$\mathcal{O}(1)$时间使用Set的insert(b)写入到哈希表，总共时间为期望的$\mathcal{O}(n)$。初始化s=0确保不变式满足。

为了实现get_at(i)，用Set find(s+i)，以$\mathcal{O}(1)$时间返回key=s+i的存储对象的值，由不变式可知是正确的。相似地，为了实现set_at(i, ,k)，使用find(s+i)找到key=s+i的对象，改变它的值为x，也花费期望$\mathcal{O}(1)$时间。

为了实现insert_at(i, x)，对从s+n-1到s+i的j，使用delete(j)以期望$\mathcal{O}(1)$时间移除key=j的对象b，改变它的key为j+1花费最坏情形$\mathcal{O}(1)$时间，用insert(b)以期望$\mathcal{O}(1)$时间插入对象。用值x和key=s+i构建一个有键对象b'，并用insert(b')以期望$\mathcal{O}(1)$时间插入，总计期望$\mathcal{O}(n)$时间。这个操作恢复每个受影响项目的不变式。

相似地，为了实现delete_at(i)，用delete(s+i)以期望$\mathcal{O}(1)$时间移除存储在s+i处的对象b'。j从s+i+1到s+n-1，使用delete(j)以$\mathcal{O}(1)$时间移除key=j的对象b，以最坏情形$\mathcal{O}(1)$时间改变它的key=j-1，用insert(b)以$\mathcal{O}(1)$时间插入对象。返回对象b'的值，总共花费期望$\mathcal{O}(n)$时间。这个操作通过不变式返回正确的值，恢复每个受影响项目的不变式。

为了实现insert_last(x)或delete_last()，简单地以期望$\mathcal{O}(1)$时间insert_at(s+n)或delete_at(s+n-1)，因为没有对象需要被移动。

为了实现insert_first(x)，构建一个有键的对象b，值为x、key=s-1，用insert(b)以期望$\mathcal{O}(1)$时间插入它。设置存储值s=s-1，恢复不变式。delete_first()是相似得，使用delete(s)以$\mathcal{O}(1)$时间移除key=s的对象，返回对象的值。然后设置s的存储值为s+1，恢复不变性。

# 3-3 生物排序（Critter sort）

Ashley Getem收集、训练口袋兽，与其他口袋兽战斗。她总共收集了n个口袋兽，她对每个口袋兽$C_i$保存一些统计数据。基于下面每种key，描述高效算法来对Ashley的口袋兽排序。

(a) 物种ID：一个整数$x_i$，-n到n之间（负ID是脾气暴躁的）

这些整数时线性的、有界的，但不是正数。因此用最坏情形$\mathcal{O}(n)$时间对每个口袋兽的ID加n，那么对于所有i，$x_i\le2n=u$。对它们使用计数排序，最坏情形用时$\mathcal{O}(n+2n)=\mathcal{O}(n)$，然后对每个ID减n，最坏情形用时$\mathcal{O}(n)$

(b) 名字：一个唯一的字符串$s_i$，包含最多$10\lceil\lg n\rceil$个英文字母

让我们假设：每个字符串存储在连续的内存块，数字（常数k为边界，比如26用于英文字母编码、256用于字节编码）代表每个字符进行编码，如果在字母表中$c_i$在$c_j$前面，那么字符$c_i$的数字表示小于另外字符$c_j$。每个字符串可被视作一个整数：0到$u=k^{10\lceil\lg n\rceil}=\mathcal{O}(n^{10\lceil\lg k\rceil})=n^{\mathcal{O}(1)}$，以常数个机器字存储，因此可用基数排序进行排序，耗时$\mathcal{O}(n+n\log_n{n^{\mathcal{O}(1)}})=\mathcal{O}(n)$。

可选择地，如果每个字符串$s_i$中每个字符用它自己的机器字存储，那么输入尺寸$\Theta(n\log n)$。对每个字符串，计算它的$n^{\mathcal{O}(1)}$数字表达，需要$\mathcal{O}(\log n)$个数学运算（每个数学运算以$\mathcal{O}(1)$时间运行，因为每个中间表达最多10个机器字）。然后像上面那样使用基数排序。计算字符串的数字表达式花费$\mathcal{O}(n\log n)$时间，与输入尺寸是线性关系。

(c) 战斗次数：一个小于$n^2$的正数$f_i$

这些整数有多项式（polynomially）边界：$u=n^2$，因此对它们使用基数排序进行排序，最坏情形$\mathcal{O}(n+n\log_nn^2)=\mathcal{O}(n)$时间

(d) 胜率，比率$w_i/f_i$，$w_i\le f_i$是战斗胜利的次数

非整数除法可能产生一个数，需要无限个数字来表示，因此我们不能直接计算这些数字。没有考虑精度地尝试计算、比较这些数字的解法，不能得分。有两个解法。

第一个解法使用最优的比较排序算法（像归并排序）来对胜率排序，花费$\mathcal{O}(n\log n)$时间。通过交叉乘法，两个胜率$w_1/f_1和w_2/f_2$可比，因为当且仅当$w_1f_2<w_2f_1$时，$w_1/f_1<w_2/f_2$。这种解法得4/5分。

第二个解法是更棘手的。想法是有效地放缩比例，使得它们不相等时，整数部分也不相等。首先，对每个胜利次数，计算$w_i'=w_i \sdot n^4$耗时$\mathcal{O}(1)$。通过整数除法计算$p_i=\lfloor w_i'/f_i\rfloor$耗时$\mathcal{O}(1)$,$w_i'=p_i\sdot f_i+q_i,q_i=w_i'\mod f_i$。那么，因为每个$p_i$是一个正整数，边界为$\mathcal{O}(n^6)$，我们可以用最坏情形$\mathcal{O}(n+n\log_nn^6)=\mathcal{O}(n)$时间利用$p_i$通过基数排序进行排序。

现在我们必须证明：利用$p_i$排序等价于利用$w_i/f_i$。当前仅当$p_i-p_j>0$为真，足以证明：$w_i/f_i-w_j/f_j>0$为真。假设$d_w=w_i/f_i-w_j/f_j>0$。
