import numpy as np
import matplotlib.pyplot as mp
import pandas as pd

index_list = ['学校名称', '科学研究', '服务社会', '学术人才', '重大项目与成果', '国际竞争力']
data = pd.read_csv('./rank.csv', engine='python', encoding='gb2312')[:5][index_list]
mp.figure('bar', facecolor='blue')

ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
mp.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
mp.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
vals = np.arange(1, 6)
texts = data[index_list[0]]
mp.ylim(0, 140)
list1 = data[index_list[1]]
list2 = data[index_list[2]]
list3 = data[index_list[3]]
list4 = data[index_list[4]]
list5 = data[index_list[5]]

mp.xticks(vals, texts)
labels = index_list[1:6]
mp.bar(vals - 0.3, list1, width=0.15, alpha=1, label=labels[0])
mp.bar(vals - 0.15, list2, width=0.15, alpha=1, label=labels[1])
mp.bar(vals + 0, list3, width=0.15, alpha=1, label=labels[2])
mp.bar(vals + 0.15, list4, width=0.15, alpha=1, label=labels[3])
mp.bar(vals + 0.3, list5, width=0.15, alpha=1, label=labels[4])
for a, b in zip(vals-0.3, list1):
    mp.text(a, b, '%.2f' % b, ha='center', va="bottom", fontsize=7)
for a, b in zip(vals-0.15, list2):
    mp.text(a, b, '%.2f' % b, ha='center', va="bottom", fontsize=7)
for a, b in zip(vals, list3):
    mp.text(a, b, '%.2f' % b, ha='center', va="bottom", fontsize=7)
for a, b in zip(vals+0.15, list4):
    mp.text(a, b, '%.2f' % b, ha='center', va="bottom", fontsize=7)
for a, b in zip(vals+0.3, list5):
    mp.text(a, b, '%.2f' % b, ha='center', va="bottom", fontsize=7 )
mp.legend()
mp.show()
print(data)
