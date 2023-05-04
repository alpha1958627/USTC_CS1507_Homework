# import os.path
# import time
# import random

# import pandas as pd
# import streamlit as st
# from streamlit_echarts import st_pyecharts
# import streamlit.components.v1 as components
# from pyecharts import options as opts
# from pyecharts.charts import Line
# from streamlit_faker import get_streamlit_faker
# st.set_page_config(layout="wide")

# Institution_lst=['工程科学学院','先进技术','管理学院','化学与材料科学学院','大数据学院','中国科学院','少年班学院','地球和空间科学学院','公共事务学院','环境科学与工程','近代力学','信息','微电子学院','火灾科学国家重点实验室','计算机学院','核科学技术学院','同步辐射','生医部','热科学','精密仪器','物理学院','化学学院','马克思主义','金融','科技传播','微尺度','人文','数学学院','天文','网络空间安全']
# Institution=['工程科学学院','先进技术研究院','管理学院','化学与材料科学学院','大数据学院','中国科学院','少年班学院','地球和空间科学学院','公共事务学院','环境科学与工程','近代力学','信息','微电子学院','火灾科学国家重点实验室','计算机学院','核科学技术学院','同步辐射','生医部','热科学','精密仪器','物理学院','化学学院','马克思主义','金融','科技传播','微尺度','人文','数学学院','天文','网络空间安全']


# # def panel():
# #     st.title('Data panel')
# #     col1, col2, col3 = st.columns(3)
# #     col1.metric("Temperature", "70 °F", "1.2 °F")
# #     col2.metric("Wind", "9 mph", "-8%")
# #     col3.metric("Humidity", "86%", "4%")



                                                                   
# if __name__ == '__main__':
#     # panel()
#     st.write('aaa')

import os.path
import time
import random

import pandas as pd
import streamlit as st
from streamlit_echarts import st_pyecharts
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

Institution_lst=['工程科学学院','先进技术','管理学院','化学与材料科学学院','大数据学院','中国科学院','少年班学院','地球和空间科学学院','公共事务学院','环境科学与工程','近代力学','信息','微电子学院','火灾科学国家重点实验室','计算机学院','核科学技术学院','同步辐射','生医部','热科学','精密仪器','物理学院','化学学院','马克思主义','金融','科技传播','微尺度','人文','数学学院','天文','网络空间安全']
Institution=['工程科学学院','先进技术研究院','管理学院','化学与材料科学学院','大数据学院','中国科学院','少年班学院','地球和空间科学学院','公共事务学院','环境科学与工程','近代力学','信息','微电子学院','火灾科学国家重点实验室','计算机学院','核科学技术学院','同步辐射','生医部','热科学','精密仪器','物理学院','化学学院','马克思主义','金融','科技传播','微尺度','人文','数学学院','天文','网络空间安全']

def Show_ins():
    with st.form(key='news' ):
        st.header('Independent presentation of news title and release time from each institution')
        options = st.multiselect('Choose Institution that you want to know', Institution)
        submission_button = st.form_submit_button(label='Start')
        if submission_button:
            for ins in options:
                i = Institution_lst.index(ins)
                st.write(f'# Displaying news of{Institution[i]}')
                df = pd.read_csv(f'./data_ins/{Institution_lst[i]}.csv')
                st.write(df)
if __name__ == '__main__':
    Show_ins()