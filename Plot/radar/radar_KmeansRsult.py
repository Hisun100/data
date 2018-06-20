# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#用于正确显示中文信息
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False   #用来正常显示负号

#fig, ax = plt.subplots() 
#ax.set_title(u'客户群特征分析雷达图')
#line1, = ax.plot(t, y1, lw=2, color='red', label='1 HZ')
#line2, = ax.plot(t, y2, lw=2, color='blue', label='2 HZ')


def plot_radar(data,attr_labels,labels):
    """绘制一维数组数据的雷达图"""
    sample_num = data.shape[0] #样本数
    dataLenght = data.shape[1] #数据长度
    print(sample_num,dataLenght)
    #获取角度信息
    angles = np.linspace(0, 2*np.pi, dataLenght, endpoint=False) # 分割圆周长
    angles = np.concatenate((angles, [angles[0]])) # 闭合    
    #绘图标记
    marker = ['r--','g--','b--','y--','k--']
#    fig, ax = plt.subplots(projection='polar')
    #创建绘图对象
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)# polar参数！！
    ax.set_title('客户群特征分析雷达图') 
    for i in range(sample_num):
        print(i)
        data_tmp = data[i,:]
        print(data_tmp)
        #数据准备
        data_tmp = np.concatenate((data_tmp, [data_tmp[0]])) # 闭合
        """调试出错处1"""
        ax.plot(angles, data_tmp, marker[i], linewidth=2, label = labels[i]) #做极坐标系
        ax.set_thetagrids(angles * 180/np.pi, attr_labels) # 做标签
        #ax.fill(angles, data_tmp, facecolor='r', alpha=0.25)# 填充
#        ax.set_ylim(0,12)  
    leg = ax.legend(fancybox=True, shadow=True) #显示图例
    leg.get_frame().set_alpha(0.4) #图例框的透明度
    
    
resultfile = './data/tmp/kmeansresult.xls' 

data = np.array([[1,4,5,2,3],[6,4,5,8,6],[3,5,7,8,9],[1,2,5,6,2]],dtype='float64') # 数据
#attr_labels = ['ZL','ZR','ZF','ZM','ZC']# 属性标签
#labels = ['客户群1','客户群2','客户群3','客户群4','客户群5'] # 图例标签 

df = pd.read_excel(resultfile)
"""调试出错处2"""
#data = df.values[:,1:]
#print(type(data))
attr_labels = df.columns[1:]
labels = df.index
plot_radar(data,attr_labels,labels)

