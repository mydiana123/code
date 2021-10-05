import requests
import tkinter as tk
import time
import hashlib
import random
salt = str(int(time.time()*1000)+random.randint(1, 10))

# 修改url 去掉-o 绕过反爬机制
url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko)'}


# kw = input('请输入你要翻译的内容')

def craw(cont):

    data = {'i': cont,
            'from': ' AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt, # 用于破解时间戳的表单信息
            'sign': '35cf0238520cd31629d50bcc196cc3dc',
            'lts': str(int(time.time()*1000)),
            'bv': 'c067065ab9f366d6a4ccd7dfdc8e96c5',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION'
            }
    data2 ={'i' : cont ,
            'from': 'zh - CHS',
            'to': 'ja' ,
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': '16324673282718',
            'sign': '7ceb8adf195d45c735dc45f648de8f63',
            'lts': '1632467328271',
            'bv': 'c067065ab9f366d6a4ccd7dfdc8e96c5',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION'}
    print(requests.post(url, headers=headers, data=data2).text)
    text = eval(requests.post(url, headers=headers, data=data).text)['translateResult'][0][0]['tgt']
    text2 = eval(requests.post(url, headers=headers, data=data).text)['translateResult'][0][0]['tgt']
    return text2

import hashlib
import json
import random
import time
import tkinter as tk

import requests
from lxml import etree

list1 = ['自动检测语言', '中文\xc2英语', '英语\xc2中文', '中文\xc2日语', '日语\xc2中文', '中文\xc2韩语', '韩语\xc2中文', '中文\xc2法语', '法语\xc2中文',
         '中文\xc2德语', '德语\xc2中文', '中文\xc2俄语', '俄语\xc2中文', '中文\xc2西班牙语', '西班牙语\xc2中文', '中文\xc2葡萄牙语', '葡萄牙语\xc2中文',
         '中文\xc2意大利语', '意大利语\xc2中文', '中文\xc2越南语', '越南语\xc2中文', '中文\xc2印尼语', '印尼语\xc2中文', '中文\xc2阿拉伯语', '阿拉伯语\xc2中文',
         '中文\xc2荷兰语', '荷兰语\xc2中文', '中文\xc2泰语', '泰语\xc2中文']
list2 = [['AUTO', 'AUTO'], ['zh-CHS', 'en'], ['en', 'zh-CHS'], ['zh-CHS', 'ja'], ['ja', 'zh-CHS'], ['zh-CHS', 'ko'],
         ['ko', 'zh-CHS'], ['zh-CHS', 'fr'], ['fr', 'zh-CHS'], ['zh-CHS', 'de'], ['de', 'zh-CHS'], ['zh-CHS', 'ru'],
         ['ru', 'zh-CHS'], ['zh-CHS', 'es'], ['es', 'zh-CHS'], ['zh-CHS', 'pt'], ['pt', 'zh-CHS'], ['zh-CHS', 'it'],
         ['it', 'zh-CHS'], ['zh-CHS', 'vi'], ['vi', 'zh-CHS'], ['zh-CHS', 'id'], ['id', 'zh-CHS'], ['zh-CHS', 'ar'],
         ['ar', 'zh-CHS'], ['zh-CHS', 'nl'], ['nl', 'zh-CHS'], ['zh-CHS', 'th'], ['th', 'zh-CHS']]
i = 0



class translate1(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
        self.url1 = 'http://fanyi.youdao.com/'
        self.url2 = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    def get_langSelect(self):
        lan_list = []
        text_list = []
        res = requests.get(url=self.url1, headers=self.headers)
        html = etree.HTML(res.text)
        li_list = html.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/ul//li')
        for i in li_list:
            dataval = i.xpath('./@data-value')[0].split('2')
            lan_list.append(dataval)
            text = i.xpath('./a/text()')[0].replace(' ', '').replace(' ', '').replace('\xa0', '')
            text_list.append(text)
        lan_list[0].append('AUTO')
        print(text_list)
        print(lan_list)
        return lan_list, text_list

    def crawler(self, i, ):
        # returnlist=list()
        header = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '239',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=48328342@10.108.160.100; OUTFOX_SEARCH_USER_ID_NCOO=276358647.14339805; JSESSIONID=aaaZHn7tLjpDiaro7Y2Hx; ___rl__test__cookies=%s' % (
                str(int(time.time() * 1000))),
            'Host': 'fanyi.youdao.com',
            'Origin': 'http', 'Referer': 'http',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }  # 我测试的时候，需要header里面需要添加cookies才能爬取到译文
        # cookies中只有___rl__test__cookies发生变化，而她的值就是当前时间戳
        client = 'fanyideskweb'
        salt = str(int(time.time() * 1000) + random.randint(1, 10))
        key = 'Tbh5E8=q6U3EXe+&L[4c@'
        sign = hashlib.md5((client + i + salt + key).encode('utf-8')).hexdigest()
        fromdata = {
            'i': i,
            'from': fromto[0],
            'to': fromto[1],
            'smartresult': 'dict',
            'client': client,
            'salt': salt,
            'sign': sign,
            'its': str(int(time.time() * 1000)),
            'bv': 'cda1e53e0c0eb8dd4002cefc117fa588',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'lan-select'
        }
        try:
            res = requests.post(url=self.url2, data=fromdata, headers=header)
            json_data = json.loads(res.text)
            # print(json_data)
            result_list = json_data['translateResult'][0]
            print(result_list)
            '''for i in result_list:
                result=i[0]['tgt']
                returnlist.append(result)'''
            return result_list[0]['tgt']
        except KeyError as e:
            self.args = e.args
            return None

spider = translate1()
def insert_point():
    var = entry.get()  # 已经读取了用户的输入内容
    t.delete('1.0', 'end')
    t.insert('insert', spider.crawler(var))  # 将读入的内容传入到爬虫函数里，并把返回的翻译结果重定向到输出区，注意方法要有返回值才行

def func():
    global i
    var2 = entry2.get()
    if var2 == 'ja':
        i = 3
        t.delete('1.0', 'end')
        t.insert('insert', '收到，请点击翻译')

    elif var2 == 'ko':
        i = 5
        t.delete('1.0', 'end')
        t.insert('insert', '收到，请点击翻译')
    elif var2 == 'en':
        i = 1
        t.delete('1.0', 'end')
        t.insert('insert', '收到，请点击翻译')
    elif var2 == 'ru':
        i = 11
        t.delete('1.0', 'end')
        t.insert('insert', '收到，请点击翻译')
    else:
        t.delete('1.0', 'end')
        t.insert('insert', '请重新输入，否则不予翻译')
    global fromto
    fromto = list2[i]
window = tk.Tk()
window.title('一嘉梓翻译')
window.geometry('400x600')
var = tk.StringVar()  # 类型变量对象要在实例化窗口之后创建
var2 = tk.StringVar()
# 设置可供选择的翻译语言选项

# 输入翻译的内容
label = tk.Label(text='想翻译成什么语言？ 日语-ja 韩语-ko 英文-en 俄语-ru 不输入自动检测', )
label.pack()
entry2 = tk.Entry(window, show=None)
entry2.pack()
button2 = tk.Button(window, command=func, width=5, height=1, text='确定')
button2.pack()
entry = tk.Entry(window, show=None)
entry.pack()
# 输出翻译结果的按钮
button = tk.Button(window, command=insert_point, width=5, height=1, text='翻译')
button.pack()
# 输出区
t = tk.Text(window, height=3, width=20)
t.pack()
# 画布
canvas = tk.Canvas(window, height=350, width=300, bg='pink')
image_file = tk.PhotoImage(file='diana.gif')
image_file2 = tk.PhotoImage(file='azi.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
image2 = canvas.create_image(200, 200, anchor='se', image=image_file2)
canvas.pack()
window.mainloop()
print(i)
spider.get_langSelect()