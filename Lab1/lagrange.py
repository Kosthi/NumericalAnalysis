#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[3]:


# 拉格朗日插值多项式
def lagrange(x_known, y_known, x_new):
    n = len(x_known)
    y_new = 0
    for i in range(n):
        p = y_known[i]
        for j in range(n):
            if j != i:
                p *= (x_new - x_known[j]) / (x_known[i] - x_known[j])
        y_new += p
    return y_new
# 原函数
def fun(x):
    return 1 / (1 + x * x)


# In[4]:


# 获取 n=2, 4, 6...插值点
total_x = []
for n in range(2, 11, 2):
    x = []
    for k in range(n + 1):
        x.append(-5 + 10 / n * k)
    total_x.append(x)


# In[10]:


# 生成样本点
x0 = np.arange(-5, 5.1, 0.1)

# 生成figure和ax实例
fig, ax = plt.subplots(figsize=(8, 6), layout='constrained')

# 画主函数图像
ax.plot(x0, fun(x0), label='f(x)')

# 画 n=2, 4, 6...插值曲线
for i in range(len(total_x)):
    # 定义已知的数据点
    x_known = np.array(total_x[i])
    y_known = np.array(fun(np.array(total_x[i])))
    # 绘制插值曲线
    ax.plot(x0, lagrange(x_known, y_known, x0), label=f'n={(i + 1) * 2}')

# 设置图的属性
ax.set_xlabel('x')  # x-label
ax.set_ylabel('y')  # y-label
ax.set_title("Lagrange interpolation")  # title
ax.legend(loc='upper right', bbox_to_anchor=(1.18, 1)) # 显示图例，对应ax.plot()中的lable属性
ax.grid() # 显示网格
fig.savefig('lagrange.png', dpi=200) # 保存图片


# In[11]:


get_ipython().system('jupyter nbconvert --to script lagrange.ipynb')


# In[ ]:




