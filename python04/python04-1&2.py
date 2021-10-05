import numpy as np
import matplotlib.pyplot as mp
import pandas as pd

df = pd.read_csv("./rank.csv", engine="python", encoding='gb2312')[['学校名称', "省市", "总分"]]
grouped = df.groupby(['省市'], as_index=False)['总分'].agg(np.mean)
avgList = grouped.sort_values(by='总分', axis=0, ascending=False)
# from openpyxl import Workbook,load_workbook
# wb = Workbook()
# ws = wb.active
# headings = ['省市', '总分']
# ws.append(headings)
# i, j = 1, 1
# for province in list(avgList['省市'].values):
#     ws['A' + str(i+1)].value = province
#     i += 1
# for score in avgList['总分'].values:
#     ws['B' + str(j+1)].value = score
#     j += 1
# wb.save('./average123.xlsx')

print(avgList)
mp.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
mp.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
vals = np.arange(1, 32)
texts = avgList['省市'].values
mp.xticks(vals, texts, rotation=45)
ax = mp.gca()
mp.tight_layout()
y = avgList['总分'].values
mp.scatter(vals, y)
mp.plot(vals, y)
for a, b in zip(vals, y):
    mp.text(a, b, '%.2f' % b, rotation=45)

mp.show()
avgList.to_excel('./test.xlsx', index=False, encoding='gb2312')
