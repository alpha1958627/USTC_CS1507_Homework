import os.path
import time
import random
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_echarts import st_pyecharts
import streamlit.components.v1 as components
from pyecharts.charts import Line
st.set_page_config(layout="wide")

Institution_lst=['工程科学学院','先进技术','管理学院','化学与材料科学学院','大数据学院','中国科学院','少年班学院','地球和空间科学学院','公共事务学院','环境科学与工程','近代力学','信息','微电子学院','火灾科学国家重点实验室','计算机学院','核科学技术学院','同步辐射','生医部','热科学','精密仪器','物理学院','化学学院','马克思主义','金融','科技传播','微尺度','人文','数学学院','天文','网络空间安全']
Institution=['工程科学学院','先进技术研究院','管理学院','化学与材料科学学院','大数据学院','中国科学院','少年班学院','地球和空间科学学院','公共事务学院','环境科学与工程','近代力学','信息','微电子学院','火灾科学国家重点实验室','计算机学院','核科学技术学院','同步辐射','生医部','热科学','精密仪器','物理学院','化学学院','马克思主义','金融','科技传播','微尺度','人文','数学学院','天文','网络空间安全']

def animation():
    with st.form(key='news' ):
        st.header('Trend')
        st.sidebar.markdown('## Select Institution')
        options = st.sidebar.multiselect('Institution', Institution)
        submission_button = st.form_submit_button(label='Start')
        if submission_button:
            for ins in options:
                i = Institution.index(ins)
                st.write(f'# Displaying news of { Institution[i]}')
                df = pd.read_csv(f'./data_ins/{Institution_lst[i]}.csv')
                df['date'] = pd.to_datetime(df['time'], format='%Y/%m%d')
                df = df.sort_values(by=['date'])
                cost_data = df.groupby('date')['pay'].sum().reset_index()
                progress_bar = st.sidebar.progress(0)
                status_text = st.sidebar.empty()
                last_rows = np.random.randn(1, 1)
                chart = st.line_chart(last_rows)

                for i in range(1, len(cost_data)):
                    # print(last_rows[-1, :]+ cost_data['pay'][i])
                    new_rows = last_rows[-1, :] + cost_data['pay'][i]
                    a=round(100*i/(len(cost_data)-1))
                    status_text.text("%a%% Complete" % a)
                    chart.add_rows(new_rows)
                    progress_bar.progress(a)
                    # last_rows = new_rows
                    time.sleep(0.05)

                progress_bar.empty()

     
if __name__ == '__main__':
   animation()
    