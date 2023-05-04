import pandas as pd
Institution_lst=['工程科学学院','先进技术','管理学院','化学与材料科学学院','大数据学院','中国科学院','少年班学院','地球和空间科学学院','公共事务学院','环境科学与工程','近代力学','信息','微电子学院','火灾科学国家重点实验室','计算机学院','核科学技术学院','同步辐射','生医部','热科学','精密仪器','物理学院','化学学院','马克思主义','金融','科技传播','微尺度','人文','数学学院','天文','网络空间安全']

df = pd.read_csv(f'./data_ins/{Institution_lst[1]}.csv')
df['date'] = pd.to_datetime(df['time'], format='%Y/%m%d')
print(df['date'])
print(df['pay'])
total_pay = df.groupby('date')['pay'].sum().reset_index()

print(total_pay['date'])