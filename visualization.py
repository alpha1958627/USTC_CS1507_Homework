import streamlit as st
import streamlit.components.v1 as components
from st_aggrid import AgGrid
from streamlit_echarts import st_pyecharts
import pandas as pd
import numpy as np
import time

# st.set_page_config(layout="wide")
Institution_lst = ['工程科学学院','先进技术','管理学院']
data = np.random.randn(2,3)
data2 = np.ones((2,3))
df = pd.DataFrame(data,columns=Institution_lst,index=['字数','图片数'])
df2 =pd.DataFrame(data2,columns=Institution_lst,index=['字数1','图片数1'])
df = pd.concat([df2,df], axis=0 ) #参数axis=0表示上下合并，1表示左右合并，ignore_index=True表示忽略原来的索引

if __name__ == '__main__':
    st.title('USTC_press release situation visualization')
    st.header('梁家华 PB21050971')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(df)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")