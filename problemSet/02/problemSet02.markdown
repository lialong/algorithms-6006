# 2-1 解决递归（Solving recurrences）

得出下面递归的解。解应该包含递归允许的最严格的上界和下界。假设$T(1)=\Theta(1)$

用两种方式解决part (a)、(b)、(c)，画一个递归树和应用主定理。用替代法解决part (d)

（a）$T(n)=4T(\frac{n}{2})+\mathcal{O}(n)$

递归树

深度 i 有$4^i$个顶点，每个最多$c\frac{n}{2^i}$次运算，因此深度 i 处最多$4^ic\frac{n}{2^i}$次运算。整个树加和，所有运算至多：

$\sum_{i=0}^{\log n}2^icn=cn\sum_{i=0}^{\log n}2^i=cn(2^{\log n+1}-1)<2cn^2=\mathcal{O}(n^2)$

因为每个叶子处运算为$\Theta(1)$，有$n^2$个叶子，所有运算至少$\Omega(n^2)$，得到$\Theta(n^2)$运行时间

主定理

a=4，b=2，符合主定理的情况1，因为$\log_ba=2,f(n)=\mathcal{O}(n^{2-\epsilon}),\epsilon\le1$，

所以$T(n)=\Theta(n^2)$

---

（b）$T(n)=3T(\frac{n}{\sqrt2})+\mathcal{O}(n^4)$

递归树

深度 i 有$3^i$个顶点，每个最多$c(\frac{n}{\sqrt2^i})^4=c\frac{n^4}{4^i}$次运算，因此深度 i 处最多$c\frac{3^i}{4^i}n^4$次运算。整个树加和，所有运算至多：

$\sum_{i=0}^{2\log n}c\frac{3^i}{4^i}n^4<\sum_{i=0}^{\infty}(\frac{3}{4})^icn^4=4cn^4$

因此$T(n)=\mathcal{O}(n^4)$。$3^{2\log n}=n^{2\log3}$个叶子节点，每个计算$\Theta(1)$，因此$T(n)$至少$\Omega(n^{2\log3})$

主定理

a=3，b=$\sqrt2$，选择$f(n)=\Theta(n^4)$，符合定理3，$T(n)=\mathcal{O}(n^4)$

因为$\log_ba=\log_{\sqrt2}3=2\log 3$，$n^4=\Omega(n^{2\log3+\epsilon})，\epsilon\le(3-2\log3)，$

$且3(\frac{n}{\sqrt2})^4=\frac{3}{4}n^4<cn^4,\frac{3}{4}<c<1$

选择$f(n)=0$，符合定理1，$T(n)=\Omega(n^{2\log3}),因为\log_ba=\log_{\sqrt2}3$