import plotly.express as px
import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
from streamlit_extras.colored_header import colored_header
import plotly.graph_objects as go
Institution_lst=['工程科学学院','先进技术','管理学院','化学与材料科学学院','大数据学院','中国科学院','少年班学院','地球和空间科学学院','公共事务学院','环境科学与工程','近代力学','信息','微电子学院','火灾科学国家重点实验室','计算机学院','核科学技术学院','同步辐射','生医部','热科学','精密仪器','物理学院','化学学院','马克思主义','金融','科技传播','微尺度','人文','数学学院','天文','网络空间安全']
Institution=['工程科学学院','先进技术研究院','管理学院','化学与材料科学学院','大数据学院','中国科学院','少年班学院','地球和空间科学学院','公共事务学院','环境科学与工程','近代力学','信息','微电子学院','火灾科学国家重点实验室','计算机学院','核科学技术学院','同步辐射','生医部','热科学','精密仪器','物理学院','化学学院','马克思主义','金融','科技传播','微尺度','人文','数学学院','天文','网络空间安全']
colors = ['#FFB6C1', '#FF69B4', '#FF1493', '#C71585', '#DA70D6', '#8B008B',
          '#4B0082', '#BA55D3', '#9932CC', '#8A2BE2', '#9400D3', '#6A5ACD',
          '#7B68EE', '#483D8B', '#0000FF', '#1E90FF', '#00BFFF', '#87CEFA',
          '#4682B4', '#00CED1', '#40E0D0', '#48D1CC', '#20B2AA', '#008080',
          '#008000', '#556B2F', '#6B8E23', '#9ACD32', '#ADFF2F', '#FFFF00']

def Overview():
    # Loop through each CSV file and read
    for i in range(0,len(Institution)):
        # Use pandas to read in the csv file
        df1 = pd.read_csv(f'./data_ins/{Institution_lst[i]}.csv')
        # Add a column, present Institution Name
        df1 = df1.assign(ins=f'{Institution[i]}')
        if i == 0:
            df = df1
        else:
            df = pd.concat([df,df1])
            
   
    # Converts the date column to the datetime type and sets it as an index
    df['date'] = pd.to_datetime(df['time'], format='%Y/%m%d')
    df.set_index('date', inplace=True)

     # Sum the fees for each college on each date and perform pivot table operations
    df_pivot = df.pivot_table(index=df.index, columns='ins', values='pay', aggfunc=sum, fill_value=0).cumsum()
    # Use Plotly to create a dynamic histogram

    fig = px.bar(df_pivot, x=df_pivot.index, y=df_pivot.columns,
                title='所有学院的稿费对比', 
                range_x=[pd.Timestamp('2022-05-01'), pd.Timestamp('2023-05-02')], 
                range_y=[0, df_pivot.max().max()],
                height=700,
                labels={'value': '累计稿费', 'index': '日期'})

    st.plotly_chart(fig)

    df_pivot = df.pivot_table(index=df.index, columns='ins', values='pay', aggfunc=sum, fill_value=0).cumsum()

    fig = go.Figure(data=[go.Bar(
                            x=df_pivot.sum(axis=0), 
                            y=df_pivot.columns, 
                            orientation='h',
                            marker_color=colors
                        )])
    fig.update_layout(
        title='每个学院的累计费用总和',
        xaxis_title='总费用',
        yaxis_title='学院名称'
    )

    st.plotly_chart(fig)
if __name__ == '__main__':
    colored_header(
    label="Overview",
    description="Cumulative contribution fees for each college",
    color_name="green-80",)
    Overview()