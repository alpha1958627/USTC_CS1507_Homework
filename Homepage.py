import streamlit as st
from st_aggrid import AgGrid
from streamlit_echarts import st_pyecharts
import pandas as pd
from streamlit_extras.colored_header import colored_header
from analysis import read_data
# st.set_page_config(layout="wide")
Institution_lst=['工程科学学院','先进技术','管理学院','化学与材料科学学院','大数据学院','中国科学院','少年班学院','地球和空间科学学院','公共事务学院','环境科学与工程','近代力学','信息','微电子学院','火灾科学国家重点实验室','计算机学院','核科学技术学院','同步辐射','生医部','热科学','精密仪器','物理学院','化学学院','马克思主义','金融','科技传播','微尺度','人文','数学学院','天文','网络空间安全']
Institution=['工程科学学院','先进技术','管理学院','化学与材料科学学院','大数据学院','中国科学院','少年班学院','地球和空间科学学院','公共事务学院','环境科学与工程','近代力学','信息','微电子学院','火灾科学国家重点实验室','计算机学院','核科学技术学院','同步辐射','生医部','热科学','精密仪器','物理学院','化学学院','马克思主义','金融','科技传播','微尺度','人文','数学学院','天文','网络空间安全']
    # Define function to read CSV and return DataFrame

if __name__ == '__main__':
   
    st.title('USTC_CS1507 Homework1')
    
    colored_header(
    label=" A news crawling script",
    description="PB21050971梁家华",
    color_name="orange-80",
)
    
    for i in range (0,len(Institution)):
        df1 = read_data(i)
        if i == 0:
            df = df1
        else:
            df = pd.concat([df,df1])
    st.write('# Displaying data from all colleges')
    st.write(df)

# streamlit run 
