import os.path
import time
import random

import pandas as pd
import streamlit as st
from streamlit_echarts import st_pyecharts
import streamlit.components.v1 as components
from pyecharts import options as opts
from pyecharts.charts import Line
# st.set_page_config(layout="wide")

Institution_lst=['工程科学学院','先进技术','管理学院','化学与材料科学学院','大数据学院','中国科学院','少年班学院','地球和空间科学学院','公共事务学院','环境科学与工程','近代力学','信息','微电子学院','火灾科学国家重点实验室','计算机学院','核科学技术学院','同步辐射','生医部','热科学','精密仪器','物理学院','化学学院','马克思主义','金融','科技传播','微尺度','人文','数学学院','天文','网络空间安全']
Institution=['工程科学学院','先进技术研究院','管理学院','化学与材料科学学院','大数据学院','中国科学院','少年班学院','地球和空间科学学院','公共事务学院','环境科学与工程','近代力学','信息','微电子学院','火灾科学国家重点实验室','计算机学院','核科学技术学院','同步辐射','生医部','热科学','精密仪器','物理学院','化学学院','马克思主义','金融','科技传播','微尺度','人文','数学学院','天文','网络空间安全']

# @st.cache
def line():
    with st.form(key='news' ):
        st.header('Trend')
        st.sidebar.markdown('## Select Time interval')
        interval = st.sidebar.selectbox('Detector', ['Annual','Monthly','Daily'])
        # dt = st.sidebar.slider('Time Range (seconds)', 0.1, 8.0, 1.0)  # min, max, default
        # dt = 
        # st.write(dt)
        st.sidebar.markdown('## Select Institution')
        options = st.sidebar.multiselect('Institution', Institution)
        submission_button = st.form_submit_button(label='Start')
        if submission_button:
            for ins in options:
                i = Institution.index(ins)
                st.write(f'# Displaying news of { Institution[i]}')
                df = pd.read_csv(f'./data_ins/{Institution_lst[i]}.csv')
                # 读取数据集并进行必要的数据清理和转换
                if interval == 'Annual':

                    df['date'] = pd.to_datetime(df['time'], format='%Y/%m%d')
                    # print(df['date'])
                    df['year']=df['date'].dt.year
                    # print(df['year'])
                    df = df.sort_values(by=['year'])
                    cost_data = df.groupby('year')['pay'].sum().reset_index()
                     # 创建直方图
                    st.bar_chart(cost_data.set_index('year'),use_container_width=True,height=500)
               
                elif interval == 'Monthly':
                    df['date'] = pd.to_datetime(df['time'], format='%Y/%m%d')
                    df = df.sort_values(by=['date'])
                    df['monthly']=df['date'].dt.strftime('%Y-%m')
                    cost_data = df.groupby('monthly')['pay'].sum().reset_index()
                    line_chart = (
                    Line()
                    .add_xaxis(list(cost_data['monthly']))
                    .add_yaxis('pay',cost_data['pay'],linestyle_opts=opts.LineStyleOpts(width=3))
                    .set_global_opts(
                        xaxis_opts=opts.AxisOpts(name="时间"),
                        yaxis_opts=opts.AxisOpts(name="费用"),
                        title_opts=opts.TitleOpts(title="费用随时间变化")
                    )
                    )
                    st_pyecharts(line_chart,height=500)

                elif interval == 'Daily':
                    df['date'] = pd.to_datetime(df['time'], format='%Y/%m%d')
                    df = df.sort_values(by=['date'])
                    cost_data = df.groupby('date')['pay'].sum().reset_index()
                    line_chart = (
                    Line()
                    .add_xaxis(list(cost_data['date'].dt.strftime('%Y-%m-%d')))
                    .add_yaxis('pay',cost_data['pay'],linestyle_opts=opts.LineStyleOpts(width=3))
                    .set_global_opts(
                        xaxis_opts=opts.AxisOpts(name="时间"),
                        yaxis_opts=opts.AxisOpts(name="费用"),
                        title_opts=opts.TitleOpts(title="费用随时间变化"),
                    )
                    )
                    st_pyecharts(line_chart,height=500)
           
                # 在Streamlit应用程序中显示折线图
                
                                                                   
if __name__ == '__main__':
    line()



