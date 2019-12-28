# -*- coding: utf-8 -*-

"""
本代码利用pyecharts模块实现地图可视化,展示上海市各区的数据分析师需求量的分布情况
"""
import pandas as pd
from pyecharts.charts import Geo,Map
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType

#提取出数据集中的可用数据
rawData = pd.read_csv('拉勾网数据分析岗位.csv')
#以公司位置为分组列，进行求和
sumNum = rawData[u'公司位置'].value_counts()
sumNum = sumNum.reset_index()  #索引项转化为数据列
sumNum.columns = ["place", "cnt"]  #修改DataFrame的列名


#pyecharts绘图所需的数据项（“上海区名”，“数据分析师的需求量”）
data = [tuple(z) for z in zip(sumNum.place,sumNum.cnt)]


def map_guangdong() -> Map:
    c = (
        Map()
        .add("Map",data, "上海")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-上海地图"),
            visualmap_opts=opts.VisualMapOpts(),
        )
    )
    return c

c = map_guangdong()
c.render(path="./上海市各区数据分析师的需求分布图.html")
