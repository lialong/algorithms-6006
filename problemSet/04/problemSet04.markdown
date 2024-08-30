# 4-1 二叉树练习（Binary Tree Practice）

## (a)

下面的Set Binary Tree T不是高度平衡的，但满足二叉搜索树属性，假设每个整数项的key都是其本身。指出所有高度不平衡的节点的key，并计算它们的偏斜。

![](C:\Users\lizelong\AppData\Roaming\marktext\images\2024-08-30-15-42-26-image.png)

解：包含键16和37的节点没有高度平衡。它们的偏斜度分别为2和-2。

## (b)

在T上依次执行以下插入和删除操作，通过添加或删除叶子保持二叉搜索树属性（可能需要将一个键向下交换到一个叶子中）。对于此部分，不要使用旋转来平衡树。每次操作后绘制修改后的树。

T.insert(2)
T.delete(49)
T.delete(35)
T.insert(85)
T.delete(84)

![](C:\Users\lizelong\AppData\Roaming\marktext\images\2024-08-30-15-42-26-image.png)