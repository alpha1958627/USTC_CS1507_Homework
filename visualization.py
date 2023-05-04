import streamlit as st
import streamlit.components.v1 as components
from st_aggrid import AgGrid
from streamlit_echarts import st_pyecharts
import pandas as pd
import numpy as np
import time
from streamlit_extras.colored_header import colored_header

# st.set_page_config(layout="wide")
Institution_lst=['工程科学学院','先进技术','管理学院','化学与材料科学学院','大数据学院','中国科学院','少年班学院','地球和空间科学学院','公共事务学院','环境科学与工程','近代力学','信息','微电子学院','火灾科学国家重点实验室','计算机学院','核科学技术学院','同步辐射','生医部','热科学','精密仪器','物理学院','化学学院','马克思主义','金融','科技传播','微尺度','人文','数学学院','天文','网络空间安全']
Institution=['工程科学学院','先进技术','管理学院','化学与材料科学学院','大数据学院','中国科学院','少年班学院','地球和空间科学学院','公共事务学院','环境科学与工程','近代力学','信息','微电子学院','火灾科学国家重点实验室','计算机学院','核科学技术学院','同步辐射','生医部','热科学','精密仪器','物理学院','化学学院','马克思主义','金融','科技传播','微尺度','人文','数学学院','天文','网络空间安全']
    # Define function to read CSV and return DataFrame
def read_data(i):
    df = pd.read_csv(f'./data_ins/{Institution_lst[i]}.csv')
    return df
if __name__ == '__main__':
   
    # # Streamlit widgets automatically run the script from top to bottom. Since
    # # this button is not connected to any other logic, it just causes a plain
    # # rerun.
    # st.button("Re-run")


    # Read CSV files into DataFrames
    df1 = read_data(1)
    df2 = read_data(2)
    df3 = read_data(3)
    df4 = read_data(4)

    # Concatenate the four DataFrames into one large DataFrame
    df = pd.concat([df1,df2,df3,df4], ignore_index=True)
    df = df[['title','time','pay']]
    # print(df)


        # Display the headings and the DataFrame

    st.title('USTC_CS1507 Homework1')
    
    colored_header(
    label=" A news crawling script",
    description="PB21050971梁家华",
    color_name="orange-80",
)
    
    st.write('# Displaying data from all colleges')
    st.write(df)

# streamlit run a:\xx\py\xuexi\Homework1\USTC_CS1507_Homework\visualization.py 