"""
热力图
-------
表示不同变量之间的关系，单元格颜色越深，代表该单元格交叉的两个变量相关性越强
"""

plt.rcParams["font.sans-serif"]='SimHei'
plt.rcParams['axes.unicode_minus'] = False

corr = data_df.corr()#计算各变量的相关性系数
xticks = list(corr.index) #x轴标签
yticks = list(corr.index) #y轴标签
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
sns.heatmap(corr, annot=True, cmap="rainbow",ax=ax1,linewidths=.5, annot_kws={'size': 9, 'weight': 'bold', 'color': 'blue'})
ax1.set_xticklabels(xticks, rotation=35, fontsize=10)
ax1.set_yticklabels(yticks, rotation=0, fontsize=10)
plt.show()
