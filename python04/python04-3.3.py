import numpy as np
import matplotlib.pyplot as mp
import pandas as pd

index_list = ['学校名称', '科学研究', '服务社会', '学术人才', '重大项目与成果', '国际竞争力']
data = pd.read_csv('./rank.csv', engine='python', encoding='gb2312')[:5][index_list]
mp.figure('subplots', facecolor='pink')
mp.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
mp.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
vals = np.arange(1, 6)
texts = data[index_list[0]]
mp.xticks(vals, texts)
index = 0
for i in range(1, 10):
    if i in [1, 3, 5, 7, 9]:
        mp.subplot(3, 3, i)
        mp.xticks(vals, texts)
        ax = mp.gca()
        mp.xticks(vals, texts, rotation=45)
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')
        mp.bar(vals, data[index_list[index + 1]], label=index_list[index + 1])

        mp.legend()
        for a, b in zip(vals, data[index_list[index + 1]]):
            mp.text(a, b, '%.2f' % b, ha='center', va="bottom", fontsize=7)
        index += 1
mp.show()
