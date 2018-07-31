#相关性探索--相关系数图
def plot_correlation_map(df):
    """相关系数图_correlationMap:数据集中各属性之间的相关性"""
    corr = df.corr()
    _, ax = plt.subplots(figsize=(12, 10))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    _ = sns.heatmap(
        corr,
        cmap=cmap,
        square=True,
        cbar_kws={'shrink': .9},
        ax=ax,
        annot=True,
        annot_kws={'fontsize': 15},
        fmt='.2f'
    )

#plot_correlation_map(rawData_train.drop([u'地级市'],axis=1))  
