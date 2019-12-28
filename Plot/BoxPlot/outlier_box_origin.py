【箱型图提供了识别异常值的一个标准】：异常值通常被定义为小于Q3－1.5IQR或大于Q1＋1.5IQR的值。
    箱型图依据实际数据绘制，没有对数据作任何限制性要求（如服从某种特定的分布形式），它只是真实直观地表现数据分布的本来面貌；
另一方面，箱型图判断异常值的标准以四分位数和四分位距为基础，四分位数具有一定的鲁棒性：多达25%的数据可以变得任意远而不会很大地扰动四分位数，所以异常值不能对这个标准施加影响。
由此可见，箱型图识别异常值的结果比较客观，在识别异常值方面有一定的优越性。 


def detectoutliers(list):
    print(type(list))
    outlier_indices = []
    # iterate over features(columns)
 
    # 1st quartile (25%)
    Q1 = np.percentile(list, 25)
    # 3rd quartile (75%)
    Q3 = np.percentile(list,75)
    # Interquartile range (IQR)
    IQR = Q3 - Q1
    # outlier step
    outlier_step = 1.5 * IQR
    # Determine a list of indices of outliers for feature col
    outlier_list_col = list[(list < Q1 - outlier_step) | (list > Q3 + outlier_step )]
 
    return outlier_list_col
